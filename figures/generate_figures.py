#!/usr/bin/env python3
"""Generate editable SVG and 300 dpi PNG figures for the review manuscript.

The figures are original synthesis diagrams.  They encode mechanisms and
comparisons supported by the cited literature; they do not reproduce any
source figure or source data.
"""

from __future__ import annotations

import html
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
W, H = 1600, 900

COLORS = {
    "ink": "#203040",
    "muted": "#5D6B78",
    "line": "#64788A",
    "blue": "#3973A8",
    "blue_fill": "#E8F1F8",
    "teal": "#2B8C87",
    "teal_fill": "#E5F4F2",
    "orange": "#D48735",
    "orange_fill": "#FFF1DE",
    "red": "#C65B5B",
    "red_fill": "#FAE9E9",
    "violet": "#7666AF",
    "violet_fill": "#EFECF8",
    "gray_fill": "#F4F6F7",
}


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def svg_start() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">
    <path d="M0,0 L12,6 L0,12 z" fill="context-stroke"/>
  </marker>
  <marker id="arrow-small" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto" markerUnits="strokeWidth">
    <path d="M0,0 L9,4.5 L0,9 z" fill="context-stroke"/>
  </marker>
  <style>
    text {{ font-family: "Noto Sans CJK SC", "Source Han Sans SC", "Microsoft YaHei", sans-serif; fill: {COLORS['ink']}; }}
    .label {{ font-size: 28px; font-weight: 600; }}
    .body {{ font-size: 24px; }}
    .small {{ font-size: 21px; }}
    .tiny {{ font-size: 18px; }}
    .panel {{ font-size: 26px; font-weight: 700; }}
    .metric {{ font-size: 22px; font-weight: 600; }}
  </style>
</defs>
<rect width="100%" height="100%" fill="#FFFFFF"/>
'''


def svg_end() -> str:
    return "</svg>\n"


def rect(x, y, w, h, fill, stroke=None, rx=18, sw=2, dash=None) -> str:
    stroke = stroke or COLORS["line"]
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{ds}/>'


def line(x1, y1, x2, y2, color=None, sw=3, arrow=True, dash=None) -> str:
    color = color or COLORS["line"]
    mk = ' marker-end="url(#arrow)"' if arrow else ""
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"{mk}{ds}/>'


def path(d, color=None, sw=3, arrow=True, dash=None, fill="none") -> str:
    color = color or COLORS["line"]
    mk = ' marker-end="url(#arrow)"' if arrow else ""
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{mk}{ds}/>'


def text(x, y, value, cls="body", anchor="middle", color=None, weight=None) -> str:
    attrs = f' class="{cls}" text-anchor="{anchor}"'
    if color:
        attrs += f' fill="{color}" style="fill:{color}"'
    if weight:
        attrs += f' font-weight="{weight}"'
    return f'<text x="{x}" y="{y}"{attrs}>{esc(value)}</text>'


def multiline(x, y, lines, cls="body", anchor="middle", gap=34, color=None, weight=None) -> str:
    attrs = f' class="{cls}" text-anchor="{anchor}"'
    if color:
        attrs += f' fill="{color}" style="fill:{color}"'
    if weight:
        attrs += f' font-weight="{weight}"'
    spans = []
    for i, item in enumerate(lines):
        dy = "0" if i == 0 else str(gap)
        spans.append(f'<tspan x="{x}" dy="{dy}">{esc(item)}</tspan>')
    return f'<text x="{x}" y="{y}"{attrs}>' + "".join(spans) + "</text>"


def phone(x, y, scale=1.0, color=None) -> str:
    color = color or COLORS["blue"]
    w, h = 58 * scale, 96 * scale
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{9*scale}" fill="#FFFFFF" stroke="{color}" stroke-width="{3*scale}"/>'
        f'<line x1="{x+12*scale}" y1="{y+14*scale}" x2="{x+w-12*scale}" y2="{y+14*scale}" stroke="{color}" stroke-width="{2*scale}"/>'
        f'<circle cx="{x+w/2}" cy="{y+h-10*scale}" r="{3*scale}" fill="{color}"/>'
    )


def database(x, y, scale=1.0, color=None) -> str:
    color = color or COLORS["teal"]
    w, h = 70 * scale, 70 * scale
    return (
        f'<ellipse cx="{x+w/2}" cy="{y+10*scale}" rx="{w/2}" ry="{10*scale}" fill="#FFFFFF" stroke="{color}" stroke-width="{3*scale}"/>'
        f'<path d="M{x},{y+10*scale} v{h-20*scale} c0,{12*scale} {w},{12*scale} {w},0 v-{h-20*scale}" fill="#FFFFFF" stroke="{color}" stroke-width="{3*scale}"/>'
        f'<path d="M{x},{y+35*scale} c0,{12*scale} {w},{12*scale} {w},0" fill="none" stroke="{color}" stroke-width="{2*scale}"/>'
    )


def server(x, y, scale=1.0, color=None) -> str:
    color = color or COLORS["violet"]
    w, h = 100 * scale, 112 * scale
    parts = []
    for i in range(3):
        yy = y + i * 35 * scale
        parts.append(f'<rect x="{x}" y="{yy}" width="{w}" height="{28*scale}" rx="{5*scale}" fill="#FFFFFF" stroke="{color}" stroke-width="{3*scale}"/>')
        parts.append(f'<circle cx="{x+14*scale}" cy="{yy+14*scale}" r="{4*scale}" fill="{color}"/>')
    return "".join(parts)


def antenna(x, y, scale=1.0, color=None) -> str:
    color = color or COLORS["orange"]
    return (
        f'<line x1="{x}" y1="{y+78*scale}" x2="{x}" y2="{y+20*scale}" stroke="{color}" stroke-width="{4*scale}"/>'
        f'<circle cx="{x}" cy="{y+14*scale}" r="{7*scale}" fill="{color}"/>'
        f'<path d="M{x-18*scale},{y+2*scale} Q{x-36*scale},{y+14*scale} {x-18*scale},{y+28*scale}" fill="none" stroke="{color}" stroke-width="{4*scale}"/>'
        f'<path d="M{x+18*scale},{y+2*scale} Q{x+36*scale},{y+14*scale} {x+18*scale},{y+28*scale}" fill="none" stroke="{color}" stroke-width="{4*scale}"/>'
        f'<line x1="{x}" y1="{y+78*scale}" x2="{x-27*scale}" y2="{y+112*scale}" stroke="{color}" stroke-width="{4*scale}"/>'
        f'<line x1="{x}" y1="{y+78*scale}" x2="{x+27*scale}" y2="{y+112*scale}" stroke="{color}" stroke-width="{4*scale}"/>'
    )


def pill(x, y, w, label, fill, color) -> str:
    return rect(x, y, w, 48, fill, color, rx=24, sw=2) + text(x + w / 2, y + 32, label, "small", color=color, weight="600")


def write_svg(name: str, body: str) -> Path:
    path_out = OUT / f"{name}.svg"
    path_out.write_text(svg_start() + body + svg_end(), encoding="utf-8")
    png = OUT / f"{name}.png"
    subprocess.run(
        ["rsvg-convert", "-w", "3200", "-h", "1800", "-o", str(png), str(path_out)],
        check=True,
    )
    return path_out


def figure_1() -> str:
    s = []
    s.append(rect(55, 70, 270, 215, COLORS["blue_fill"], COLORS["blue"], 24, 3))
    s.append(server(105, 118, 1.1, COLORS["blue"]))
    s.append(multiline(230, 135, ["聚合端", "全局模型 wₜ"], "label", gap=43, color=COLORS["blue"]))
    s.append(text(190, 250, "选择终端并广播模型", "small", color=COLORS["muted"]))

    s.append(rect(470, 70, 620, 420, COLORS["gray_fill"], "#AAB5BE", 24, 2))
    s.append(text(780, 112, "入选终端：数据留在本地，仅交换模型更新", "label"))
    client_x = [535, 735, 935]
    labels = ["终端1", "终端2", "终端K"]
    for x, lab in zip(client_x, labels):
        s.append(phone(x, 158, 0.9, COLORS["blue"]))
        s.append(database(x + 82, 170, 0.75, COLORS["teal"]))
        s.append(text(x + 65, 292, lab, "small"))
        s.append(rect(x - 10, 320, 150, 92, "#FFFFFF", COLORS["teal"], 14, 2))
        s.append(multiline(x + 65, 350, ["本地训练", "E 步更新"], "small", gap=30, color=COLORS["teal"]))
        s.append(line(x + 65, 300, x + 65, 316, COLORS["teal"], 2, True))
    s.append(pill(610, 430, 340, "异构算力 · 非独立同分布 · 掉线", COLORS["orange_fill"], COLORS["orange"]))

    s.append(rect(1255, 70, 290, 215, COLORS["violet_fill"], COLORS["violet"], 24, 3))
    s.append(text(1400, 120, "服务器聚合", "label", color=COLORS["violet"]))
    s.append(text(1400, 178, "Σ 加权更新", "label", color=COLORS["violet"]))
    s.append(text(1400, 235, "得到 wₜ₊₁", "label", color=COLORS["violet"]))

    s.append(line(325, 175, 470, 175, COLORS["blue"], 5, True))
    s.append(multiline(398, 118, ["① 模型下发", "下行载荷"], "small", gap=31, color=COLORS["blue"]))
    s.append(line(1090, 240, 1255, 240, COLORS["orange"], 5, True))
    s.append(multiline(1172, 156, ["③ 更新上传", "带宽 · 功率", "衰落 · 排队"], "small", gap=29, color=COLORS["orange"]))
    s.append(path("M1400,285 C1400,560 190,560 190,285", COLORS["violet"], 4, True, "12 9"))
    s.append(text(795, 585, "④ 进入下一轮：重复交互直至达到目标精度", "label", color=COLORS["violet"]))
    s.append(pill(610, 505, 340, "② 以本地计算换取更少全局交互", COLORS["teal_fill"], COLORS["teal"]))

    s.append(rect(90, 660, 1420, 170, "#F8FAFB", "#9EABB5", 20, 2))
    s.append(text(800, 705, "通信成本的形成", "label"))
    s.append(text(800, 753, "累计开销 ≈ 通信轮数 ×（每轮下行载荷 + 每轮上行载荷）+ 控制开销", "body", color=COLORS["ink"]))
    metrics = [
        (210, "累计比特量", COLORS["blue_fill"], COLORS["blue"]),
        (540, "端到端时延", COLORS["orange_fill"], COLORS["orange"]),
        (870, "通信能耗", COLORS["teal_fill"], COLORS["teal"]),
        (1200, "目标精度约束", COLORS["violet_fill"], COLORS["violet"]),
    ]
    for x, lab, fill, color in metrics:
        s.append(pill(x, 775, 230, lab, fill, color))
    return "".join(s)


def figure_2() -> str:
    s = []
    s.append(text(215, 83, "优化杠杆", "panel", color=COLORS["muted"]))
    s.append(text(755, 83, "主要改变的通信要素", "panel", color=COLORS["muted"]))
    s.append(text(1325, 83, "优先观察的指标与代价", "panel", color=COLORS["muted"]))
    rows = [
        (125, "时间 / 频率", "本地多步更新 · 异步 · 事件触发", "减少或重排全局交互轮次 R", "轮数 / 陈旧度 / 本地计算", COLORS["blue"], COLORS["blue_fill"]),
        (275, "参与者 / 资源", "客户端选择 · 调度 · 带宽功率分配", "改变每轮参与集合 Kₜ 与完成时间", "时延 / 能耗 / 公平性 / 控制开销", COLORS["teal"], COLORS["teal_fill"]),
        (425, "传输载荷", "量化 · 稀疏化 · 剪枝 · 压缩感知", "降低单次下发或上传的比特量 Bₜ", "累计比特 / 精度损失 / 编解码", COLORS["orange"], COLORS["orange_fill"]),
        (575, "无线信道", "空中计算 · 模拟聚合", "把多用户上传与求和合并", "聚合时延 / 频谱 / 聚合误差", COLORS["red"], COLORS["red_fill"]),
        (725, "聚合拓扑", "边缘局部聚合 · 分层与边缘辅助", "重组端—边—云之间的跨层流量", "两级流量 / 同步频率 / 边缘负载", COLORS["violet"], COLORS["violet_fill"]),
    ]
    for y, lever, methods, changed, metric, color, fill in rows:
        s.append(rect(70, y, 300, 115, fill, color, 18, 3))
        s.append(text(220, y + 45, lever, "label", color=color))
        s.append(text(220, y + 84, methods, "tiny", color=COLORS["ink"]))
        s.append(line(370, y + 58, 485, y + 58, color, 4, True))
        s.append(rect(485, y, 540, 115, "#FFFFFF", color, 18, 2))
        s.append(text(755, y + 69, changed, "body", color=COLORS["ink"]))
        s.append(line(1025, y + 58, 1140, y + 58, color, 4, True))
        s.append(rect(1140, y, 390, 115, "#FFFFFF", color, 18, 2))
        s.append(text(1335, y + 69, metric, "small", color=COLORS["ink"]))
    s.append(rect(285, 850, 1030, 38, COLORS["gray_fill"], "#B5BEC5", 18, 1))
    s.append(text(800, 878, "横向比较必须在相同目标精度和系统假设下核算总成本，五类方法可组合但不可直接按单一百分比排序。", "small", color=COLORS["muted"]))
    return "".join(s)


def figure_3() -> str:
    s = []
    s.append(rect(55, 55, 715, 780, "#FAFBFC", "#AAB5BE", 24, 2))
    s.append(rect(830, 55, 715, 780, "#FAFBFC", "#AAB5BE", 24, 2))
    s.append(text(95, 105, "A", "panel", anchor="start", color=COLORS["blue"]))
    s.append(text(412, 105, "数字正交上传：先分离传输，再求和", "panel", color=COLORS["blue"]))
    s.append(text(870, 105, "B", "panel", anchor="start", color=COLORS["red"]))
    s.append(text(1187, 105, "空中聚合：信道叠加直接形成聚合量", "panel", color=COLORS["red"]))

    ys = [190, 350, 510]
    for i, y in enumerate(ys, 1):
        s.append(phone(105, y, 0.72, COLORS["blue"]))
        lab = f"更新 g{i}" if i < 3 else "更新 gK"
        s.append(text(210, y + 45, lab, "small", anchor="start"))
        s.append(line(300, y + 35, 515, y + 35, COLORS["blue"], 4, True))
        s.append(text(405, y + 18, f"资源块 {i if i < 3 else 'K'}", "tiny", color=COLORS["blue"]))
    s.append(antenna(585, 300, 1.25, COLORS["blue"]))
    s.append(rect(515, 590, 185, 92, COLORS["blue_fill"], COLORS["blue"], 15, 2))
    s.append(multiline(608, 625, ["分别解码", "g₁, g₂, …, gK"], "small", gap=30, color=COLORS["blue"]))
    s.append(line(608, 555, 608, 588, COLORS["blue"], 3, True))
    s.append(rect(175, 700, 420, 70, "#FFFFFF", COLORS["blue"], 18, 2))
    s.append(text(385, 746, "服务器再执行数字加权求和", "body", color=COLORS["blue"]))
    s.append(line(515, 636, 470, 700, COLORS["blue"], 3, True))

    for i, y in enumerate(ys, 1):
        s.append(phone(880, y, 0.72, COLORS["red"]))
        lab = f"预处理 x{i}" if i < 3 else "预处理 xK"
        s.append(text(985, y + 45, lab, "small", anchor="start"))
        s.append(path(f"M1080,{y+35} C1160,{y+35} 1215,390 1300,390", COLORS["red"], 4, True))
    s.append(antenna(1360, 325, 1.25, COLORS["red"]))
    s.append(text(1190, 325, "同频同时间发送", "small", color=COLORS["red"]))
    s.append(rect(1185, 550, 300, 112, COLORS["red_fill"], COLORS["red"], 16, 2))
    s.append(multiline(1335, 588, ["接收叠加波形", "y = Σ hₖxₖ + n"], "small", gap=38, color=COLORS["red"]))
    s.append(line(1360, 470, 1360, 548, COLORS["red"], 3, True))
    s.append(rect(950, 700, 470, 70, "#FFFFFF", COLORS["red"], 18, 2))
    s.append(text(1185, 746, "经标定后直接估计加权聚合结果", "body", color=COLORS["red"]))
    s.append(line(1210, 662, 1185, 700, COLORS["red"], 3, True))

    s.append(pill(885, 790, 180, "同步", COLORS["orange_fill"], COLORS["orange"]))
    s.append(pill(1080, 790, 260, "信道估计 / 功率对齐", COLORS["orange_fill"], COLORS["orange"]))
    s.append(pill(1355, 790, 150, "噪声", COLORS["orange_fill"], COLORS["orange"]))
    return "".join(s)


def figure_4() -> str:
    s = []
    s.append(rect(60, 65, 1480, 705, "#FAFBFC", "#AAB5BE", 26, 2))

    s.append(rect(650, 92, 300, 125, COLORS["violet_fill"], COLORS["violet"], 22, 3))
    s.append(server(690, 112, 0.75, COLORS["violet"]))
    s.append(multiline(850, 135, ["云服务器", "周期性全局聚合"], "label", gap=42, color=COLORS["violet"]))

    edge_centers = [450, 1150]
    for idx, cx in enumerate(edge_centers, 1):
        s.append(rect(cx - 175, 330, 350, 125, COLORS["blue_fill"], COLORS["blue"], 20, 3))
        s.append(antenna(cx - 105, 342, 0.65, COLORS["blue"]))
        s.append(multiline(cx + 50, 370, [f"边缘节点 {idx}", "局部模型聚合"], "label", gap=40, color=COLORS["blue"]))
        s.append(line(cx, 330, 770 if idx == 1 else 830, 217, COLORS["violet"], 5, True, "12 8"))
    s.append(pill(610, 255, 380, "边—云：较低频同步（跨域链路）", COLORS["violet_fill"], COLORS["violet"]))

    client_groups = [(220, 450), (520, 450), (920, 1150), (1220, 1150)]
    client_xs = [160, 310, 460, 610, 860, 1010, 1160, 1310]
    for i, x in enumerate(client_xs):
        s.append(phone(x, 565, 0.7, COLORS["teal"]))
        s.append(database(x + 55, 582, 0.48, COLORS["teal"]))
        target = 450 if i < 4 else 1150
        s.append(line(x + 30, 558, target, 455, COLORS["teal"], 2.5, True))
    s.append(text(450, 710, "终端簇 A：频繁端—边更新", "body", color=COLORS["teal"]))
    s.append(text(1150, 710, "终端簇 B：频繁端—边更新", "body", color=COLORS["teal"]))
    s.append(pill(585, 475, 430, "端—边：较高频局部聚合（接入链路）", COLORS["teal_fill"], COLORS["teal"]))

    s.append(rect(80, 800, 450, 70, COLORS["teal_fill"], COLORS["teal"], 18, 2))
    s.append(text(305, 846, "收益：减少高频更新跨越远距离链路", "small", color=COLORS["teal"]))
    s.append(rect(575, 800, 450, 70, COLORS["orange_fill"], COLORS["orange"], 18, 2))
    s.append(text(800, 846, "权衡：两级聚合间隔与模型漂移", "small", color=COLORS["orange"]))
    s.append(rect(1070, 800, 450, 70, COLORS["red_fill"], COLORS["red"], 18, 2))
    s.append(text(1295, 846, "代价：边缘负载、部署与同步控制", "small", color=COLORS["red"]))
    return "".join(s)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    figures = {
        "fig01_fl_round_communication_mechanism": figure_1(),
        "fig02_optimization_lever_map": figure_2(),
        "fig03_digital_vs_aircomp": figure_3(),
        "fig04_hierarchical_two_timescale": figure_4(),
    }
    for name, body in figures.items():
        path_out = write_svg(name, body)
        print(path_out)


if __name__ == "__main__":
    main()
