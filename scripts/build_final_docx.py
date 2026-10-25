#!/usr/bin/env python3
"""Build the course-formatted DOCX from final/manuscript.md without changing content."""

from __future__ import annotations

import csv
import re
import shutil
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "final" / "manuscript.md"
OUTPUT = ROOT / "final" / "无线边缘网络中联邦学习通信效率优化方法研究综述.docx"
FONT_FILE = "/usr/share/fonts/google-noto-sans-cjk-vf-fonts/NotoSansCJK-VF.ttc"

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "pic": "http://schemas.openxmlformats.org/drawingml/2006/picture",
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
}
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)


def q(name: str) -> str:
    prefix, local = name.split(":", 1)
    return f"{{{NS[prefix]}}}{local}"


def E(name: str, attrs=None, text=None):
    el = ET.Element(q(name), {q(k) if ":" in k else k: str(v) for k, v in (attrs or {}).items()})
    if text is not None:
        el.text = text
    return el


def sub(parent, name: str, attrs=None, text=None):
    el = E(name, attrs, text)
    parent.append(el)
    return el


def xml_bytes(root) -> bytes:
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def font(size: int):
    return ImageFont.truetype(FONT_FILE, size=size, index=0)


def centered(draw, box, text, fnt, fill="#16324F"):
    x1, y1, x2, y2 = box
    bb = draw.multiline_textbbox((0, 0), text, font=fnt, spacing=5, align="center")
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    draw.multiline_text(((x1 + x2 - w) / 2, (y1 + y2 - h) / 2), text, font=fnt, fill=fill, spacing=5, align="center")


def rounded_box(draw, box, text, fill, outline="#28536B", radius=18, fnt=None):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=3)
    centered(draw, box, text, fnt or font(30))


def arrow(draw, start, end, fill="#58788C", width=5):
    draw.line([start, end], fill=fill, width=width)
    x2, y2 = end
    x1, y1 = start
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    s = 16
    pts = [(x2, y2), (x2 - s * math.cos(a - 0.45), y2 - s * math.sin(a - 0.45)),
           (x2 - s * math.cos(a + 0.45), y2 - s * math.sin(a + 0.45))]
    draw.polygon(pts, fill=fill)


def build_figures(tmp: Path):
    # Figure 1: architecture and bottlenecks
    im = Image.new("RGB", (1800, 920), "white")
    d = ImageDraw.Draw(im)
    title_f = font(38)
    box_f = font(30)
    small_f = font(25)
    d.text((900, 35), "无线边缘联邦学习架构与通信瓶颈", anchor="ma", font=title_f, fill="#102A43")
    cloud = (650, 110, 1150, 230)
    e1, e2 = (240, 365, 740, 495), (1060, 365, 1560, 495)
    devs = [(80, 690, 400, 800), (470, 690, 790, 800), (1010, 690, 1330, 800), (1400, 690, 1720, 800)]
    rounded_box(d, cloud, "云服务器\n全局聚合与模型下发", "#DCEEFF", fnt=box_f)
    rounded_box(d, e1, "边缘服务器 / 基站 A\n局部聚合与资源协调", "#E4F4E8", fnt=box_f)
    rounded_box(d, e2, "边缘服务器 / 基站 B\n局部聚合与资源协调", "#E4F4E8", fnt=box_f)
    for box, txt in zip(devs, ["终端群1\n本地训练", "终端群2\n异构设备", "终端群3\n移动终端", "终端群4\n物联网节点"]):
        rounded_box(d, box, txt, "#FFF1D6", fnt=small_f)
    for edge in (e1, e2):
        arrow(d, ((cloud[0] + cloud[2]) // 2, cloud[3]), ((edge[0] + edge[2]) // 2, edge[1]))
        arrow(d, ((edge[0] + edge[2]) // 2 + 24, edge[1]), ((cloud[0] + cloud[2]) // 2 + 24, cloud[3]))
    for edge, pair in ((e1, devs[:2]), (e2, devs[2:])):
        for box in pair:
            arrow(d, ((edge[0] + edge[2]) // 2, edge[3]), ((box[0] + box[2]) // 2, box[1]))
    d.text((330, 285), "边—云同步频率、跨域流量", font=small_f, fill="#9B2C2C")
    d.text((1080, 285), "边—云同步频率、跨域流量", font=small_f, fill="#9B2C2C")
    d.text((160, 575), "带宽 · 功率 · 时延", font=small_f, fill="#9B2C2C")
    d.text((1190, 575), "信道叠加 · 掉线 · 能耗", font=small_f, fill="#9B2C2C")
    fig1 = tmp / "figure1.png"
    im.save(fig1, dpi=(220, 220))

    # Figure 2: taxonomy
    im = Image.new("RGB", (1800, 880), "white")
    d = ImageDraw.Draw(im)
    d.text((900, 35), "通信效率优化方法分类框架", anchor="ma", font=title_f, fill="#102A43")
    center = (600, 310, 1200, 465)
    rounded_box(d, center, "无线边缘联邦学习\n通信效率优化", "#DCEEFF", fnt=box_f)
    boxes = [
        ((65, 120, 520, 255), "时间\n本地更新、异步与触发", "#E9F5DB"),
        ((1280, 120, 1735, 255), "参与者\n选择、调度与资源配置", "#E9F5DB"),
        ((65, 590, 520, 725), "载荷\n量化、稀疏与压缩感知", "#FFF1D6"),
        ((1280, 590, 1735, 725), "信道\n空中计算与模拟聚合", "#FFF1D6"),
        ((675, 665, 1125, 810), "拓扑\n分层聚合与边缘辅助", "#F4E8FA"),
    ]
    for box, txt, fill in boxes:
        rounded_box(d, box, txt, fill, fnt=small_f)
        sx = (center[0] + center[2]) // 2
        sy = center[1] if box[3] < center[1] else center[3]
        ex = (box[0] + box[2]) // 2
        ey = box[3] if box[3] < center[1] else box[1]
        arrow(d, (sx, sy), (ex, ey))
    d.text((900, 540), "跨层协同：频率 × 载荷 × 资源 × 聚合层级", anchor="ma", font=small_f, fill="#9B2C2C")
    fig2 = tmp / "figure2.png"
    im.save(fig2, dpi=(220, 220))
    return [fig1, fig2]


def make_styles():
    root = ET.Element(q("w:styles"))
    doc_defaults = sub(root, "w:docDefaults")
    rpr_d = sub(sub(doc_defaults, "w:rPrDefault"), "w:rPr")
    sub(rpr_d, "w:rFonts", {"w:ascii": "Times New Roman", "w:hAnsi": "Times New Roman", "w:eastAsia": "仿宋", "w:cs": "Times New Roman"})
    sub(rpr_d, "w:sz", {"w:val": "24"}); sub(rpr_d, "w:szCs", {"w:val": "24"})
    ppr_d = sub(sub(doc_defaults, "w:pPrDefault"), "w:pPr")
    sub(ppr_d, "w:spacing", {"w:line": "360", "w:lineRule": "auto", "w:after": "0"})

    def style(style_id, name, size, east="仿宋", bold=False, align=None, before=0, after=0,
              first=0, line=360, keep=False):
        st = sub(root, "w:style", {"w:type": "paragraph", "w:styleId": style_id})
        sub(st, "w:name", {"w:val": name})
        ppr = sub(st, "w:pPr")
        if align: sub(ppr, "w:jc", {"w:val": align})
        if first: sub(ppr, "w:ind", {"w:firstLine": str(first)})
        sub(ppr, "w:spacing", {"w:before": str(before), "w:after": str(after), "w:line": str(line), "w:lineRule": "auto"})
        if keep: sub(ppr, "w:keepNext")
        rpr = sub(st, "w:rPr")
        sub(rpr, "w:rFonts", {"w:ascii": "Times New Roman", "w:hAnsi": "Times New Roman", "w:eastAsia": east, "w:cs": "Times New Roman"})
        if bold: sub(rpr, "w:b"); sub(rpr, "w:bCs")
        sub(rpr, "w:sz", {"w:val": str(size)}); sub(rpr, "w:szCs", {"w:val": str(size)})
        sub(rpr, "w:lang", {"w:val": "en-US", "w:eastAsia": "zh-CN"})
        return st

    style("Normal", "正文", 24, first=480, line=360)
    style("TitleCN", "中文标题", 32, east="黑体", bold=False, align="center", after=160, keep=True)
    style("Author", "作者与单位", 21, align="center", after=40, keep=True)
    style("EnglishTitle", "英文标题", 32, east="Times New Roman", bold=True, align="center", before=100, after=180, keep=True)
    style("AbstractCN", "中文摘要", 21, first=0, line=315, after=80)
    style("EnglishAbstract", "英文摘要", 21, east="Times New Roman", first=0, line=315, after=80)
    style("Heading1", "一级标题", 28, bold=True, before=240, after=120, keep=True)
    style("Heading2", "二级标题", 28, bold=False, before=180, after=80, keep=True)
    style("Caption", "图表题注", 21, align="center", before=80, after=120, line=280, keep=True)
    style("Reference", "参考文献条目", 21, first=-420, line=300, after=30)
    style("ReferenceHeading", "参考文献标题", 28, bold=True, before=240, after=120, keep=True)
    style("TableText", "表格文字", 18, first=0, line=260, after=0)
    return xml_bytes(root)


def make_numbering():
    root = ET.Element(q("w:numbering"))
    abstract = sub(root, "w:abstractNum", {"w:abstractNumId": "1"})
    sub(abstract, "w:multiLevelType", {"w:val": "multilevel"})
    for lvl, text in ((0, "%1"), (1, "%1.%2")):
        le = sub(abstract, "w:lvl", {"w:ilvl": str(lvl)})
        sub(le, "w:start", {"w:val": "1"})
        sub(le, "w:numFmt", {"w:val": "decimal"})
        sub(le, "w:lvlText", {"w:val": text})
        sub(le, "w:lvlJc", {"w:val": "left"})
        if lvl == 1: sub(le, "w:lvlRestart", {"w:val": "0"})
        ppr = sub(le, "w:pPr"); sub(ppr, "w:tabs", {})
        sub(ppr, "w:ind", {"w:left": "0", "w:hanging": "0"})
        rpr = sub(le, "w:rPr"); sub(rpr, "w:rFonts", {"w:eastAsia": "仿宋"})
    num = sub(root, "w:num", {"w:numId": "1"}); sub(num, "w:abstractNumId", {"w:val": "1"})
    return xml_bytes(root)


class DocBuilder:
    def __init__(self):
        self.document = ET.Element(q("w:document"))
        self.body = sub(self.document, "w:body")
        self.bookmark_id = 1
        self.drawing_id = 1
        self.images = []

    def p(self, style="Normal", align=None, keep_with_next=False):
        p = sub(self.body, "w:p")
        ppr = sub(p, "w:pPr")
        sub(ppr, "w:pStyle", {"w:val": style})
        if align: sub(ppr, "w:jc", {"w:val": align})
        if keep_with_next: sub(ppr, "w:keepNext")
        return p

    def run(self, p, text, bold=False, east=None, size=None, italic=False):
        r = sub(p, "w:r")
        if bold or east or size or italic:
            rpr = sub(r, "w:rPr")
            if east: sub(rpr, "w:rFonts", {"w:ascii": "Times New Roman", "w:hAnsi": "Times New Roman", "w:eastAsia": east})
            if bold: sub(rpr, "w:b"); sub(rpr, "w:bCs")
            if italic: sub(rpr, "w:i"); sub(rpr, "w:iCs")
            if size: sub(rpr, "w:sz", {"w:val": str(size)}); sub(rpr, "w:szCs", {"w:val": str(size)})
        t = sub(r, "w:t", text=text)
        if text.startswith(" ") or text.endswith(" "): t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        return r

    def field(self, p, instruction, result, bookmark=None):
        bid = None
        if bookmark:
            bid = str(self.bookmark_id); self.bookmark_id += 1
            sub(p, "w:bookmarkStart", {"w:id": bid, "w:name": bookmark})
        fld = sub(p, "w:fldSimple", {"w:instr": instruction})
        self.run(fld, result)
        if bookmark:
            sub(p, "w:bookmarkEnd", {"w:id": bid})
        return fld

    def mixed_text(self, p, text):
        pos = 0
        for m in re.finditer(r"\[(\d+)\]", text):
            if m.start() > pos: self.run(p, text[pos:m.start()])
            n = m.group(1)
            self.run(p, "[")
            self.field(p, f" REF ref{n} \\h ", n)
            self.run(p, "]")
            pos = m.end()
        if pos < len(text): self.run(p, text[pos:])

    def heading(self, text, level):
        p = self.p("Heading1" if level == 0 else "Heading2", keep_with_next=True)
        ppr = p.find(q("w:pPr"))
        numpr = sub(ppr, "w:numPr")
        sub(numpr, "w:ilvl", {"w:val": str(level)})
        sub(numpr, "w:numId", {"w:val": "1"})
        clean = re.sub(r"^\d+(?:\.\d+)?\s+", "", text)
        self.run(p, clean)
        return p

    def ref_field(self, p, kind, number):
        self.field(p, f" REF {kind}{number} \\h ", str(number))

    def image(self, path: Path, width_cm=15.5):
        img = Image.open(path)
        wemu = int(width_cm * 360000)
        hemu = int(wemu * img.height / img.width)
        rid = f"rIdImage{len(self.images)+1}"
        self.images.append((rid, path))
        p = self.p("Normal", align="center", keep_with_next=True)
        ppr = p.find(q("w:pPr")); sub(ppr, "w:spacing", {"w:before": "100", "w:after": "0"})
        r = sub(p, "w:r"); drawing = sub(r, "w:drawing")
        inline = sub(drawing, "wp:inline", {"distT": "0", "distB": "0", "distL": "0", "distR": "0"})
        sub(inline, "wp:extent", {"cx": str(wemu), "cy": str(hemu)})
        sub(inline, "wp:effectExtent", {"l": "0", "t": "0", "r": "0", "b": "0"})
        did = self.drawing_id; self.drawing_id += 1
        sub(inline, "wp:docPr", {"id": str(did), "name": f"原创归纳图{did}"})
        c = sub(inline, "wp:cNvGraphicFramePr"); sub(c, "a:graphicFrameLocks", {"noChangeAspect": "1"})
        graphic = sub(inline, "a:graphic")
        gd = sub(graphic, "a:graphicData", {"uri": "http://schemas.openxmlformats.org/drawingml/2006/picture"})
        pic = sub(gd, "pic:pic")
        nv = sub(pic, "pic:nvPicPr"); sub(nv, "pic:cNvPr", {"id": str(did), "name": path.name}); sub(nv, "pic:cNvPicPr")
        bf = sub(pic, "pic:blipFill"); sub(bf, "a:blip", {"r:embed": rid}); stretch = sub(bf, "a:stretch"); sub(stretch, "a:fillRect")
        sp = sub(pic, "pic:spPr")
        xfrm = sub(sp, "a:xfrm"); sub(xfrm, "a:off", {"x": "0", "y": "0"}); sub(xfrm, "a:ext", {"cx": str(wemu), "cy": str(hemu)})
        geom = sub(sp, "a:prstGeom", {"prst": "rect"}); sub(geom, "a:avLst")

    def caption(self, kind, number, text):
        p = self.p("Caption", align="center", keep_with_next=False)
        label = "图" if kind == "fig" else "表"
        seq = "Figure" if kind == "fig" else "Table"
        self.run(p, label)
        self.field(p, f" SEQ {seq} \\* ARABIC ", str(number), bookmark=f"{kind}{number}")
        self.mixed_text(p, " " + text)

    def table(self, rows):
        tbl = sub(self.body, "w:tbl")
        pr = sub(tbl, "w:tblPr")
        sub(pr, "w:tblW", {"w:w": "9000", "w:type": "dxa"})
        sub(pr, "w:tblLayout", {"w:type": "fixed"})
        borders = sub(pr, "w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            sub(borders, f"w:{edge}", {"w:val": "single", "w:sz": "6", "w:space": "0", "w:color": "7F8C8D"})
        grid = sub(tbl, "w:tblGrid")
        widths = [1250, 1700, 1300, 1300, 1650, 1800]
        for x in widths: sub(grid, "w:gridCol", {"w:w": str(x)})
        for ri, row in enumerate(rows):
            tr = sub(tbl, "w:tr")
            for ci, value in enumerate(row):
                tc = sub(tr, "w:tc"); tcpr = sub(tc, "w:tcPr")
                sub(tcpr, "w:tcW", {"w:w": str(widths[ci]), "w:type": "dxa"})
                sub(tcpr, "w:vAlign", {"w:val": "center"})
                if ri == 0: sub(tcpr, "w:shd", {"w:val": "clear", "w:fill": "D9EAF4"})
                p = sub(tc, "w:p"); ppr = sub(p, "w:pPr"); sub(ppr, "w:pStyle", {"w:val": "TableText"}); sub(ppr, "w:jc", {"w:val": "center" if ri == 0 else "left"})
                self.run(p, value, bold=(ri == 0), size=18)

    def reference(self, number, text):
        p = self.p("Reference")
        ppr = p.find(q("w:pPr")); sub(ppr, "w:ind", {"w:left": "420", "w:hanging": "420"})
        self.run(p, "[")
        self.field(p, " SEQ Reference \\* ARABIC ", str(number), bookmark=f"ref{number}")
        self.run(p, "] " + text)

    def finish(self):
        sect = sub(self.body, "w:sectPr")
        sub(sect, "w:pgSz", {"w:w": "11906", "w:h": "16838", "w:orient": "portrait"})
        sub(sect, "w:pgMar", {"w:top": "1440", "w:right": "1440", "w:bottom": "1440", "w:left": "1440", "w:header": "720", "w:footer": "720", "w:gutter": "0"})
        sub(sect, "w:cols", {"w:space": "425"})
        sub(sect, "w:docGrid", {"w:linePitch": "312"})
        return xml_bytes(self.document)


def parse_table(lines):
    rows = []
    for line in lines:
        vals = [x.strip() for x in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", x) for x in vals):
            continue
        rows.append(vals)
    return rows


def build_document(md: str, figures):
    title = re.search(r"^# (.+)$", md, re.M).group(1)
    eng_title = re.search(r"\*\*英文题目：\*\*\s*(.+)", md).group(1).strip()
    zh_abs = re.search(r"## 摘要\n\n(.+?)\n\n\*\*关键词：\*\*\s*(.+?)\n", md, re.S)
    en_abs = re.search(r"## Abstract\n\n(.+?)\n\n\*\*Keywords:\*\*\s*(.+?)\n", md, re.S)
    body_text = md[md.index("## 1 引言"):md.index("## 参考文献")]
    refs_text = md[md.index("## 参考文献") + len("## 参考文献"):]

    b = DocBuilder()
    p = b.p("TitleCN", align="center", keep_with_next=True); b.run(p, title, east="黑体", size=32)
    p = b.p("Author", align="center", keep_with_next=True); b.run(p, "作者：________________")
    p = b.p("Author", align="center", keep_with_next=True); b.run(p, "作者单位：________________")
    p = b.p("EnglishTitle", align="center", keep_with_next=True); b.run(p, eng_title, bold=True, east="Times New Roman", size=32)

    p = b.p("AbstractCN"); b.run(p, "摘要：", bold=True); b.run(p, zh_abs.group(1).strip())
    p = b.p("AbstractCN"); b.run(p, "关键词：", bold=True); b.run(p, zh_abs.group(2).strip())
    p = b.p("EnglishAbstract"); b.run(p, "Abstract: ", bold=True, east="Times New Roman"); b.run(p, en_abs.group(1).strip(), east="Times New Roman")
    p = b.p("EnglishAbstract"); b.run(p, "Keywords: ", bold=True, east="Times New Roman"); b.run(p, en_abs.group(2).strip(), east="Times New Roman")

    lines = body_text.splitlines()
    i = 0
    fig_index = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1; continue
        if line.startswith("## "):
            b.heading(line[3:], 0); i += 1; continue
        if line.startswith("### "):
            b.heading(line[4:], 1); i += 1; continue
        if line.startswith("```mermaid"):
            while i < len(lines) and not (i > 0 and lines[i].strip() == "```"):
                i += 1
            i += 1
            b.image(figures[fig_index], width_cm=15.5)
            fig_index += 1
            continue
        if line.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i].strip()); i += 1
            b.table(parse_table(block)); continue
        m = re.match(r"\*\*(图|表)(\d+)\s+(.+?)\*\*\s*(.*)$", line)
        if m:
            kind = "fig" if m.group(1) == "图" else "tab"
            caption_text = m.group(3).strip()
            if m.group(4).strip():
                caption_text += " " + m.group(4).strip()
            b.caption(kind, int(m.group(2)), caption_text); i += 1; continue
        p = b.p("Normal")
        b.mixed_text(p, line)
        if "通信开销由模型大小、参与比例、同步频率、接入方式和聚合拓扑共同决定。" in line:
            b.run(p, " 无线边缘联邦学习架构与通信瓶颈见图")
            b.ref_field(p, "fig", 1); b.run(p, "。")
        elif "混合方案的组合关系见第4章。" in line:
            b.run(p, " 方法分类框架见图"); b.ref_field(p, "fig", 2); b.run(p, "。")
        elif "组合机制能够同时优化轮数、载荷和资源" in line:
            b.run(p, " 五类方法的横向比较见表"); b.ref_field(p, "tab", 1); b.run(p, "。")
        i += 1

    p = b.p("ReferenceHeading", keep_with_next=True); b.run(p, "参考文献")
    refs = re.findall(r"^\[(\d+)\]\s+(.+)$", refs_text, re.M)
    for n, text in refs:
        b.reference(int(n), text.strip())
    return b, b.finish()


def make_relationships(images):
    root = ET.Element("Relationships", xmlns="http://schemas.openxmlformats.org/package/2006/relationships")
    ET.SubElement(root, "Relationship", Id="rIdStyles", Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles", Target="styles.xml")
    ET.SubElement(root, "Relationship", Id="rIdNumbering", Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering", Target="numbering.xml")
    ET.SubElement(root, "Relationship", Id="rIdSettings", Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings", Target="settings.xml")
    ET.SubElement(root, "Relationship", Id="rIdFontTable", Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/fontTable", Target="fontTable.xml")
    for idx, (rid, path) in enumerate(images, 1):
        ET.SubElement(root, "Relationship", Id=rid, Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image", Target=f"media/image{idx}.png")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def static_parts():
    content = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Default Extension="png" ContentType="image/png"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
<Override PartName="/word/fontTable.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>""".encode()
    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>""".encode()
    settings = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:updateFields w:val="true"/><w:compat/><w:defaultTabStop w:val="420"/></w:settings>""".encode()
    fonts = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:fonts xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:font w:name="仿宋"/><w:font w:name="黑体"/><w:font w:name="Times New Roman"/></w:fonts>""".encode()
    core = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>无线边缘网络中联邦学习通信效率优化方法研究综述</dc:title><dc:subject>专业写作基础课程综述</dc:subject><dc:creator>作者信息待填写</dc:creator><cp:keywords>联邦学习; 无线边缘网络; 通信效率; 模型压缩; 分层聚合</cp:keywords><dcterms:created xsi:type="dcterms:W3CDTF">2026-10-11T00:00:00Z</dcterms:created></cp:coreProperties>""".encode()
    app = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>Codex OOXML Builder</Application><DocSecurity>0</DocSecurity><ScaleCrop>false</ScaleCrop><Company></Company><AppVersion>1.0</AppVersion></Properties>""".encode()
    return content, rels, settings, fonts, core, app


def main():
    md = SOURCE.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory(prefix="fpwriting-docx-") as td:
        tmp = Path(td)
        figures = build_figures(tmp)
        builder, document_xml = build_document(md, figures)
        content, rels, settings, fonts, core, app = static_parts()
        with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as z:
            z.writestr("[Content_Types].xml", content)
            z.writestr("_rels/.rels", rels)
            z.writestr("word/document.xml", document_xml)
            z.writestr("word/styles.xml", make_styles())
            z.writestr("word/numbering.xml", make_numbering())
            z.writestr("word/settings.xml", settings)
            z.writestr("word/fontTable.xml", fonts)
            z.writestr("word/_rels/document.xml.rels", make_relationships(builder.images))
            z.writestr("docProps/core.xml", core)
            z.writestr("docProps/app.xml", app)
            for idx, (_, path) in enumerate(builder.images, 1):
                z.write(path, f"word/media/image{idx}.png")
    print(OUTPUT)


if __name__ == "__main__":
    main()
