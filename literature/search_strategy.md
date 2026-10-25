# 阶段 1 检索策略：无线边缘网络中的联邦学习通信效率优化

## 1. 检索目标与边界

- 目标：建立 60～80 篇可追溯的候选文献库，其中中文候选不少于 20 篇，为后续筛选与证据矩阵提供输入。
- 本阶段仅做候选发现、去重与出版元数据核验；不筛选最终文献，不从摘要推演研究结论，不撰写论文正文。
- 主题边界：联邦学习在无线边缘网络、移动边缘计算、边缘智能或云—边—端架构中的通信效率问题，以及可迁移到该场景的基础通信压缩方法。
- 时间范围：主体检索为 2016-01-01 至 2026-10-11；允许纳入更早的分布式学习通信压缩奠基文献，但须在后续筛选中说明其基础性。
- 语言：中文、英文。
- 文献类型：优先同行评审期刊论文和高水平会议论文；综述、专著/章节和学位论文用于框架或线索补充；预印本仅作补充并单独标记。

## 2. 概念组与同义词

### 2.1 英文概念组

| 组别 | 检索词 |
|---|---|
| A 联邦学习 | `federated learning` OR `federated edge learning` OR `wireless federated learning` OR `federated optimization` |
| B 边缘/无线场景 | `wireless edge network*` OR `mobile edge computing` OR `multi-access edge computing` OR `edge intelligence` OR `edge computing` OR `cloud-edge-device` OR `edge-assisted` |
| C 通信代价 | `communication efficien*` OR `communication cost` OR `communication overhead` OR `bandwidth efficien*` OR `training latency` |
| D 本地更新/聚合频率 | `local update*` OR `local iteration*` OR `communication frequenc*` OR `periodic averaging` OR `adaptive aggregation` OR `asynchronous aggregation` |
| E 压缩 | `model compression` OR `gradient compression` OR quantization OR sparsification OR pruning OR ternarization OR `one-bit` |
| F 客户端与资源 | `client selection` OR `device selection` OR scheduling OR `device scheduling` OR `resource allocation` OR `bandwidth allocation` |
| G 空中聚合 | `over-the-air computation` OR `over-the-air aggregation` OR `analog aggregation` OR AirComp |
| H 分层架构 | `hierarchical federated learning` OR `edge-assisted federated learning` OR `client-edge-cloud` OR `cloud-edge-end` |

### 2.2 中文概念组

| 组别 | 检索词 |
|---|---|
| A 联邦学习 | 联邦学习 OR 联邦边缘学习 OR 无线联邦学习 OR 联邦优化 |
| B 边缘/无线场景 | 无线边缘网络 OR 移动边缘计算 OR 多接入边缘计算 OR 边缘智能 OR 边缘计算 OR 云边端 OR 边缘辅助 |
| C 通信代价 | 通信效率 OR 通信成本 OR 通信开销 OR 带宽效率 OR 训练时延 |
| D 本地更新/聚合频率 | 本地更新 OR 本地迭代 OR 通信频率 OR 周期聚合 OR 自适应聚合 OR 异步聚合 |
| E 压缩 | 模型压缩 OR 梯度压缩 OR 量化 OR 稀疏化 OR 剪枝 OR 三值化 OR 一比特 |
| F 客户端与资源 | 客户端选择 OR 设备选择 OR 设备调度 OR 用户调度 OR 资源分配 OR 带宽分配 |
| G 空中聚合 | 空中计算 OR 空中聚合 OR 模拟聚合 OR 通信计算一体化 |
| H 分层架构 | 分层联邦学习 OR 边缘辅助联邦学习 OR 端边云 OR 云边端 OR 分层聚合 |

## 3. 核心布尔检索式

### 3.1 英文综合式

```text
("federated learning" OR "federated edge learning" OR "wireless federated learning")
AND
("wireless edge network*" OR "mobile edge computing" OR "multi-access edge computing"
 OR "edge intelligence" OR "edge computing" OR "edge-assisted")
AND
("communication efficien*" OR "communication cost" OR "communication overhead"
 OR "training latency" OR "bandwidth efficien*")
```

### 3.2 英文专题式

```text
S1 = ("federated learning") AND ("local update*" OR "local iteration*" OR
      "communication frequenc*" OR "periodic averaging" OR "adaptive aggregation")

S2 = ("federated learning") AND ("model compression" OR "gradient compression" OR
      quantization OR sparsification OR pruning OR ternarization)

S3 = ("federated learning") AND ("client selection" OR "device scheduling" OR
      "resource allocation" OR "bandwidth allocation") AND (wireless OR edge)

S4 = ("federated learning" OR "federated edge learning") AND
      ("over-the-air computation" OR "over-the-air aggregation" OR
       "analog aggregation" OR AirComp)

S5 = ("hierarchical federated learning" OR "edge-assisted federated learning" OR
      "client-edge-cloud") AND (communication OR aggregation OR resource*)
```

### 3.3 中文综合式

```text
(联邦学习 OR 联邦边缘学习 OR 无线联邦学习)
AND
(无线边缘网络 OR 移动边缘计算 OR 边缘智能 OR 边缘计算 OR 云边端)
AND
(通信效率 OR 通信成本 OR 通信开销 OR 带宽效率 OR 训练时延)
```

### 3.4 中文专题式

```text
S1 = 联邦学习 AND (本地更新 OR 本地迭代 OR 通信频率 OR 自适应聚合 OR 异步聚合)
S2 = 联邦学习 AND (模型压缩 OR 梯度压缩 OR 量化 OR 稀疏化 OR 剪枝)
S3 = 联邦学习 AND (客户端选择 OR 设备调度 OR 资源分配 OR 带宽分配)
S4 = (联邦学习 OR 联邦边缘学习) AND (空中计算 OR 空中聚合 OR 模拟聚合 OR 通信计算一体化)
S5 = (分层联邦学习 OR 边缘辅助联邦学习 OR 端边云 OR 云边端) AND (通信 OR 聚合 OR 资源)
```

## 4. 数据库适配

- IEEE Xplore / ACM DL / ScienceDirect / Springer：使用上述英文综合式与专题式，题名、摘要、关键词字段优先；会议名和期刊名用于二次收窄。
- Web of Science：`TS=(...)`，年份限制为 2016–2026，文献类型优先 Article、Proceedings Paper、Review。
- Google Scholar：拆分为短式精确短语检索，例如 `"federated learning" "over-the-air aggregation"`；仅用于发现与引用追踪，元数据回到出版页面或 DOI 核验。
- 知网 / 万方 / 国家哲学社会科学文献中心：主题字段使用中文综合式；再以“梯度压缩、客户端选择、资源分配、空中计算、分层联邦学习”分别扩展。
- 中文核心期刊官网：以题名或 DOI 复核作者、卷期页码和稳定链接。
- Crossref：仅用于出版元数据核对和 DOI 解析，不以其相关性排序代替人工主题判断。
- Consensus / Scite：本环境未发现已连接工具，故本轮未使用；若后续连接，只用于发现和引用关系查看，不能代替原文或出版元数据核验。

## 5. 候选进入规则（非最终筛选）

候选条目满足以下任一条件即可进入本阶段候选库：

1. 直接研究无线/边缘联邦学习的通信、时延、能耗或资源调度；
2. 研究可降低联邦学习通信轮次或传输比特数的本地更新、压缩、量化、稀疏化、客户端选择或聚合方法；
3. 研究空中计算/模拟聚合或分层/边缘辅助联邦学习；
4. 属于定义问题、建立基线或综述分类所需的奠基性研究。

暂不进入的记录：纯隐私/安全而无通信或边缘关联、仅将联邦学习作为应用工具且不讨论训练通信、非学术网页、专利、营销材料，以及元数据无法定位的搜索片段。

## 6. 元数据与核验状态

- `已核验（出版元数据）`：题名、作者、年份、来源和 DOI/稳定 URL 已由出版社、会议、期刊官网、学位授予单位或 Crossref 记录相互确认。
- `待核验（元数据不完整）`：候选存在性可见，但至少一项关键元数据尚未从权威页面确认。
- `待核验（预印本）`：仅有预印本或技术报告版本，后续需检查是否存在正式发表版本。
- 全文状态独立记录；“元数据已核验”不等于“全文已读”。无法访问全文者进入 `download_requests.md`。

## 7. 去重规则

1. DOI 完全相同视为重复；保留元数据更完整的正式版本。
2. 题名高度相同且作者、年份一致时，优先期刊/会议正式版本，预印本仅在备注中保留。
3. 同一工作的会议版和扩展期刊版暂作为不同候选，但须标注版本关系，留待阶段 2 判断。
4. 中文译题与英文原题不自动视为两篇；需依据 DOI、作者和来源判断。

## 8. 实际检索记录与限制

- 检索日期：2026-10-11（Asia/Shanghai）。
- 已实际访问：IEEE Xplore、PMLR、ScienceDirect、Springer、Crossref 官方 API、中文期刊官网、知网页面镜像/期刊平台、万方条目页及通用网页检索。
- 未能直接登录或完整复现：Web of Science、知网主站高级检索、部分万方全文、机构订阅全文。检索式已保留，后续可由具备机构访问权限的用户复跑。
- 候选库不记录搜索摘要中的性能数字或结论；主题类别仅依据题名、关键词和出版页面可见的研究对象标注。
- 当前候选库是宽口径发现集，不代表最终参考文献资格。
