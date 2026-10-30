#!/usr/bin/env python3
"""Generate grayscale, publication-style mechanism figures for manuscript v1.2."""

from __future__ import annotations

import html
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "v1.2"
W, H = 1800, 950

INK = "#111111"
MID = "#666666"
LIGHT = "#D8D8D8"
PALE = "#F3F3F3"
WHITE = "#FFFFFF"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def start() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="strokeWidth">
    <path d="M0,0 L10,5 L0,10 z" fill="{INK}"/>
  </marker>
  <marker id="arrow-gray" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="strokeWidth">
    <path d="M0,0 L10,5 L0,10 z" fill="{MID}"/>
  </marker>
  <style>
    text {{ font-family: "Noto Serif CJK SC", "Source Han Serif CN", "SimSun", serif; fill: {INK}; }}
    .panel {{ font-size: 31px; font-weight: 700; }}
    .label {{ font-size: 28px; font-weight: 600; }}
    .body {{ font-size: 25px; }}
    .small {{ font-size: 21px; }}
    .math {{ font-family: "Times New Roman", serif; font-size: 28px; font-style: italic; }}
  </style>
</defs>
<rect width="100%" height="100%" fill="{WHITE}"/>
'''


def end() -> str:
    return "</svg>\n"


def rect(x, y, w, h, fill=WHITE, stroke=INK, sw=2.4, rx=6, dash=None) -> str:
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def line(x1, y1, x2, y2, stroke=INK, sw=3, arrow=True, dash=None) -> str:
    marker = ' marker-end="url(#arrow)"' if arrow and stroke == INK else (' marker-end="url(#arrow-gray)"' if arrow else "")
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"{marker}{d}/>'


def path(data, stroke=INK, sw=3, arrow=True, dash=None) -> str:
    marker = ' marker-end="url(#arrow)"' if arrow and stroke == INK else (' marker-end="url(#arrow-gray)"' if arrow else "")
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{data}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{marker}{d}/>'


def text(x, y, value, cls="body", anchor="middle") -> str:
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{esc(value)}</text>'


def multiline(x, y, values, cls="body", anchor="middle", gap=34) -> str:
    spans = []
    for idx, value in enumerate(values):
        spans.append(f'<tspan x="{x}" dy="{0 if idx == 0 else gap}">{esc(value)}</tspan>')
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">' + "".join(spans) + "</text>"


def server(x, y, w=150, h=90, label="服务器") -> str:
    return rect(x, y, w, h, PALE, INK, 2.8, 5) + line(x + 18, y + 27, x + w - 18, y + 27, MID, 1.5, False) + line(x + 18, y + 52, x + w - 18, y + 52, MID, 1.5, False) + text(x + w / 2, y + h + 31, label, "small")


def device(x, y, label, w=92, h=118) -> str:
    return rect(x, y, w, h, WHITE, INK, 2.6, 10) + line(x + 14, y + 18, x + w - 14, y + 18, MID, 1.4, False) + f'<circle cx="{x+w/2}" cy="{y+h-11}" r="3.5" fill="{INK}"/>' + text(x + w / 2, y + h + 29, label, "small")


def dataset(x, y, label) -> str:
    return (
        f'<ellipse cx="{x+45}" cy="{y+10}" rx="45" ry="10" fill="{WHITE}" stroke="{INK}" stroke-width="2.3"/>'
        f'<path d="M{x},{y+10} v54 c0,11 90,11 90,0 v-54" fill="{WHITE}" stroke="{INK}" stroke-width="2.3"/>'
        f'<path d="M{x},{y+36} c0,11 90,11 90,0" fill="none" stroke="{MID}" stroke-width="1.4"/>'
        + text(x + 45, y + 98, label, "small")
    )


def write(name: str, body: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    svg = OUT / f"{name}.svg"
    png = OUT / f"{name}.png"
    svg.write_text(start() + body + end(), encoding="utf-8")
    subprocess.run(["rsvg-convert", "-w", "3600", "-h", "1900", "-o", str(png), str(svg)], check=True)


def figure1() -> str:
    s = []
    panels = [(55, "(a) 全局模型下发"), (625, "(b) 终端本地训练"), (1195, "(c) 更新上传与聚合")]
    for x, title in panels:
        s.append(rect(x, 65, 520, 750, WHITE, INK, 2.2, 0))
        s.append(text(x + 260, 112, title, "panel"))

    s.append(server(235, 155, 160, 95, "参数服务器"))
    s.append(text(315, 143, "全局模型 wₜ", "math"))
    for i, x in enumerate([115, 260, 405], 1):
        s.append(device(x, 565, f"客户端 {i if i < 3 else 'K'}"))
        s.append(line(315, 275, x + 46, 548, INK, 3.2, True))
        s.append(text((315 + x + 46) / 2, 405, "wₜ", "math"))
    s.append(multiline(315, 755, ["广播开销随参与规模、模型大小", "和下行链路条件增加"], "body", gap=38))

    for i, x in enumerate([685, 830, 975], 1):
        s.append(dataset(x, 180, f"D{i if i < 3 else 'K'}"))
        s.append(device(x, 430, f"客户端 {i if i < 3 else 'K'}"))
        s.append(line(x + 45, 300, x + 46, 413, MID, 2.7, True))
        s.append(text(x + 46, 390, "E 次本地更新", "small"))
    s.append(rect(705, 640, 370, 88, PALE, INK, 2, 3))
    s.append(text(890, 677, "wₖ,ₜ⁽ᴱ⁾ = LocalUpdate(wₜ,Dₖ)", "math"))
    s.append(text(890, 710, "以终端计算换取更少的全局交互", "small"))
    s.append(text(890, 778, "本地步数过大会放大非独立同分布漂移", "body"))

    s.append(server(1375, 155, 160, 95, "参数服务器"))
    for i, x in enumerate([1255, 1400, 1545], 1):
        s.append(device(x, 565, f"客户端 {i if i < 3 else 'K'}"))
        s.append(line(x + 46, 548, 1455, 285, INK, 3.2, True))
        s.append(text(x + 46, 535, f"Δw{i if i < 3 else 'K'},ₜ", "math"))
    s.append(rect(1280, 315, 350, 82, PALE, INK, 2, 3))
    s.append(text(1455, 350, "wₜ₊₁ = Σₖ αₖ wₖ,ₜ⁽ᴱ⁾", "math"))
    s.append(text(1455, 381, "加权聚合", "small"))
    s.append(multiline(1455, 755, ["上行载荷、等待最慢终端和", "无线信道共同决定单轮完成时间"], "body", gap=38))

    s.append(path("M1455,815 C1455,900 315,900 315,815", MID, 2.8, True, "10 9"))
    s.append(text(885, 890, "重复执行，直至达到预设精度或训练轮数", "label"))
    return "".join(s)


def figure2() -> str:
    s = []
    s.append(text(900, 58, "五类通信效率方法在无线边缘联邦学习流程中的作用位置", "panel"))
    s.append(rect(65, 330, 1670, 245, WHITE, INK, 2.4, 0))
    nodes = [
        (95, 385, 230, 120, "参与客户端集合", "Sₜ"),
        (405, 385, 230, 120, "模型下发", "Bₜ↓"),
        (715, 385, 230, 120, "本地训练", "Eₖ,ₜ"),
        (1025, 385, 230, 120, "无线上传", "Bₖ,ₜ↑"),
        (1335, 385, 230, 120, "边缘/云聚合", "wₜ₊₁"),
    ]
    for idx, (x, y, w, h, lab, sym) in enumerate(nodes):
        s.append(rect(x, y, w, h, PALE if idx % 2 == 0 else WHITE, INK, 2.2, 4))
        s.append(text(x + w / 2, y + 47, lab, "label"))
        s.append(text(x + w / 2, y + 91, sym, "math"))
        if idx < len(nodes) - 1:
            s.append(line(x + w, y + h / 2, nodes[idx + 1][0] - 12, y + h / 2, INK, 3.2, True))
    s.append(path("M1450,585 C1450,720 520,720 520,585", MID, 2.7, True, "10 8"))
    s.append(text(985, 748, "下一轮", "small"))

    callouts = [
        (65, 105, 300, 145, "① 客户端选择与资源配置", ["决定谁参与、分配多少", "带宽、功率与算力"], 210, 330),
        (390, 105, 300, 145, "② 模型/梯度压缩", ["减少下行或上行的", "参数位数与非零元素"], 520, 330),
        (715, 105, 300, 145, "③ 本地更新与频率控制", ["改变本地步数、触发条件", "和全局交互轮数"], 830, 330),
        (1040, 105, 300, 145, "④ 空中计算", ["利用多址叠加并发完成", "上传与求和"], 1140, 330),
        (1365, 105, 300, 145, "⑤ 分层与边缘辅助", ["重组端—边—云流量", "和聚合时间尺度"], 1450, 330),
    ]
    for x, y, w, h, title, desc, tx, ty in callouts:
        s.append(rect(x, y, w, h, WHITE, INK, 2.1, 0))
        s.append(text(x + w / 2, y + 42, title, "small"))
        s.append(multiline(x + w / 2, y + 82, desc, "small", gap=30))
        s.append(line(x + w / 2, y + h, tx, ty, MID, 2.4, True, "8 7"))

    s.append(rect(210, 815, 1380, 80, PALE, INK, 1.8, 0))
    s.append(text(900, 851, "统一评价：在相同目标精度下比较累计比特量、通信轮数、端到端时延与能耗", "label"))
    s.append(text(900, 882, "局部指标改善不等于系统总成本必然下降", "small"))
    return "".join(s)


def figure3() -> str:
    s = []
    s.append(rect(55, 65, 805, 800, WHITE, INK, 2.3, 0))
    s.append(rect(940, 65, 805, 800, WHITE, INK, 2.3, 0))
    s.append(text(457, 112, "(a) 数字正交上传：分别传输、分别解码、再聚合", "panel"))
    s.append(text(1342, 112, "(b) 空中聚合：同时传输、信道叠加、直接估计", "panel"))

    ys = [205, 385, 565]
    for i, y in enumerate(ys, 1):
        s.append(device(115, y, f"终端 {i if i < 3 else 'K'}", 82, 104))
        s.append(line(240, y + 48, 555, y + 48, INK, 3.1, True))
        s.append(text(395, y + 32, f"资源块 {i if i < 3 else 'K'}：q(g{i if i < 3 else 'K'})", "math"))
    s.append(server(610, 335, 150, 95, "基站"))
    s.append(rect(555, 520, 260, 100, PALE, INK, 2.1, 2))
    s.append(multiline(685, 555, ["分别解码", "q(g₁),…,q(gₖ)"], "body", gap=36))
    s.append(line(685, 455, 685, 505, INK, 2.8, True))
    s.append(rect(230, 710, 455, 78, WHITE, INK, 2.1, 2))
    s.append(text(457, 760, "服务器执行数字加权求和", "label"))
    s.append(line(565, 620, 520, 700, INK, 2.8, True))
    s.append(text(457, 825, "所需正交资源通常随参与终端数增加", "body"))

    for i, y in enumerate(ys, 1):
        s.append(device(990, y, f"终端 {i if i < 3 else 'K'}", 82, 104))
        s.append(path(f"M1110,{y+48} C1220,{y+48} 1310,410 1430,410", INK, 3.1, True))
        s.append(text(1205, y + 30, f"b{i if i < 3 else 'K'}g{i if i < 3 else 'K'}", "math"))
    s.append(text(1245, 175, "同一时频资源", "label"))
    s.append(server(1490, 335, 150, 95, "基站"))
    s.append(text(1440, 305, "+ n", "math"))
    s.append(line(1460, 255, 1460, 370, MID, 2.5, True))
    s.append(rect(1130, 575, 470, 105, PALE, INK, 2.1, 2))
    s.append(text(1365, 617, "yₜ = Σₖ hₖ,ₜ bₖ,ₜ gₖ,ₜ + nₜ", "math"))
    s.append(text(1365, 657, "经信道补偿后估计加权更新", "body"))
    s.append(line(1565, 455, 1510, 560, INK, 2.8, True))
    s.append(rect(1050, 720, 585, 78, WHITE, INK, 2.1, 2))
    s.append(text(1342, 767, "收益依赖同步、信道估计和功率对齐", "label"))
    s.append(text(1342, 842, "噪声与深衰落直接形成聚合误差", "body"))
    return "".join(s)


def figure4() -> str:
    s = []
    s.append(text(900, 55, "端—边—云分层联邦学习与双时间尺度聚合", "panel"))
    s.append(rect(65, 90, 1670, 745, WHITE, INK, 2.3, 0))
    s.append(text(135, 165, "云层", "label", "start"))
    s.append(text(135, 420, "边缘层", "label", "start"))
    s.append(text(135, 705, "设备层", "label", "start"))
    s.append(line(220, 205, 1670, 205, LIGHT, 2, False))
    s.append(line(220, 505, 1670, 505, LIGHT, 2, False))

    s.append(server(825, 105, 170, 95, ""))
    s.append(text(910, 165, "云服务器", "label"))
    edge_x = [435, 825, 1215]
    for idx, x in enumerate(edge_x, 1):
        s.append(server(x, 350, 150, 90, ""))
        s.append(text(x + 75, 405, f"边缘节点 {idx}", "small"))
        target_x = [850, 910, 970][idx - 1]
        s.append(line(x + 75, 340, target_x, 215, MID, 3, True, "10 8"))
        s.append(text((x + 75 + target_x) / 2, 286, "低频边—云同步", "small"))
        for j, dx in enumerate([-105, 0, 105], 1):
            cx = x + 29 + dx
            s.append(device(cx, 610, f"k{idx}{j}", 70, 95))
            s.append(line(cx + 35, 596, x + 75, 465, INK, 2.7, True))
        s.append(path(f"M{x+5},550 C{x-25},525 {x+175},525 {x+145},550", INK, 2.2, False, "7 6"))
        s.append(text(x + 75, 575, "高频端—边聚合", "small"))

    s.append(rect(235, 740, 460, 58, PALE, INK, 1.8, 0))
    s.append(text(465, 778, "端—边：多次局部聚合，缩短接入距离", "small"))
    s.append(rect(705, 740, 465, 58, PALE, INK, 1.8, 0))
    s.append(text(937, 778, "边—云：较少全局同步，减少骨干流量", "small"))
    s.append(rect(1180, 740, 470, 58, PALE, INK, 1.8, 0))
    s.append(text(1415, 778, "代价：两级漂移、边缘负载与同步控制", "small"))
    s.append(text(900, 890, "评价时应分别统计端—边与边—云流量、聚合间隔、等待时间和附加计算", "label"))
    return "".join(s)


def main() -> None:
    write("fig01_fl_process_bw", figure1())
    write("fig02_method_locations_bw", figure2())
    write("fig03_digital_aircomp_bw", figure3())
    write("fig04_hierarchical_bw", figure4())
    print(OUT)


if __name__ == "__main__":
    main()
