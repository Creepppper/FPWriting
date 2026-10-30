# 上游双栏模板许可记录

- 上游仓库：`EmpyreanHYR/Self-made-two-column-Latex-template-for-Chinese-papers`
- 仓库地址：<https://github.com/EmpyreanHYR/Self-made-two-column-Latex-template-for-Chinese-papers>
- 核查日期：2026-10-30
- 核查分支：`main`
- 核查提交：`b8b4c471af8116a778a6233b55b6e5ec3c1e287f`
- 许可证：MIT License
- 版权声明：`Copyright (c) 2025 HuangYaorong`
- 完整许可文本：`licenses/upstream_template_LICENSE.txt`

## 本项目的复用范围

本项目复用的是上游模板的版式方案：A4 双栏、首页顶部通栏中英文题录与摘要、正文模块化、中文图表名称和交叉引用。没有复制上游示例正文、示例参考文献或示例图片。

本项目对实现作了实质性调整：

1. 使用 `ctexart + XeLaTeX`，加入 Times New Roman、SimSun/SimHei、Fandol 和 TeX Gyre 的字体后备；
2. 使用 `biblatex-gb7714-2015 + biber` 生成 GB/T 7714—2015 顺序编码参考文献，不使用手工 `thebibliography`；
3. 将导言、正文、图和表拆分到独立文件；
4. 使用原生数学环境、`cleveref`、`booktabs`、`tabularx` 和 TikZ；
5. 删除上游示例正文及其与本论文无关的算法宏包配置。

根据 MIT License，随本项目保留上游版权声明和许可文本。
