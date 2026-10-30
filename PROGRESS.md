# 项目进度与断点

> 本文件是跨会话续作入口。新会话须先阅读 `AGENTS.md`，再读取本文件，并仅从“下一步”继续。

## 项目状态

- 项目：无线边缘网络中联邦学习通信效率优化方法研究综述
- 当前阶段：LaTeX 重构阶段 7——全文事实、引用、版权和版式终审
- 当前状态：待用户确认
- 最近更新：2026-10-31（Asia/Shanghai）
- 本轮范围：完成全文事实、引用、版权、公式、写作和版式终审，生成最终 PDF、审计记录和构建说明；不覆盖 v1.2 DOCX，不提交 Git

## 阶段清单

- [x] 阶段 0：建立项目目录
- [x] 阶段 0：将长期项目规则写入 `AGENTS.md`
- [x] 阶段 0：整理课程要求和验收标准
- [x] 阶段 0：建立跨会话断点续作机制
- [x] 阶段 1：范围界定、检索设计与候选文献库
- [x] 阶段 2：最终文献筛选与元数据核验（43篇纳入；17篇排除或暂不纳入）
- [x] 阶段 3：基于当前证据矩阵建立分类框架与详细提纲（后续英文库完成后需刷新引文）
- [x] 阶段 4：正文与中英文摘要写作（分节草稿完成，待后续合并复核）
  - [x] 4A：中英文题目、引言与第 2 章
  - [x] 4B：第 3.1～3.2 节
  - [x] 4C：第 3.3～3.5 节
  - [x] 4D：第 4～6 章及中英文摘要
- [x] 阶段 5：引用、事实、图表与格式完整性核验
- [x] 阶段 6：修订、最终复核、课程格式DOCX与Markdown交付
- [x] LaTeX 重构阶段 0—6：诊断、结构学习、内容蓝图、工程搭建、全文重写与初稿编译
- [x] LaTeX 重构阶段 7：事实、引用、版权、公式、写作和版式终审

## 阶段 0 产物

- `AGENTS.md`：项目长期规则、诚信边界、目录职责和续作协议。
- `requirements/course_requirements.md`：课程要求、量化指标和阶段/最终验收标准。
- `PROGRESS.md`：当前状态、产物、未决项及下一步。
- `literature/`：阶段 0 时仅建立目录；阶段 1 产物见下文。
- `outline/`：已建立，当前为空。
- `draft/`：已建立，当前为空。
- `figures/`：已建立，当前为空。
- `final/`：已建立，当前为空。

## 阶段 0 验收

- [x] 题目、论文性质和禁止事项已记录。
- [x] 字数、参考文献数量与中英文文献配比已记录。
- [x] 摘要、关键词、正文结构、图表与引文格式要求已记录。
- [x] 文献元数据核验和“待核验不得入最终参考文献”规则已记录。
- [x] 已定义新会话读取顺序、状态用语、版本约定和阶段关口。
- [x] 未开展大规模检索。
- [x] 未生成论文正文。

## 已确认决定

- 论文按本科课程文献综述定位，不包装为原创研究。
- 中文正文按 4500～5500 字验收，目标约 5000 字；摘要和参考文献不计入。
- 最终参考文献至少 40 篇，建议 42～48 篇；中文学术文献目标 12～18 篇。
- 时间覆盖必须兼顾经典早期文献与 2022—2026 年文献。
- 引文采用顺序编码制，参考文献标注文献类型。
- 图表以原创归纳图和比较表为主。

## 未决事项

以下事项仍待用户确认或根据课程模板补充，后续阶段不得擅自决定：

- 学校或教师是否提供专用排版模板、封面、页边距、字体和行距要求。
- 顺序编码制所依据的具体标准（如是否严格采用 GB/T 7714—2015）。
- 可用数据库及访问条件，以及是否需要保存完整检索日志。
- 综述的研究问题、主题边界和“通信效率”评价维度的最终定义。
- 最终交付格式（Markdown、DOCX、PDF 或其组合）。

## 阶段 1 进度日志

- [x] 已建立中英文概念组、布尔检索式、数据库适配、候选进入规则、去重规则和核验状态定义：`literature/search_strategy.md`。
- [x] 里程碑 1：候选文献 15/60（中文 15，英文 0）；已写入 `literature/candidates.csv`。
- [x] 里程碑 2：候选文献 30/60（中文 20，英文 10）；中文候选最低数量已达到。
- [x] 里程碑 3：候选文献 45/60（中文 20，英文 25）；已覆盖经典基线、调度、分层聚合和压缩方向。
- [x] 里程碑 4：候选文献 60/60（中文 20，英文 40）；达到候选数量后停止扩展。
- [x] 候选文献：60/60（达到 60～80 区间；中文 20 篇）。

## 阶段 1 产物

- `literature/search_strategy.md`：中英文概念组、综合式与专题式、数据库适配、候选进入规则、去重规则、核验状态和实际检索限制。
- `literature/candidates.csv`：60 篇候选的结构化元数据；中文 20 篇、英文 40 篇。
- `literature/download_requests.md`：37 篇本轮未取得完整正文的合法获取请求。

## 阶段 1 验收

- [x] 候选总数 60，位于 60～80 篇目标区间。
- [x] 中文候选 20 篇，达到“至少 20 篇”要求；英文候选 40 篇。
- [x] 2022—2026 年候选 36 篇；截至 2021 年的经典/早期候选 24 篇。
- [x] 文献类型分布：期刊 46、会议 12、学位论文 1、预印本 1；同行评审期刊和会议为主体。
- [x] 已覆盖本地更新/通信频率、模型与梯度压缩、量化/稀疏化、客户端选择/资源分配、空中计算/模拟聚合、分层/边缘辅助联邦学习。
- [x] CSV 必填字段无缺失；ID、题名和 DOI 无重复。
- [x] 37 条全文受限记录与 `download_requests.md` 一一对应。
- [x] 未根据搜索摘要编造研究结论；主题标签仅用于候选分类。
- [x] 未筛选最终参考文献，未撰写论文正文。

## 阶段 1 限制与待核验项

- Consensus 和 Scite 在本环境中未连接，因此本轮未使用。
- Web of Science、知网主站高级检索及部分万方/出版社全文需要机构权限；检索式已保存以便复跑。
- `E002` 目前仅记录预印本版本，状态为“待核验（预印本）”，不得直接进入最终参考文献。
- 若干中文期刊页面未显示 DOI，但已有期刊官网稳定 URL；阶段 2 应继续补核卷期页码和 DOI。
- 元数据核验不代表全文内容核验；37 篇全文受限候选需按下载清单获取后再评估。

## 阶段 2 批次日志

### 批次 1（2026-10-11）

- [x] 已按候选编号连续处理 C001—C020、E001—E002，共 22 篇；未重复处理既有记录。
- [x] 已逐篇记录完整出版元数据、研究场景与无线假设、优化类别、核心方法、通信指标、主要结论、优点、限制、适用条件、章节用途、证据层级及核验状态：`literature/evidence_matrix.csv`。
- [x] 本批暂定纳入 18 篇：中文 17 篇、英文 1 篇；记录于 `literature/final_library.csv`。这里的“暂定纳入”是阶段 2 的批次判定，不代表 42～48 篇最终库已经完成。
- [x] 本批排除 4 篇：C014（通信指标与无线场景不足且摘要结果表述不一致）、C015（纵向联邦学习偏离主题）、C020（学位论文且未获全文）、E002（仅预印本，优先正式同行评审来源）；记录于 `literature/rejected_library.csv`。
- [x] C009、C016 为正式期刊且主题直接，但本轮仅取得期刊官网摘要；已限制为“摘要层面已核验”，不得引用摘要未报告的实验数字或细节。
- [x] 已检查本批版本关系：E001 使用 AISTATS/PMLR 正式会议版本；E002 未发现正式发表版本，但因预印本属性未进入暂定最终库。
- [x] 未撰写论文正文。

### 当前累计（阶段 2）

- 已处理：22/60 篇。
- 暂定纳入：18 篇（中文 17、英文 1；经典/早期 3 篇，2022—2026 年 15 篇）。
- 排除：4 篇（中文 3、英文 1）。
- 待处理：38 篇（E003—E040）。
- 类别覆盖（暂定纳入）：本地更新/通信频率、异步聚合、模型与梯度压缩、量化/稀疏化、客户端选择/资源分配、空中计算/模拟聚合、分层/边缘辅助联邦学习均已有至少 1 篇代表文献。
- 配额提示：中文暂定纳入已达 17 篇，接近 12～18 篇目标上限；下一批应以高质量英文正式论文为主，并允许后续按质量替换而非继续堆叠中文文献。

## 阶段 3 进度日志

### 分类框架与三级大纲（2026-10-11）

- [x] 已采用主题型文献综述结构，形成“时间—参与者—载荷—信道—拓扑”五维分类：通信频率、客户端与无线资源、模型/梯度压缩、空中计算、分层/边缘辅助联邦学习。
- [x] 已建立混合方法的交叉归类规则，避免将同一研究在多个章节重复逐篇介绍。
- [x] 已形成六章三级大纲，并为每个二级标题记录核心问题、比较维度、拟得出的结论及拟引用文献：`outline/paper_outline.md`。
- [x] 正文字数预算合计 5000 字：引言 550、基础与通信开销 850、优化方法 2250、方法比较 600、问题与趋势 500、结论 250。
- [x] 已为当前 18 篇暂定纳入文献建立“暂定顺序号/稳定 ID”映射；所有文献至少分配到一个正文小节，引言仅安排 4 篇框架型文献。
- [x] 已规划两幅原创图：无线边缘 FL 架构与通信瓶颈、通信效率优化方法分类框架。
- [x] 已规划一张方法比较表，字段包括原理、通信指标、优点、局限、适用场景和代表文献。
- [x] 已将隐私、安全、激励和一般资源优化限定为通信效率的约束或附加成本，不独立扩展为主题主线。
- [x] 未撰写完整正文。

### 阶段 3 限制与刷新条件

- 阶段 2 仍只处理 22/60 篇，当前最终库仅 18 篇，尚未达到 42～48 篇目标；本大纲的证据分布和引文编号为暂定版本。
- `[9/C009]` 与 `[14/C016]` 仅有摘要层面证据，大纲已限制其用途，不得在正文补写摘要未提供的实验细节或数值。
- AirComp/模拟聚合目前只有 `[1/C001]` 一篇暂定文献，是最明显的证据缺口；后续英文核验应补入 3～5 篇正式原始研究。
- 完成 E003—E040 筛选后，须回到 `outline/paper_outline.md` 更新引用编号、英文证据分布和各类别代表文献，但不必改变已经稳定的五维主框架，除非新证据显示分类边界不适用。

## 阶段 4 进度日志

### 4A：中英文题目、引言与第 2 章（2026-10-11）

- [x] 已写入中英文题目、引言、第 2 章“无线边缘网络中的联邦学习与通信开销”：`draft/4A.md`。
- [x] 正文净字符约 1410 字（不含题目、标题、引文编号和空白；汉字总量 1469），位于本轮 1200～1500 字目标内。
- [x] 各正文段落以中心句开头，并按问题、代表性方法、比较和局限组织；未撰写第 3～6 章或摘要。
- [x] 所有定量表述均来自 `literature/evidence_matrix.csv`：FedAvg 通信轮数、分层协同训练指标、异步通信比例、稀疏三值压缩以及 1-bit 压缩感知结果。
- [x] AirComp 当前只有单篇中文全文证据，已在正文标记 `[待补证据]`，未补造定量结论。
- [x] 缩略语检查已通过；未发现正文缩略语首现未定义问题。
- [x] 本轮引文采用首次出现顺序编号，并逐项确认对应文献均存在于 `literature/final_library.csv`；无孤立正文引文。

### 4A 引文编号映射

| 本轮编号 | 稳定 ID | 文献简称 | 库内状态 |
|---|---|---|---|
| [1] | E001 | McMahan 等：FedAvg | 本批暂定纳入（全文） |
| [2] | C003 | 面向边缘智能的联邦学习综述 | 本批暂定纳入（全文） |
| [3] | C013 | 联邦学习的高效性研究综述 | 本批暂定纳入（全文） |
| [4] | C008 | 跨设备联邦学习中的客户端选择算法 | 本批暂定纳入（全文） |
| [5] | C018 | 异构物联网下资源高效的分层协同联邦学习方法 | 本批暂定纳入（全文） |
| [6] | C019 | 面向云边端系统的分层异构联邦学习方法 | 本批暂定纳入（全文） |
| [7] | C002 | 面向边缘计算的高效异步联邦学习机制 | 本批暂定纳入（全文） |
| [8] | C001 | 通信计算一体化设计 | 本批暂定纳入（全文） |
| [9] | C004 | 提升联邦学习通信效率的梯度压缩算法 | 本批暂定纳入（全文） |
| [10] | C006 | 基于 1-bit 压缩感知的高效无线联邦学习算法 | 本批暂定纳入（全文） |

### 4B：第 3.1～3.2 节（2026-10-11）

- [x] 已完成“3.1 本地更新与通信频率控制”和“3.2 客户端选择、调度与无线资源配置”：`draft/4B.md`。
- [x] 正文净字符约 1085 字（不含标题、引文编号和空白；汉字总量 1111），位于本轮 1000～1300 字目标内。
- [x] 两节均围绕问题、代表性机制、方法比较和适用局限组织，未提前撰写第 3.3 节及后续内容。
- [x] 定量表述均来自证据矩阵：异步通信比例及精度变化、自适应触发次数及准确率、单轮通信量比例。
- [x] 动态无线环境下频率控制的收敛边界，以及边缘关联和无人机调度的跨方案定量比较，均已标记 `[待补证据]`。
- [x] 缩略语检查通过；本轮所有引用均已逐项匹配 `literature/final_library.csv`，无孤立正文引文。

### 4B 新增引文编号映射

| 本轮编号 | 稳定 ID | 文献简称 | 证据范围 |
|---|---|---|---|
| [11] | C005 | 基于自适应梯度压缩的高效联邦学习通信机制研究 | 全文 |
| [12] | C007 | 面向通信成本优化的联邦学习算法 | 全文 |
| [13] | C011 | 边缘计算网络中区块链赋能的异步联邦学习算法 | 全文 |
| [14] | C009 | 基于分层博弈的边缘关联和资源分配 | 摘要；仅作定性引用 |
| [15] | C012 | 边缘辅助的自适应稀疏联邦学习优化算法 | 全文 |
| [16] | C016 | 无人机辅助联邦学习安全传输能效优化 | 摘要；仅作定性引用 |
| [17] | C010 | 基于主从博弈的分层联邦学习激励机制研究 | 全文 |

### 4C：第 3.3～3.5 节（2026-10-11）

- [x] 已完成“3.3 模型和梯度压缩”“3.4 空中计算与模拟聚合”“3.5 分层式和边缘辅助联邦学习”：`draft/4C.md`。
- [x] 正文净字符约 1410 字（不含标题、引文编号和空白；汉字总量 1471），位于本轮 1400～1700 字目标内。
- [x] 三节均按问题、代表性机制、方法比较和适用局限组织，未提前撰写第 4 章及后续内容。
- [x] 定量表述均来自证据矩阵：一比特压缩感知通信量与能耗、稀疏三值压缩倍数与轮数、模型异构准确率、分层协同训练指标。
- [x] 空中计算的跨方案定量优势及动态分层网络的两级流量比例均因证据不足标记 `[待补证据]`。
- [x] 缩略语检查通过；合并检查 4A—4C 的引文首次出现顺序为 [1]～[18]，本轮所有引用均存在于 `literature/final_library.csv`。

### 4C 新增引文编号映射

| 本轮编号 | 稳定 ID | 文献简称 | 证据范围 |
|---|---|---|---|
| [18] | C017 | 基于秘密共享和压缩感知的通信高效联邦学习 | 全文；仅将安全作为通信附加成本讨论 |

### 4D：第 4～6 章及中英文摘要（2026-10-11）

- [x] 已完成第 4 章“不同优化方法的比较与适用场景”、第 5 章“现有问题与发展趋势”、第 6 章“结论”及中英文摘要：`draft/4D.md`。
- [x] 第 4～6 章正文汉字总量 1209，位于本轮 1000～1300 字目标内；摘要按课程规则不计入正文。
- [x] 中文摘要 169 字，接近“约 150 字”要求；英文摘要 150 词；中英文关键词各 5 个。
- [x] 第 4 章按统一指标比较五类方法并给出场景匹配，第 5 章归纳证据限制和趋势，第 6 章未引入新数据或新方法。
- [x] 组合策略的跨实验定量排名和真实平台统一成本报告因证据不足标记 `[待补证据]`。
- [x] 本轮无新增引文编号，全部复用 [2]～[18] 中的已建映射；所有引用均存在于 `literature/final_library.csv`。
- [x] 4A～4D 合并后的引文首次出现顺序连续为 [1]～[18]；正文、中文摘要和英文摘要缩略语检查均通过。
- [x] 4A～4D 正文累计约 5114 字，位于课程要求的 4500～5500 字范围内；最终合并时仍须按统一口径重新计数。

### 阶段 4 历史限制的处理结果

- 18篇暂定文献不足的问题已解决：最终库现为43篇，其中中文17篇、英文26篇。
- 大纲和分节草稿中的旧编号已由最终稿统一重排为[1]～[43]，旧映射仅保留作历史记录。
- AirComp证据已补入E014、E015、E031、E032、E033等正式英文研究；正文仍避免无统一条件的跨方案数字比较。
- C009与C016仍只有正式摘要证据，最终稿只保留摘要直接支持的定性表述，未写入算法参数或性能数字。
- 分节草稿中的全部`[待补证据]`已通过补入正式来源或收缩论断处理，最终稿无占位符。

## 阶段 5～6：合并审校、引用核验与交付（2026-10-11）

- [x] 已合并并修订4A～4D：`final/manuscript.md`。
- [x] 正文严格口径5480个汉字，中文摘要159字，英文摘要140词，中英文关键词各5个。
- [x] 最终参考文献43篇：中文17篇、英文26篇；期刊34篇、会议9篇；2022—2026年22篇。
- [x] 已形成“时间—参与者—载荷—信道—拓扑”五类方法框架，并完成两幅原创归纳图和一张方法比较表。
- [x] 正文引文覆盖[1]～[43]，首次出现顺序连续；无正文孤立引文，无未被正文引用的参考文献。
- [x] 已逐项核验作者、题名、年份、来源、卷期页码和DOI或稳定URL；E008的来源/DOI和E013的作者字段已纠正。
- [x] 已复核8组具体数字，全部可回到全文或期刊官网；没有根据二手摘要补造性能结论。
- [x] 已生成逐项审计报告：`final/citation_audit.md`。
- [x] C006的DOI解析异常、C002目标站错误以及C009/C016仅有摘要证据等限制已在审计报告显式记录。
- [x] 17篇未进入最终稿的候选已在审计报告列入排除或待处理清单，不计入最终参考文献。

## 最终产物

1. `final/manuscript.md`：合并、审校并完成顺序编码的Markdown论文稿。
2. `final/citation_audit.md`：完整性、学术结构、引文双向覆盖、元数据、数字证据和待处理项审计。
3. `literature/final_library.csv`：43篇最终使用文献及证据范围。
4. `literature/candidates.csv`：已纠正E008和E013元数据的60篇候选库。
5. `final/无线边缘网络中联邦学习通信效率优化方法研究综述.docx`：按课程字号、字体、图表和自动编号要求生成的最终排版稿。
6. `final/format_checklist.md`：课程格式逐项验收、自动字段检查、渲染检查及人工复核提醒。
7. `final/无线边缘网络中联邦学习通信效率优化方法研究综述_图示优化版.docx`：用四幅机制/对照图替换原两幅树状图，并补充正文解释的版本。
8. `final/manuscript_figure_revision.md`：与图示优化版DOCX对应的可追溯Markdown源稿。
9. `figures/`：四幅图的SVG、高清PNG、生成脚本及来源/用途说明。

## 最终排版日志（2026-10-11）

- [x] 页面设置为A4纵向。
- [x] 中文标题、作者/单位、摘要、关键词、两级标题、正文、图注和参考文献均建立对应字号与字体样式。
- [x] 英文题目、摘要和关键词指定Times New Roman。
- [x] 两幅原创归纳图已重新绘制并嵌入DOCX，宽15.5 cm；比较表完整显示。
- [x] 章节采用两级自动编号；图、表、参考文献采用SEQ字段；正文引文和图表引用采用REF字段。
- [x] DOCX压缩结构测试通过；LibreOffice独立打开并导出15页A4临时PDF，抽查首页、图表、结论及参考文献无越界或截断。
- [x] 本机缺少仿宋和黑体，DOCX仍写入目标字体名称；需在安装相应字体的Word环境中人工复核。
- [x] 项目未提供作者和单位信息，DOCX保留可填写占位符，未虚构个人信息。

## 图示专项优化日志（2026-10-30）

- [x] 学习本地课程示例 `docs/2020_航空兵器_锑化物红外探测器国内外发展综述.pdf` 与 `docs/2015_Nature_Deep Learning.pdf` 的图文组织方式：图前提出问题、图中呈现机制、图后解释结论。
- [x] 检查移动边缘联邦学习、空中聚合和分层联邦学习的代表性论文图示，采用系统流程图、机制对照图和分层消息交换图的表达方式；未复制论文原图。
- [x] 新增四幅原创归纳图：一轮通信流程与开销形成机制、五类优化杠杆作用图、数字正交上传与空中聚合对比、分层联邦学习双时间尺度图。
- [x] 每幅图均保存SVG可编辑源文件和高清PNG，并在 `figures/figure_sources.md` 记录用途、支撑文献和证据边界；生成脚本为 `figures/generate_figures.py`。
- [x] 已在第2.1节、第3章开头、第3.4节和第3.5节补写图前/图后说明，明确每幅图帮助说明的机制和局限。
- [x] 图示优化版正文汉字数5297、严格词元数5465，仍位于4500～5500字验收范围；43篇参考文献全部在正文出现，正文引文均可回到参考文献表。
- [x] 新DOCX保持A4和既有课程样式，四图宽度均不超过15.5 cm；图、表、参考文献及正文引用继续使用SEQ/REF字段。
- [x] DOCX后检通过：无空白页、图片越界或比例失真；LibreOffice独立渲染为14页A4，四幅图与题注均完整显示。
- [x] 原始 `final/无线边缘网络中联邦学习通信效率优化方法研究综述.docx` 未覆盖，便于对照和回退。

## 下一步

- 待用户确认图示优化方向后，再单独进行结构和论证链优化；不在本轮继续改写其他章节。

## 同主题综述阅读包（2026-10-30）

- [x] 已检索移动边缘联邦学习、通信效率、无线资源、空中聚合、分层拓扑和能效等方向的代表性综述。
- [x] 已将12篇合法开放全文保存到 `assets/surveys/`，包括2篇中文核心综述及10篇英文/双语开放版本，总计约24 MB；全部通过PDF结构读取检查。
- [x] 已生成 `assets/surveys/README.md`，逐篇记录正式来源、版本状态、相关度、建议阅读重点和使用边界。
- [x] 对3篇非开放获取正式综述及2篇仅HTML可访问的中文综述，只保存DOI或期刊入口，没有使用非授权镜像。
- [x] 已标出优先阅读顺序，并说明可借鉴的是分类、论证、图表和比较方法，不得复制原文或原图。

## v1.2 结构、图示与公式修订（2026-10-30）

- [x] 已逐篇阅读 `assets/surveys/` 中 12 篇综述的全文提取文本，并将结构、公式、图示和横向比较写法整理为 `assets/surveys/structure_notes_v1.2.md`。
- [x] 已将正文重组为“系统与指标—五类优化机制—统一比较—局限与趋势”的论证链，避免按文献或年份逐篇罗列。
- [x] 已加入 7 组有文献依据的公式：全局目标、局部更新与 FedAvg、累计通信量、上行时延、压缩比、空中聚合和两级分层聚合。
- [x] 已生成 4 幅黑白专业线稿：联邦学习一轮流程、五类方法作用位置、数字上传与空中聚合、端—边—云双时间尺度聚合。
- [x] 每幅图均采用“图前说明问题—图中呈现机制—图后解释结论与限制”的写法；来源与证据边界记录于 `figures/figure_sources_v1.2.md`。
- [x] 参考文献仍为已核验的 43 篇（中文 17 篇）；按 v1.2 首次出现顺序重排为连续 `[1]`—`[43]`，没有未引用条目或孤立引文。
- [x] 正文汉字数 4829，位于 4500～5500 范围；未新增未经核验的事实、实验或参考文献。
- [x] 已生成 `final/无线边缘网络中联邦学习通信效率优化方法研究综述_v1.2.docx`；旧版和图示优化版均保留。
- [x] DOCX 使用 A4、课程字体字号、自动章节/图/表/式/参考文献编号及交叉引用；表格和图示统一为黑白灰。
- [x] 后检 9/9 通过；LibreOffice 独立渲染为 15 页 A4，无空白页、图片越界或比例失真。
- [x] 已生成 `final/citation_audit_v1.2.md`、`final/format_checklist_v1.2.md` 和 `final/reference_number_map_v1.2.json`。

## 继续工作所需文件（更新）

1. `AGENTS.md`
2. `PROGRESS.md`
3. `requirements/course_requirements.md`
4. `final/manuscript.md`
5. `final/citation_audit.md`
6. `final/无线边缘网络中联邦学习通信效率优化方法研究综述.docx`
7. `final/format_checklist.md`
8. `literature/final_library.csv`
9. `literature/evidence_matrix.csv`
10. `outline/paper_outline.md`
11. `final/manuscript_v1.2.md`
12. `final/citation_audit_v1.2.md`
13. `final/format_checklist_v1.2.md`
14. `figures/figure_sources_v1.2.md`

## LaTeX 重构阶段 0：现有论文诊断与重构计划（2026-10-30）

- [x] 已检查 v1.2 DOCX、对应 Markdown、图、公式、生成脚本、格式清单、引用审计、最终文献库和证据矩阵。
- [x] 已阅读 `assets/surveys/` 中 12 篇综述的摘要、引言、章节结构、分类图、主要比较表和结论，并建立逐部分学习映射。
- [x] 已完成 DOCX OOXML 审计：6 章、11 个二级小节、4 幅正文图、1 张实质性比较表、7 组公式；7 组公式全部是 PNG，原生数学节点为 0。
- [x] 已确认 v1.2 正文 4829 个汉字，中文摘要 159 个汉字；43 篇参考文献中中文 17 篇、英文 26 篇，2022—2026 年 22 篇。
- [x] 已确认图、表、公式和参考文献使用 `SEQ` 自动编号，正文使用 `REF` 交叉引用；43 篇参考文献均被正文引用，正文无孤立编号。
- [x] 已从选题边界、分类逻辑、文献综合、公式、图片、比较表、章节衔接、摘要与结论、版式与引用九方面完成诊断。
- [x] 已记录式 (2)、(4)、(6)、(7) 的符号或物理条件问题，以及广播、压缩元数据、控制信令和两级流量的统计口径问题。
- [x] 已形成目标章节、约 5000 字预算、旧稿迁移关系、保留/重写/删减原则、图表与公式计划及风险清单：`latex/REBUILD_PLAN.md`。
- [x] 已核查指定双栏模板采用 MIT License，版权声明为 `Copyright (c) 2025 HuangYaorong`；后续复用时须保留许可证声明。
- [x] 本阶段未改写正文、未复制图片、未生成 `main.tex` 或完整 LaTeX 论文。

### 本阶段新增或修改文件

1. `latex/REBUILD_PLAN.md`：阶段 0 诊断、示例学习映射、章节迁移和重构风险。
2. `PROGRESS.md`：更新当前阶段、验收结果、断点和下一步。

### 编译、引用与版权状态

- 编译：本阶段按要求未创建 LaTeX 主文档，因此没有可编译 PDF；编译检查不适用，未误报为通过。
- 引用：v1.2 的编号完整性合格，但参考文献为手工排版，尚未转换为 GB/T 7714—2015 的 BibTeX/Biber 工作流；少数旧审计风险需在建立 `references.bib` 时重新核验。
- 版权：当前四图为项目原创归纳图；后续如考虑复用示例图片，必须逐图检查许可证和第三方声明。Kunjumon 等的 CC BY-NC-ND 图片不得裁剪、翻译、改色或改绘。

## 继续工作所需文件（LaTeX 重构）

1. `AGENTS.md`
2. `PROGRESS.md`
3. `latex/REBUILD_PLAN.md`
4. `assets/surveys/README.md`
5. `assets/surveys/structure_notes_v1.2.md`
6. `final/manuscript_v1.2.md`
7. `final/citation_audit_v1.2.md`
8. `figures/figure_sources_v1.2.md`
9. `literature/final_library.csv`
10. `literature/evidence_matrix.csv`

## LaTeX 重构阶段 1：示例综述结构学习与图片复用审查（2026-10-30）

- [x] 已逐篇检查 `assets/surveys/` 中 12 篇综述的范围、分类依据、章节论证关系、分类图、系统模型图、方法框架图、主要比较表和结论。
- [x] 已建立 `latex/SURVEY_LEARNING_MATRIX.md`，每篇均记录题目年份、范围、分类、章节组织、值得学习的图表、写作方式及不适用部分。
- [x] 已核查各 PDF 的版权页或许可声明：2 篇 MDPI 论文为 CC BY 4.0，Kunjumon 等为 CC BY-NC-ND 4.0，Wu 等为 ACM 版权及有限课堂复制许可，其余本地 PDF 未载明可支持图片复用的开放许可。
- [x] 已建立 `latex/licenses/figure_rights.md`，对 22 幅候选图逐项记录文件、图号页码、用途、许可、第三方声明、直接使用/修改权限、建议方式、中文图注和对应文献。
- [x] 已优先审查 Sensors 2023 Figure 3 和 Figure 4：两图图注均未标第三方来源并受 CC BY 4.0 覆盖；Figure 3 误写“客户端上传本地数据”，不建议原样使用；Figure 4 信息量不足，无需使用。
- [x] 已核实 Applied Sciences 2022 Figure 2、Figure 6、Figure 7 分别明确指向参考文献[8]、[55]、[48]，不得借该综述的 CC BY 许可直接复用。
- [x] 已核实 Kunjumon 2026 Fig. 8/9 在未见单独第三方 credit line 的情况下可按 CC BY-NC-ND 非商业原样使用，但不能裁剪、翻译、改色或改绘；因双栏可读性和主题偏移，不建议直接采用。
- [x] 已提出控制在 2—4 幅图的方案：系统消息与成本图、方法分类框架、数字上传与 AirComp 对比、可选分层聚合图；均建议用 TikZ 原创绘制。
- [x] 建议直接复用图片数量为 0；这是学术适用性判断，不是否认 Sensors/Applied Sciences 部分原创图的 CC BY 权利。
- [x] 本阶段未复制图片到 `latex/`，未修改正文，未创建 `main.tex`。

### 本阶段新增或修改文件

1. `latex/SURVEY_LEARNING_MATRIX.md`
2. `latex/licenses/figure_rights.md`
3. `PROGRESS.md`

### 编译、引用与版权状态

- 编译：当前仍没有 LaTeX 主文档，本阶段无可编译 PDF；编译检查不适用。
- 引用：如后续直接复用或明确改编图片，图片来源论文必须加入 `references.bib`，并由首次引用顺序自动编号。
- 版权：对无明确开放许可、ACM/IEEE 默认版权或第三方转引图片，一律保持“不直接复用”；后续不得绕过本台账直接导入图片。

## 继续工作所需文件（阶段 1 后）

1. `AGENTS.md`
2. `PROGRESS.md`
3. `latex/REBUILD_PLAN.md`
4. `latex/SURVEY_LEARNING_MATRIX.md`
5. `latex/licenses/figure_rights.md`
6. `assets/surveys/README.md`
7. `assets/surveys/structure_notes_v1.2.md`
8. `literature/final_library.csv`
9. `literature/evidence_matrix.csv`

## LaTeX 重构阶段 2：详细大纲、证据地图与图表公式规划（2026-10-30）

- [x] 已建立 `latex/CONTENT_BLUEPRINT.md`，不沿用 v1.2 的段落顺序，改以“被直接改变的通信成本分量 + 系统作用层次”为双重分类依据。
- [x] 已确定六章结构及三级论证单元：引言；通信模型与指标；客户端/频率、无线资源、压缩、AirComp、分层拓扑五类方法；横向比较；问题与趋势；结论。
- [x] 正文预算精确合计 5000 字：引言 520、第 2 章 830、第 3 章 2350、第 4 章 620、第 5 章 450、第 6 章 230；摘要和参考文献不计入。
- [x] 每节均已记录中心问题、拟得判断、必须引用的核心文献、可用中文文献、图表公式位置及相邻章节过渡。
- [x] 已为 43 篇最终库文献逐条分配主用章节、证据角色和使用边界；继续使用稳定 ID，正式顺序编号留待 BibTeX/Biber 按首次出现生成。
- [x] 已限制 `C009`、`C016` 为摘要支持的定性证据；未把摘要外数字或结论写入蓝图。
- [x] 已规划 7 组 LaTeX 原生公式：全局经验风险、本地 SGD/FedAvg、累计通信量、无线速率/时延/能耗、有效压缩率/稀疏率、AirComp 信号模型、两级分层聚合；同时记录了符号和统计口径修正要求。
- [x] 已规划 4 幅原创 TikZ 学术图：系统消息与成本位置、成本分量—系统层次分类、数字上传—AirComp 对比、端—边—云双时间尺度聚合；直接复用示例图片仍为 0 幅。
- [x] 已规划 2 张通栏比较表：五类方法统一比较、代表性研究的目标/假设/指标/局限；禁止用跨论文、跨基线百分比直接排名。
- [x] 已完成“通信效率”聚焦检查：隐私安全、激励和一般资源优化只作为通信约束或附加开销，不设并列主线。
- [x] 本阶段未改写完整正文、未复制图片、未创建 `main.tex`，未覆盖现有 DOCX/PDF。

### 本阶段新增或修改文件

1. `latex/CONTENT_BLUEPRINT.md`：约 5000 字内容蓝图、三级大纲、43 篇证据地图、7 组公式、4 幅图和 2 张表的规划。
2. `PROGRESS.md`：更新当前阶段、完成项、证据边界和下一步关口。

### 编译、引用与版权状态

- 编译：阶段要求只形成蓝图，当前仍未建立 `main.tex`，无可编译 PDF；编译检查不适用。
- 引用：最终库仍为 43 篇（中文 17、英文 26）；蓝图没有新增未核验文献。正式编号尚未生成，避免将大纲中的稳定 ID 误作最终序号。
- 证据缺口：`C009`、`C016` 仍只有正式摘要；进入正文阶段前如无法取得全文，只能保留定性表述。英文文献的证据范围按 `final_library.csv` 的 caveat 执行。
- 版权：图片方案全部为基于多篇来源事实关系的原创 TikZ，不复制权利不明、第三方转引或禁止修改的图片；后续绘图时仍须更新 `latex/licenses/figure_rights.md` 的最终图注和本地文件名。

## 继续工作所需文件（阶段 2 后）

1. `AGENTS.md`
2. `PROGRESS.md`
3. `latex/CONTENT_BLUEPRINT.md`
4. `latex/REBUILD_PLAN.md`
5. `latex/SURVEY_LEARNING_MATRIX.md`
6. `latex/licenses/figure_rights.md`
7. `literature/final_library.csv`
8. `literature/evidence_matrix.csv`
9. `final/citation_audit_v1.2.md`

## LaTeX 重构阶段 3：工程与双栏版式样张（2026-10-30）

- [x] 已建立 `latex/main.tex`、`preamble.tex`、`references.bib`、`sections/`、`figures/reused/`、`figures/tikz/`、`tables/`、`licenses/` 和 `output/`。
- [x] 已核查指定上游模板，固定核查提交为 `b8b4c471af8116a778a6233b55b6e5ec3c1e287f`；许可证为 MIT，版权声明为 `Copyright (c) 2025 HuangYaorong`，完整文本已保存在 `latex/licenses/upstream_template_LICENSE.txt`。
- [x] 已用 `ctexart + XeLaTeX` 重新实现版式方案，没有复制上游示例正文、示例图片或手工参考文献内容。
- [x] 首页采用通栏中英文题目、作者与单位占位符、中英文摘要和关键词；摘要后正文切换为双栏。
- [x] 页面为 A4，四边页边距 2 cm，栏间距 0.8 cm；已配置中文标题层级、图表题注、章内公式编号、页眉页码和末页栏平衡。
- [x] 已配置字体检测与后备：英文优先 Times New Roman、后备 TeX Gyre Termes；中文正文优先 SimSun、后备 FandolSong；标题优先 SimHei、后备 FandolHei；作者单位使用 FandolFang。
- [x] 已使用 `biblatex-gb7714-2015 + biber` 生成 GB/T 7714—2015 顺序编码参考文献，并设置 2 em 悬挂缩进。
- [x] 样张包含 1 个 LaTeX 原生公式、1 张 `booktabs + tabularx + threeparttable` 三线表和 1 幅项目内原创的黑白 TikZ 临时占位图；公式、图、表和章节均使用 `label` 与 `cref`。
- [x] 样张只引用 3 条已核验文献以测试工具链；这不代表最终 43 篇文献库缩减。
- [x] 已生成 2 页样张：`latex/output/layout_sample.pdf`。本阶段未迁移 v1.2 正文，未导入任何外部图片。

### 阶段 3 编译与验收

- 编译命令：`latexmk -xelatex -interaction=nonstopmode -halt-on-error -jobname=layout_sample -outdir=output main.tex`。
- 编译结果：XeLaTeX、Biber 和 xdvipdfmx 全流程成功；PDF 为 2 页 A4，文件尺寸约 234 KiB。
- 字体检查：Times New Roman、SimSun、SimHei、FandolFang 及数学字体均嵌入 PDF；未发现字体缺失或字形替代警告。
- 引用检查：无未定义引用、重复标签或待重跑提示；正文引文、公式、图和表的编号及超链接均已解析。
- 版面检查：无 `overfull box`；逐页渲染检查未发现文字、图表越过页边距或栏宽，中文断行、标题层级、单栏表宽和末页双栏平衡正常。
- 参考文献检查：顺序编号和 2 em 悬挂缩进可见；窄栏内长英文题名产生 4 条 `underfull hbox` 疏排提示，但没有溢出或截断。
- 环境提示：TeX Live 当前格式文件为 LaTeX 2025-11-01，而个别已安装宏包请求 2026-06-01，日志保留一条版本提示；不影响本次编译结果。项目附带的深度 PDF QA 脚本因环境未安装 PyMuPDF 无法执行，已改用 `pdfinfo`、`pdffonts`、`pdftotext` 和 Poppler 逐页渲染完成替代检查。
- 版权检查：样张图为本项目 TikZ 临时图，外部复用图片为 0；`latex/figures/reused/` 保持为空。

### 阶段 3 新增或修改文件

1. `latex/main.tex`
2. `latex/preamble.tex`
3. `latex/references.bib`
4. `latex/sections/layout_sample_body.tex`
5. `latex/tables/layout_sample_table.tex`
6. `latex/figures/tikz/layout_placeholder.tex`
7. `latex/licenses/upstream_template.md`
8. `latex/licenses/upstream_template_LICENSE.txt`
9. `latex/README.md`
10. `latex/output/.gitignore`
11. `latex/output/layout_sample.pdf`
12. `PROGRESS.md`

## 继续工作所需文件（阶段 3 后）

1. `AGENTS.md`
2. `PROGRESS.md`
3. `latex/CONTENT_BLUEPRINT.md`
4. `latex/main.tex`
5. `latex/preamble.tex`
6. `latex/references.bib`
7. `latex/README.md`
8. `latex/output/layout_sample.pdf`
9. `latex/licenses/figure_rights.md`
10. `literature/final_library.csv`
11. `literature/evidence_matrix.csv`

## LaTeX 重构阶段 4：引言与通信模型（2026-10-30）

- [x] 已新建 `latex/sections/introduction.tex`，按“背景—无线通信瓶颈—已有综述—本文范围—分类思路—文章结构”重新组织，不逐句迁移 v1.2。
- [x] 已新建 `latex/sections/system_model.tex`，将系统参与者、训练流程、通信消息和指标口径纳入同一模型，并在每组公式前说明建模目的、公式后解释其通信效率含义。
- [x] 已使用 LaTeX 原生数学环境规范呈现五组核心关系：全局经验风险（2.1）、本地模型更新（2.2）、FedAvg 聚合（2.3）、累计通信量（2.4）、无线速率/时延/能耗（2.5a～2.5c）；所有公式均有标签和正文交叉引用，没有公式图片。
- [x] 本阶段新增正文按汉字字符统计约 1303 字，位于要求的 1200～1600 字范围；引言约 565 字，第 2 节约 738 字。
- [x] 当前正文实际使用 9 篇已核验文献，其中中文 3 篇、英文 6 篇；全部可在 `literature/final_library.csv` 中找到。参考文献库总体仍保持 43 篇，不因阶段性 PDF 只列已引用条目而缩减。
- [x] 重要技术定义优先引用 FedAvg 原始论文及无线联邦学习建模研究；综述性判断使用移动边缘、无线通信和中文综述证据；未写入超出证据范围的性能数字。
- [x] `latex/main.tex` 已切换为阶段正文入口；摘要、关键词仍明确保留为“全文完成后撰写/确定”的占位状态，未越界提前撰写。
- [x] 已扩充 `latex/references.bib` 至当前阶段所需的 9 条 GB/T 7714—2015 条目，并完成正文引文、Biber 条目和最终文献库的闭环检查。
- [x] 已生成当前完整 PDF：`latex/output/manuscript_current.pdf`（2 页 A4）。逐页渲染确认公式、中文换行、双栏栏宽和参考文献均无裁切。

### 阶段 4 编译与验收

- 编译命令：`latexmk -xelatex -interaction=nonstopmode -halt-on-error -jobname=manuscript_current -outdir=output main.tex`。
- 编译结果：XeLaTeX、Biber 和 xdvipdfmx 全流程成功；公式编号连续为（2.1）～（2.5c），9 条正文引文和参考文献编号均已解析。
- 日志检查：无未定义引用、重复标签、`overfull box`、`underfull box` 或字体缺失警告。仅保留 TeX Live 格式文件版本早于个别宏包请求版本的环境提示，不影响输出。
- 字体检查：Times New Roman、SimSun、SimHei、FandolFang 和数学字体均嵌入 PDF。
- 自动检查：`poster_validate.py check-tex main.tex` 通过，未报告错误或版宽风险；另用 `pdfinfo`、`pdffonts`、`pdftotext` 和 Poppler 逐页渲染复核。
- 末页处理：阶段性稿件暂不强制平衡参考文献末页双栏，以避免短稿使用 `balance` 时产生基线舍入溢出；全文完成后再统一平衡末页。
- 图表与版权：本阶段没有新增或复用图片、表格，`latex/licenses/figure_rights.md` 无需增加条目。

### 阶段 4 新增或修改文件

1. `latex/sections/introduction.tex`
2. `latex/sections/system_model.tex`
3. `latex/main.tex`
4. `latex/references.bib`
5. `latex/preamble.tex`
6. `latex/README.md`
7. `latex/output/.gitignore`
8. `latex/output/manuscript_current.pdf`
9. `PROGRESS.md`

## 继续工作所需文件（阶段 4 后）

1. `AGENTS.md`
2. `PROGRESS.md`
3. `latex/CONTENT_BLUEPRINT.md`
4. `latex/sections/introduction.tex`
5. `latex/sections/system_model.tex`
6. `latex/main.tex`
7. `latex/preamble.tex`
8. `latex/references.bib`
9. `literature/final_library.csv`
10. `literature/evidence_matrix.csv`
11. `latex/output/manuscript_current.pdf`

## LaTeX 重构阶段 5A：方法综述前半部分（2026-10-31）

- [x] 已新建 `latex/sections/methods_5a.tex`，写入第 3 章分类导语以及第 3.1“客户端选择与通信频率控制”、第 3.2“无线资源分配与联合优化”和第 3.3“模型压缩与通信载荷削减”。
- [x] 三节均按“通信瓶颈—优化变量—共同机制—方法演进—通信收益—代价—适用场景—局限”展开，没有按论文逐篇分段，也没有把不同实验条件下的百分比直接排名。
- [x] 第 3.1 节以参与集合 `\mathcal S_t`、本地步数 `E_k` 和异步时序为比较轴，区分资源/信道感知选择、长期公平约束和自适应/异步通信，并讨论状态反馈、选择偏差、陈旧性和公平性。
- [x] 第 3.2 节明确资源分配主要改变速率、时延和能耗，而不必然减少传输比特；比较单轮与跨轮、单业务与多业务、解析优化与在线学习，并记录信道反馈、求解开销及数据代表性风险。
- [x] 第 3.3 节统一比较量化、稀疏化、压缩感知和自适应混合压缩；新增式（3.1），用非零比例 `s_{k,t}` 和有效传输比 `\rho_{k,t}^{\mathrm{eff}}` 区分理论稀疏度与包含数值、索引、头部后的实际比特开销。
- [x] 请求的三个小节合计约 1427 个汉字：3.1 约 461 字、3.2 约 450 字、3.3 约 516 字；加第 3 章分类导语后，本阶段新增约 1528 个汉字。三节总量相对蓝图 1400 字预算偏差约 +1.9%。
- [x] 引用密度检查：3.1 有 4 个引文位置、涉及 9 个不同来源；3.2 有 3 个引文位置、涉及 6 个不同来源；3.3 有 4 个引文位置、涉及 8 个不同来源。本阶段共使用 20 个不同来源。
- [x] 当前正文累计引用 25 篇已核验文献，其中中文 8 篇、英文 17 篇；`references.bib` 的 25 条记录全部在正文出现，正文所有引用键均能解析，并均可追溯至 `literature/final_library.csv`。
- [x] 没有写入跨论文可比性不足的性能数字；`C012` 等联合方法只用于机制与适用条件，未拆分宣称无法由原证据分离的单项贡献。
- [x] 本阶段未创建、复制或修改 AirComp 和分层联邦学习图片，也没有写第 3.4—3.5 节。

### 阶段 5A 编译与验收

- 编译命令：`latexmk -xelatex -interaction=nonstopmode -halt-on-error -jobname=manuscript_current -outdir=output main.tex`。
- 编译结果：XeLaTeX、Biber 和 xdvipdfmx 全流程成功；当前 `latex/output/manuscript_current.pdf` 为 4 页 A4，文件约 263 KiB。
- 公式与引用：压缩公式编号为（3.1），章节和公式交叉引用均已解析；Biber 输出 25 条参考文献，无遗漏或未引用条目。
- 日志检查：无未定义引用、重复标签、`overfull box`、`underfull box`、Biber 错误或字体缺失警告；仅保留 TeX Live 格式文件版本早于个别宏包请求版本的环境提示。
- 字体与版面：Times New Roman、SimSun、SimHei、FandolFang 和数学字体均嵌入；逐页渲染确认正文、公式和参考文献未越出栏宽或页边距。阶段性末页因正文尚未完成而右栏留白，待全文完成后统一平衡。
- 自动检查：`poster_validate.py check-tex main.tex` 通过。深度 `pdf_qa.py --formulas` 因环境缺少 PyMuPDF 无法运行，已使用 `pdfinfo`、`pdffonts`、`pdftotext`、日志扫描和 Poppler 逐页渲染替代检查。
- 缩写检查：ARS 缩写脚本不直接接受 `.tex` 输入，已人工复核本阶段缩写；首次出现的中央处理器（CPU）已补充中文全称，FedAvg 已在引言定义。

### 阶段 5A 新增或修改文件

1. `latex/sections/methods_5a.tex`
2. `latex/main.tex`
3. `latex/references.bib`
4. `latex/README.md`
5. `latex/output/manuscript_current.pdf`
6. `PROGRESS.md`

## 继续工作所需文件（阶段 5A 后）

1. `AGENTS.md`
2. `PROGRESS.md`
3. `latex/CONTENT_BLUEPRINT.md`
4. `latex/sections/introduction.tex`
5. `latex/sections/system_model.tex`
6. `latex/sections/methods_5a.tex`
7. `latex/main.tex`
8. `latex/preamble.tex`
9. `latex/references.bib`
10. `literature/final_library.csv`
11. `literature/evidence_matrix.csv`
12. `latex/output/manuscript_current.pdf`

## 下一步（待用户确认）

阶段 5A 已完成并停止。等待用户审阅第 3.1—3.3 节及当前 PDF；未经明确授权，不写第 3.4 空中计算、第 3.5 分层联邦学习，不制作相关图片，也不进入方法比较、趋势或结论章节。

## LaTeX 重构阶段 5B：方法综述后半部分与已审核图片（2026-10-31）

- [x] 已新建 `latex/sections/methods_5b.tex`，完成第 3.4“空中计算与通信聚合融合”和第 3.5“分层联邦学习与网络拓扑优化”。
- [x] 第 3.4 节明确区分数字正交传输与 AirComp：前者分配独立时频资源、逐用户解码后求和，后者让终端同频同时发送并利用多址信道叠加直接估计加权和。
- [x] 已用 LaTeX `subequations + align` 原生排版 AirComp 接收信号、目标聚合值和聚合误差，编号为（3.2a）～（3.2c）；变量首次出现处均已解释。
- [x] 已明确 AirComp 并非“零代价聚合”：收益依赖信道估计、载波与符号同步、功率控制/信道反演和噪声条件；时变信道、稀疏一比特与分层 AirComp 只在各自系统假设内定性比较。
- [x] 第 3.5 节用 LaTeX 原生公式表示簇内边缘聚合与每 \(H\) 次边缘聚合后的云端聚合，编号为（3.3a）～（3.3b）。
- [x] 已说明分层 FL 通过端—边高频、边—云低频的双时间尺度减少远距离回传，但会引入簇内非独立同分布数据造成的边缘聚合偏差，以及节点分组、调度、边缘负载、故障和层间协调问题。
- [x] 两节均沿“瓶颈—优化变量—机制—代表性演进—收益—代价—场景—局限”综合论述，没有逐篇摘要式罗列，也没有写入跨论文不可比的性能数字。
- [x] 第 3.4 节约 533 个汉字，第 3.5 节约 544 个汉字，本阶段新增约 1077 个汉字。
- [x] 已新增 10 条已核验 BibTeX 记录，并复用既有 `Liu2020HierarchicalFL`；当前正文累计引用 35 篇已核验文献，其中中文 11 篇、英文 24 篇。正文全部引用键均能解析，`references.bib` 的 35 条记录均已在正文或图注中引用。

### 阶段 5B 图片与版权处理

- [x] 阶段 1 的最终结论为“适合直接复用的相关图片 0 幅”。本阶段没有从原 PDF 提取图片，也没有复制、裁剪、翻译或改绘权利不明确及 IEEE/ACM 默认版权图片。
- [x] 已创建 `latex/figures/tikz/aircomp_mechanism.tex`：黑白通栏矢量图，对比数字正交上传与 AirComp 的信号处理链，并使图中变量与式（3.2）一致。
- [x] 已创建 `latex/figures/tikz/hierarchical_aggregation.tex`：黑白通栏矢量图，展示端—边—云双时间尺度聚合，并使 \(H\) 与式（3.3）的云端周期一致。
- [x] 两幅图均在出现前后由正文解释其论点，不是装饰性流程图；图注列出事实依据文献，并明确“原创图，未直接复用或改编第三方图片”。
- [x] 已在 `latex/licenses/figure_rights.md` 记录最终文件名、用途、事实依据、第三方声明、修改情况、最终图注和暂停复用的权利疑点；`latex/figures/reused/` 保持为空。
- [x] 暂停项保持不变：Sun 2022 Figure 15、Xiao 等 OTA-FL Figure 1、Wu 2024 Figure 8、Le 2024 Figure 5.1 等图片没有足够明确的复用许可，未进入工程。

### 阶段 5B 编译与验收

- 编译命令：`latexmk -xelatex -interaction=nonstopmode -halt-on-error -jobname=manuscript_current -outdir=output main.tex`。
- 编译结果：XeLaTeX、Biber 和 xdvipdfmx 全流程成功；`latex/output/manuscript_current.pdf` 为 6 页 A4，约 306 KiB。
- 浮动体：参考文献前使用 `\clearpage` 清空阶段性稿件的通栏浮动队列；两幅图连续位于方法章节之后，参考文献从下一页开始，不再发生图表与参考文献混排。待第 4—6 章加入后，可按全文分页重新评估该阶段性分页控制。
- 清晰度：两幅图直接由 TikZ 输出为 PDF 矢量内容，无栅格缩放损失；以 150 dpi 渲染第 3—4 页目视检查，图中文字、箭头和公式变量可辨识，未越出页边距。
- 日志检查：无未定义引用、重复标签、`overfull box`、`underfull box`、Biber 错误或字体缺失警告；仅保留 TeX Live 格式文件版本早于个别宏包请求版本的环境提示。
- 字体检查：Times New Roman、SimSun、SimHei、FandolFang 和数学字体均嵌入 PDF。
- 公式与交叉引用：式（3.2a）～（3.3b）、图 1、图 2 和正文交叉引用均已解析。

### 阶段 5B 新增或修改文件

1. `latex/sections/methods_5b.tex`
2. `latex/figures/tikz/aircomp_mechanism.tex`
3. `latex/figures/tikz/hierarchical_aggregation.tex`
4. `latex/references.bib`
5. `latex/main.tex`
6. `latex/licenses/figure_rights.md`
7. `latex/README.md`
8. `latex/output/manuscript_current.pdf`
9. `PROGRESS.md`

## 继续工作所需文件（阶段 5B 后）

1. `AGENTS.md`
2. `PROGRESS.md`
3. `latex/CONTENT_BLUEPRINT.md`
4. `latex/sections/introduction.tex`
5. `latex/sections/system_model.tex`
6. `latex/sections/methods_5a.tex`
7. `latex/sections/methods_5b.tex`
8. `latex/main.tex`
9. `latex/preamble.tex`
10. `latex/references.bib`
11. `latex/licenses/figure_rights.md`
12. `literature/final_library.csv`
13. `literature/evidence_matrix.csv`
14. `latex/output/manuscript_current.pdf`

## 下一步（待用户确认）

阶段 5B 已完成并停止。等待用户审阅第 3.4—3.5 节、两幅原创 TikZ 图和当前 PDF；未经明确授权，不进入第 4 章方法比较、第 5 章趋势、第 6 章结论或摘要写作。

## LaTeX 重构阶段 6：比较分析、发展趋势、结论与摘要（2026-10-31）

- [x] 已新建 `latex/sections/discussion_conclusion.tex`，完成第 4 节“方法比较与适用场景分析”、第 5 节“现存问题与发展趋势”和第 6 节“结论”。
- [x] 第 4 节采用横向比较，不重复第 3 节的逐类机制说明；以成本分量、额外代价和系统假设为统一比较轴，指出五类方法分别改变通信轮数/参与规模、无线传输、载荷或消息路径，组合方法需避免重复计算收益。
- [x] 已新建 `latex/tables/method_comparison.tex`。综合表覆盖优化对象、代表机制、主要收益、额外代价、关键假设、适用场景和主要局限；每一行均给出可追溯至已核验文献的代表来源。
- [x] 因正文（含表格文字）已接近 5500 字上限，本阶段没有增加可选的第二张代表性文献表；代表文献已通过综合表行内引文和场景分析纳入比较。
- [x] 第 5 节只保留与通信效率直接相关且有证据支持的方向：跨层在线联合优化、异构网络适配、学习与通信协同、任务/语义导向消息设计和可复现实验评价。隐私与安全仅作为增加比特、计算和时延的约束简述，没有扩展为并列主线。
- [x] 第 6 节综合归纳五类方法的作用位置、收益—代价关系和选择原则，没有引入新文献、新机制或原创算法表述。
- [x] `latex/main.tex` 已写入中文摘要、5 个中文关键词、内容对应的英文摘要和 5 个英文关键词。中文摘要按“背景—问题—分类范围—主要认识—用途”组织，不含引文；摘要约 241 个汉字（不计“摘要”标签）。
- [x] `latex/references.bib` 新增 8 条先前已完成元数据核验且在本阶段实际使用的文献；当前共 43 条，其中中文 17 条、英文 26 条，满足总量与中文文献目标。

### 阶段 6 全文统计与引用审计

- 正文各节及综合表合计 5487 个汉字；若按通常口径不计表格文字，正文叙述为 5004 个汉字。两种口径均已记录，其中严格口径满足 4500—5500 字验收范围。
- 图表：2 幅原创 TikZ 黑白矢量图，1 张 `booktabs`/`tabularx` 综合比较表。
- 公式：8 组 LaTeX 原生公式环境，共 13 个编号公式或子公式；不存在图片公式。
- 参考文献：43 篇（中文 17、英文 26）。全文使用 43 个不同引用键；引用键与 BibTeX 条目双向一致，无缺失条目，也无未在正文出现的条目。
- 具体性能百分比未用于跨论文排名；表格结论限定于证据矩阵可支持的机制、收益类型、代价、假设和场景。

### 阶段 6 编译与版面验收

- 编译命令：`latexmk -xelatex -interaction=nonstopmode -halt-on-error -jobname=manuscript_current -outdir=output main.tex`。
- 编译结果：XeLaTeX、Biber 和 xdvipdfmx 全流程成功；`latex/output/manuscript_current.pdf` 为 8 页 A4，文件 405046 字节。
- 日志检查：无未定义引用、重复标签、`overfull box`、`underfull box`、Biber 错误或字体缺失警告；仅有 LaTeX 发布版本请求与当前格式版本不一致的环境提示，不影响输出。
- 字体检查：Times New Roman、SimSun、SimHei、FandolFang 和数学字体均嵌入 PDF。
- 目视检查：已渲染检查摘要页、公式页、两幅图及综合表所在页；未发现裁切、重叠、栏宽溢出或不可辨识文字。综合表采用约 7.1 pt 字号以适应双栏通栏宽度。

### 阶段 6 新增或修改文件

1. `latex/sections/discussion_conclusion.tex`
2. `latex/tables/method_comparison.tex`
3. `latex/main.tex`
4. `latex/references.bib`
5. `latex/README.md`
6. `latex/output/manuscript_current.pdf`
7. `PROGRESS.md`

## 继续工作所需文件（阶段 6 后）

1. `AGENTS.md`
2. `PROGRESS.md`
3. `latex/CONTENT_BLUEPRINT.md`
4. `latex/main.tex`
5. `latex/preamble.tex`
6. `latex/sections/introduction.tex`
7. `latex/sections/system_model.tex`
8. `latex/sections/methods_5a.tex`
9. `latex/sections/methods_5b.tex`
10. `latex/sections/discussion_conclusion.tex`
11. `latex/tables/method_comparison.tex`
12. `latex/references.bib`
13. `literature/final_library.csv`
14. `literature/evidence_matrix.csv`
15. `latex/output/manuscript_current.pdf`

## 下一步（待用户确认）

阶段 6 已完成并停止。等待用户审阅全文初稿、摘要和综合比较表；未经明确授权，不进入全文润色、图表增补、终稿审校或交付版本生成。

## LaTeX 重构阶段 7：全文事实、引用、版权和版式终审（2026-10-31）

### 已完成

- [x] 逐节复核算法名称、研究场景、优化对象、收益、代价和适用条件；删除或收紧证据不足的强判断，不保留跨论文性能百分比。
- [x] 修正本地 SGD、压缩/稀疏率和无线物理单位表达；8 组公式均为 LaTeX 原生对象，共 13 个编号公式或子公式。
- [x] 核对 `references.bib` 的 43 条元数据与 `literature/final_library.csv`；38 条 DOI 中 24 条由 Crossref 直接返回，14 条中文 DOI 由期刊官网和既有核验记录支持，5 条稳定 URL 均可访问。
- [x] 完成引用闭环检查：43 个唯一引用键对应 43 个唯一 BibTeX 条目，未引用、缺失和重复均为 0；Biber 顺序与正文首次出现顺序一致。
- [x] 对照 `latex/licenses/figure_rights.md` 复核两幅图。最终直接复用外部图片 0 幅，两幅正式图片均为原创 TikZ 黑白矢量图。
- [x] 最终统计：正文与综合比较表共 5269 个汉字（叙述 4804、表格 465），参考文献 43 篇（中文 17、英文 26），图 2 幅、表 1 张、公式 8 组。
- [x] 对最终文件名强制执行两轮完整 XeLaTeX+Biber 构建；日志无未定义引用、重复标签、字体缺失和 overfull/underfull 警告。
- [x] 已用 `pdfinfo`、`pdffonts`、`pdfimages`、`pdftotext`、MuPDF 和 Poppler 逐页检查。最终 PDF 为 7 页 A4，字体全部嵌入，无栅格图片对象，图表无拉伸、裁切或截图边框。
- [x] 已清理 `latex/output/` 中的编译辅助文件和临时预览图，保留正式 PDF、阶段 PDF、审计报告和构建说明。
- [x] v1.2 DOCX 未覆盖；未执行 Git 提交或推送。

> 阶段 6 的字数和页数是当时的阶段性统计。本阶段以活跃源文件和最终命名 PDF 重新统计，最终口径为 5269 个正文汉字、7 页。

### 阶段 7 新增或修改文件

1. `latex/main.tex`
2. `latex/sections/system_model.tex`
3. `latex/sections/methods_5a.tex`
4. `latex/sections/discussion_conclusion.tex`
5. `latex/tables/method_comparison.tex`
6. `latex/figures/tikz/aircomp_mechanism.tex`
7. `latex/licenses/figure_rights.md`
8. `latex/README.md`
9. `latex/output/无线边缘网络中联邦学习通信效率优化方法研究综述_final.pdf`
10. `latex/output/final_audit.md`
11. `latex/output/build_instructions.md`
12. `PROGRESS.md`

## 继续工作所需文件（阶段 7 后）

1. `AGENTS.md`
2. `PROGRESS.md`
3. `latex/main.tex`
4. `latex/preamble.tex`
5. `latex/references.bib`
6. `latex/licenses/figure_rights.md`
7. `latex/output/final_audit.md`
8. `latex/output/build_instructions.md`
9. `latex/output/无线边缘网络中联邦学习通信效率优化方法研究综述_final.pdf`

## 下一步（待用户确认）

阶段 7 已完成并停止。提交前由用户填写真实中英文作者与单位信息，并按 `latex/output/build_instructions.md` 重新编译；若正文论断范围不扩大，无需重新检索或增加文献。
