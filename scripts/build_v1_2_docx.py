#!/usr/bin/env python3
"""Build the black-and-white, formula-supported v1.2 course review DOCX."""

from __future__ import annotations

import importlib.util
import re
import zipfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "final" / "manuscript_v1.2.md"
OUTPUT = ROOT / "final" / "无线边缘网络中联邦学习通信效率优化方法研究综述_v1.2.docx"
BASE_SCRIPT = ROOT / "scripts" / "build_final_docx.py"


def load_base():
    spec = importlib.util.spec_from_file_location("fpwriting_base_builder_v12", BASE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {BASE_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def configure(base):
    class V12DocBuilder(base.DocBuilder):
        def mixed_text(self, paragraph, value):
            """Use live Word cross-references for citations, figures, tables and equations."""
            pos = 0
            token = re.compile(r"\[(\d+)\]|(图|表)(\d+)|式\((\d+)\)")
            for match in token.finditer(value):
                if match.start() > pos:
                    self.run(paragraph, value[pos : match.start()])
                if match.group(1):
                    number = match.group(1)
                    self.run(paragraph, "[")
                    self.field(paragraph, f" REF ref{number} \\h ", number)
                    self.run(paragraph, "]")
                elif match.group(2):
                    label, number = match.group(2), match.group(3)
                    self.run(paragraph, label)
                    self.field(paragraph, f" REF {'fig' if label == '图' else 'tab'}{number} \\h ", number)
                else:
                    number = match.group(4)
                    self.run(paragraph, "式(")
                    self.field(paragraph, f" REF eq{number} \\h ", number)
                    self.run(paragraph, ")")
                pos = match.end()
            if pos < len(value):
                self.run(paragraph, value[pos:])

        def add_inline_image(self, paragraph, path: Path, width_cm: float, name: str):
            img = Image.open(path)
            wemu = int(width_cm * 360000)
            hemu = int(wemu * img.height / img.width)
            rid = f"rIdImage{len(self.images) + 1}"
            self.images.append((rid, path))
            r = base.sub(paragraph, "w:r")
            drawing = base.sub(r, "w:drawing")
            inline = base.sub(drawing, "wp:inline", {"distT": "0", "distB": "0", "distL": "0", "distR": "0"})
            base.sub(inline, "wp:extent", {"cx": str(wemu), "cy": str(hemu)})
            base.sub(inline, "wp:effectExtent", {"l": "0", "t": "0", "r": "0", "b": "0"})
            did = self.drawing_id
            self.drawing_id += 1
            base.sub(inline, "wp:docPr", {"id": str(did), "name": name})
            c = base.sub(inline, "wp:cNvGraphicFramePr")
            base.sub(c, "a:graphicFrameLocks", {"noChangeAspect": "1"})
            graphic = base.sub(inline, "a:graphic")
            gd = base.sub(graphic, "a:graphicData", {"uri": "http://schemas.openxmlformats.org/drawingml/2006/picture"})
            pic = base.sub(gd, "pic:pic")
            nv = base.sub(pic, "pic:nvPicPr")
            base.sub(nv, "pic:cNvPr", {"id": str(did), "name": path.name})
            base.sub(nv, "pic:cNvPicPr")
            bf = base.sub(pic, "pic:blipFill")
            base.sub(bf, "a:blip", {"r:embed": rid})
            stretch = base.sub(bf, "a:stretch")
            base.sub(stretch, "a:fillRect")
            sp = base.sub(pic, "pic:spPr")
            xfrm = base.sub(sp, "a:xfrm")
            base.sub(xfrm, "a:off", {"x": "0", "y": "0"})
            base.sub(xfrm, "a:ext", {"cx": str(wemu), "cy": str(hemu)})
            geom = base.sub(sp, "a:prstGeom", {"prst": "rect"})
            base.sub(geom, "a:avLst")

        def image(self, path: Path, width_cm=15.5):
            p = self.p("Normal", align="center", keep_with_next=True)
            ppr = p.find(base.q("w:pPr"))
            base.sub(ppr, "w:spacing", {"w:before": "100", "w:after": "0"})
            self.add_inline_image(p, path, width_cm, f"黑白归纳图{self.drawing_id}")

        def equation(self, path: Path, width_cm: float, number: int):
            """Place a rendered equation and a live SEQ number in a borderless two-cell row."""
            tbl = base.sub(self.body, "w:tbl")
            pr = base.sub(tbl, "w:tblPr")
            base.sub(pr, "w:tblW", {"w:w": "9000", "w:type": "dxa"})
            base.sub(pr, "w:tblLayout", {"w:type": "fixed"})
            grid = base.sub(tbl, "w:tblGrid")
            base.sub(grid, "w:gridCol", {"w:w": "8250"})
            base.sub(grid, "w:gridCol", {"w:w": "750"})
            tr = base.sub(tbl, "w:tr")
            for idx, width in enumerate((8250, 750)):
                tc = base.sub(tr, "w:tc")
                tcpr = base.sub(tc, "w:tcPr")
                base.sub(tcpr, "w:tcW", {"w:w": str(width), "w:type": "dxa"})
                base.sub(tcpr, "w:vAlign", {"w:val": "center"})
                p = base.sub(tc, "w:p")
                ppr = base.sub(p, "w:pPr")
                base.sub(ppr, "w:pStyle", {"w:val": "Normal"})
                base.sub(ppr, "w:ind", {"w:firstLine": "0"})
                base.sub(ppr, "w:spacing", {"w:before": "40", "w:after": "40", "w:line": "240", "w:lineRule": "auto"})
                base.sub(ppr, "w:jc", {"w:val": "center" if idx == 0 else "right"})
                if idx == 0:
                    self.add_inline_image(p, path, width_cm, f"公式{number}")
                else:
                    self.run(p, "(")
                    self.field(p, " SEQ Equation \\* ARABIC ", str(number), bookmark=f"eq{number}")
                    self.run(p, ")")

        def table(self, rows):
            """Render a monochrome comparison table."""
            tbl = base.sub(self.body, "w:tbl")
            pr = base.sub(tbl, "w:tblPr")
            base.sub(pr, "w:tblW", {"w:w": "9000", "w:type": "dxa"})
            base.sub(pr, "w:tblLayout", {"w:type": "fixed"})
            borders = base.sub(pr, "w:tblBorders")
            for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
                base.sub(borders, f"w:{edge}", {"w:val": "single", "w:sz": "6", "w:space": "0", "w:color": "000000"})
            widths = [1250, 1700, 1300, 1300, 1650, 1800]
            grid = base.sub(tbl, "w:tblGrid")
            for width in widths:
                base.sub(grid, "w:gridCol", {"w:w": str(width)})
            for ri, row in enumerate(rows):
                tr = base.sub(tbl, "w:tr")
                for ci, value in enumerate(row):
                    tc = base.sub(tr, "w:tc")
                    tcpr = base.sub(tc, "w:tcPr")
                    base.sub(tcpr, "w:tcW", {"w:w": str(widths[ci]), "w:type": "dxa"})
                    base.sub(tcpr, "w:vAlign", {"w:val": "center"})
                    if ri == 0:
                        base.sub(tcpr, "w:shd", {"w:val": "clear", "w:fill": "E6E6E6"})
                    p = base.sub(tc, "w:p")
                    ppr = base.sub(p, "w:pPr")
                    base.sub(ppr, "w:pStyle", {"w:val": "TableText"})
                    base.sub(ppr, "w:jc", {"w:val": "center" if ri == 0 else "left"})
                    self.run(p, value, bold=(ri == 0), size=18)

    base.DocBuilder = V12DocBuilder
    return V12DocBuilder


def build_document(base, md: str):
    title = re.search(r"^# (.+)$", md, re.M).group(1)
    eng_title = re.search(r"\*\*英文题目：\*\*\s*(.+)", md).group(1).strip()
    zh_abs = re.search(r"## 摘要\n\n(.+?)\n\n\*\*关键词：\*\*\s*(.+?)\n", md, re.S)
    en_abs = re.search(r"## Abstract\n\n(.+?)\n\n\*\*Keywords:\*\*\s*(.+?)\n", md, re.S)
    body_text = md[md.index("## 1 引言") : md.index("## 参考文献")]
    refs_text = md[md.index("## 参考文献") + len("## 参考文献") :]

    b = base.DocBuilder()
    p = b.p("TitleCN", align="center", keep_with_next=True)
    b.run(p, title, east="黑体", size=32)
    p = b.p("Author", align="center", keep_with_next=True)
    b.run(p, "作者：________________")
    p = b.p("Author", align="center", keep_with_next=True)
    b.run(p, "作者单位：________________")
    p = b.p("EnglishTitle", align="center", keep_with_next=True)
    b.run(p, eng_title, bold=True, east="Times New Roman", size=32)
    p = b.p("AbstractCN")
    b.run(p, "摘要：", bold=True)
    b.run(p, zh_abs.group(1).strip())
    p = b.p("AbstractCN")
    b.run(p, "关键词：", bold=True)
    b.run(p, zh_abs.group(2).strip())
    p = b.p("EnglishAbstract")
    b.run(p, "Abstract: ", bold=True, east="Times New Roman")
    b.run(p, en_abs.group(1).strip(), east="Times New Roman")
    p = b.p("EnglishAbstract")
    b.run(p, "Keywords: ", bold=True, east="Times New Roman")
    b.run(p, en_abs.group(2).strip(), east="Times New Roman")

    lines = body_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith("## "):
            b.heading(line[3:], 0)
            i += 1
            continue
        if line.startswith("### "):
            b.heading(line[4:], 1)
            i += 1
            continue
        equation = re.match(r"\[\[EQUATION\s+(\d+)\s+(.+?)\s+([0-9.]+)\]\]", line)
        if equation:
            path = (SOURCE.parent / equation.group(2)).resolve()
            if not path.exists():
                raise FileNotFoundError(path)
            b.equation(path, float(equation.group(3)), int(equation.group(1)))
            i += 1
            continue
        image = re.match(r"!\[[^\]]*\]\(([^)]+\.png)\)", line)
        if image:
            path = (SOURCE.parent / image.group(1)).resolve()
            if not path.exists():
                raise FileNotFoundError(path)
            b.image(path, width_cm=15.5)
            i += 1
            continue
        if line.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i].strip())
                i += 1
            b.table(base.parse_table(block))
            continue
        caption = re.match(r"\*\*(图|表)(\d+)\s+(.+?)\*\*\s*(.*)$", line)
        if caption:
            kind = "fig" if caption.group(1) == "图" else "tab"
            caption_text = caption.group(3).strip()
            if caption.group(4).strip():
                caption_text += " " + caption.group(4).strip()
            b.caption(kind, int(caption.group(2)), caption_text)
            i += 1
            continue
        p = b.p("Normal")
        b.mixed_text(p, line)
        i += 1

    p = b.p("ReferenceHeading", keep_with_next=True)
    b.run(p, "参考文献")
    refs = re.findall(r"^\[(\d+)\]\s+(.+)$", refs_text, re.M)
    for number, text in refs:
        b.reference(int(number), text.strip())
    return b, b.finish()


def main() -> None:
    base = load_base()
    configure(base)
    md = SOURCE.read_text(encoding="utf-8")
    builder, document_xml = build_document(base, md)
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
        for index, (_, path) in enumerate(builder.images, 1):
            archive.write(path, f"word/media/image{index}.png")
    print(OUTPUT)


if __name__ == "__main__":
    main()
