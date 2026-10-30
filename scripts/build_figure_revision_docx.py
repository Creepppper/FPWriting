#!/usr/bin/env python3
"""Build the figure-optimized DOCX while preserving the original submission file."""

from __future__ import annotations

import importlib.util
import re
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "final" / "manuscript_figure_revision.md"
OUTPUT = ROOT / "final" / "无线边缘网络中联邦学习通信效率优化方法研究综述_图示优化版.docx"
BASE_SCRIPT = ROOT / "scripts" / "build_final_docx.py"


def load_base():
    spec = importlib.util.spec_from_file_location("fpwriting_base_builder", BASE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {BASE_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def enable_body_cross_references(base) -> None:
    """Turn literal 图1/表1 mentions and [1] citations into Word REF fields."""

    def mixed_text(self, paragraph, value):
        pos = 0
        token = re.compile(r"\[(\d+)\]|(图|表)(\d+)")
        for match in token.finditer(value):
            if match.start() > pos:
                self.run(paragraph, value[pos : match.start()])
            if match.group(1):
                number = match.group(1)
                self.run(paragraph, "[")
                self.field(paragraph, f" REF ref{number} \\h ", number)
                self.run(paragraph, "]")
            else:
                label = match.group(2)
                number = match.group(3)
                self.run(paragraph, label)
                kind = "fig" if label == "图" else "tab"
                self.field(paragraph, f" REF {kind}{number} \\h ", number)
            pos = match.end()
        if pos < len(value):
            self.run(paragraph, value[pos:])

    base.DocBuilder.mixed_text = mixed_text


def collect_figures(markdown: str):
    figures = []

    def replace(match):
        relative = match.group(1)
        image_path = (SOURCE.parent / relative).resolve()
        if not image_path.exists():
            raise FileNotFoundError(image_path)
        figures.append(image_path)
        return "```mermaid\n%% external original synthesis figure\n```"

    converted = re.sub(r"^!\[[^\]]*\]\(([^)]+\.png)\)\s*$", replace, markdown, flags=re.M)
    if len(figures) != 4:
        raise RuntimeError(f"Expected 4 figures, found {len(figures)}")
    return converted, figures


def main() -> None:
    base = load_base()
    enable_body_cross_references(base)
    markdown, figures = collect_figures(SOURCE.read_text(encoding="utf-8"))

    with tempfile.TemporaryDirectory(prefix="fpwriting-figure-revision-"):
        builder, document_xml = base.build_document(markdown, figures)
        content, rels, settings, fonts, core, app = base.static_parts()
        with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("[Content_Types].xml", content)
            archive.writestr("_rels/.rels", rels)
            archive.writestr("word/document.xml", document_xml)
            archive.writestr("word/styles.xml", base.make_styles())
            archive.writestr("word/numbering.xml", base.make_numbering())
            archive.writestr("word/settings.xml", settings)
            archive.writestr("word/fontTable.xml", fonts)
            archive.writestr("word/_rels/document.xml.rels", base.make_relationships(builder.images))
            archive.writestr("docProps/core.xml", core)
            archive.writestr("docProps/app.xml", app)
            for index, (_, image_path) in enumerate(builder.images, 1):
                archive.write(image_path, f"word/media/image{index}.png")
    print(OUTPUT)


if __name__ == "__main__":
    main()
