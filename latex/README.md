# LaTeX 工程说明

本目录用于重构课程综述论文《无线边缘网络中联邦学习通信效率优化方法研究综述》。当前已完成阶段 7 终审，包括第 1—6 节、中英文摘要与关键词、两幅原创机理图、一张综合比较表、43 篇参考文献及最终 PDF。

## 目录

```text
latex/
  main.tex
  preamble.tex
  references.bib
  sections/
  figures/reused/
  figures/tikz/
  tables/
  licenses/
  output/
```

`figures/reused/` 目前为空。阶段 5B 没有导入外部图片；正式采用的 AirComp 对比图和分层聚合图均为 `figures/tikz/` 中的原创黑白矢量图。
`output/` 保留版式样张、阶段稿、最终 PDF、终审记录和构建说明；编译辅助文件和目视检查预览由 `.gitignore` 排除。

## 编译环境

- 引擎：XeLaTeX
- 文献后端：Biber
- 文献样式：`biblatex-gb7714-2015` 的 `gb7714-2015`
- 页面：A4，四边 2 cm，栏间距 0.8 cm
- 字体：英文优先 Times New Roman，后备 TeX Gyre Termes；中文正文优先 SimSun，后备 FandolSong；中文标题优先 SimHei，后备 FandolHei；作者与单位信息优先 FandolFang

## 编译命令

在 `latex/` 目录执行：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error \
  -jobname=无线边缘网络中联邦学习通信效率优化方法研究综述_final \
  -outdir=output main.tex
```

清理辅助文件但保留 PDF：

```bash
latexmk -c \
  -jobname=无线边缘网络中联邦学习通信效率优化方法研究综述_final \
  -outdir=output main.tex
```

## 上游模板

版式以 EmpyreanHYR 的双栏中文论文模板为基础重新实现。上游采用 MIT License；版本、复用范围和完整许可文本见：

- `licenses/upstream_template.md`
- `licenses/upstream_template_LICENSE.txt`

## 当前阶段边界

- `sections/introduction.tex` 与 `sections/system_model.tex` 是阶段 4 新写正文。
- `sections/methods_5a.tex` 是阶段 5A 新写的第 3 章导语及第 3.1—3.3 节，含原生压缩指标公式。
- `sections/methods_5b.tex` 是阶段 5B 新写的第 3.4—3.5 节，含 AirComp 接收/误差公式、两级聚合公式及两幅原创 TikZ 机理图。
- `sections/discussion_conclusion.tex` 是阶段 6 新写的第 4—6 节；`tables/method_comparison.tex` 是横向比较五类方法的综合表。
- `sections/layout_sample_body.tex` 和 `figures/tikz/layout_placeholder.tex` 仅保留为阶段 3 版式测试材料，当前主文档不再载入。
- `main.tex` 已写入内容对应的中英文摘要和关键词；`references.bib` 收录并仅收录全文实际引用的 43 篇已核验文献。

## 阶段 7 最终状态

- 最终 PDF：`output/无线边缘网络中联邦学习通信效率优化方法研究综述_final.pdf`
- 终审记录：`output/final_audit.md`
- 可复现构建说明：`output/build_instructions.md`
- 最终统计：正文 5269 个汉字，参考文献 43 篇（中文 17、英文 26），原创 TikZ 图 2 幅、比较表 1 张、原生公式 8 组。
- 最终 PDF 已完成两轮强制完整构建和逐页检查；输出目录中的辅助文件与临时预览已清理。
- 提交前仍需在 `main.tex` 填写真实的中英文作者和单位信息并重新编译。
