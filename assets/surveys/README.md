# 无线边缘联邦学习通信效率综述阅读包

更新时间：2026-10-30

本目录收录与《无线边缘网络中联邦学习通信效率优化方法研究综述》直接相关的公开全文。文件仅来自 arXiv、作者公开版、期刊开放获取页面或中文期刊官网；没有使用非授权镜像。若正式出版版本非开放获取，则只在文末提供 DOI 和出版社入口。

## 最值得先读的六篇

### 1. 孙兵等：移动边缘网络中联邦学习效率优化综述（2022）

- 本地全文：[`02_sun_2022_mobile_edge_efficiency_cn.pdf`](02_sun_2022_mobile_edge_efficiency_cn.pdf)
- 正式来源：[《计算机研究与发展》官网PDF](https://crad.ict.ac.cn/cn/article/pdf/preview/10.7544/issn1000-1239.20210119.pdf)
- DOI：10.7544/issn1000-1239.20210119
- 相关度：极高，题目、场景和中文课程综述写法都与当前论文接近。
- 建议学习：引言怎样从通信消耗、训练效率和安全问题限定范围；怎样先建立大分类，再用表格比较代表性工作；每类方法结尾怎样总结优点、不足和未来方向。
- 注意：它把安全与隐私作为独立主类，而当前论文只应把二者作为通信约束，不能照搬其范围。

### 2. Jia等：A Comprehensive Survey on Communication-Efficient Federated Learning in Mobile Edge Environments（2025）

- 全文状态：IEEE正式版本目前为非开放获取，本目录不保存非授权副本。
- 出版信息与摘要：[HKUST研究门户](https://researchportal.hkust.edu.hk/en/publications/a-comprehensive-survey-on-communication-efficient-federated-learn/)
- DOI：[10.1109/COMST.2025.3535957](https://doi.org/10.1109/COMST.2025.3535957)
- 相关度：最高，主题几乎与本课程论文同构。
- 建议学习：其三条主线——降低通信复杂度、资源调度、空中计算——可用于检查当前五类框架是否遗漏关键联系；重点关注它如何把收敛、数据异构与无线调度串在同一论证链中。
- 获取建议：若学校图书馆可访问 IEEE Xplore，应优先阅读全文。

### 3. Lim等：Federated Learning in Mobile Edge Networks: A Comprehensive Survey（2020）

- 本地全文：[`01_lim_2020_mobile_edge_fl_survey.pdf`](01_lim_2020_mobile_edge_fl_survey.pdf)
- 公开作者版：[arXiv](https://arxiv.org/abs/1909.11875)
- 正式版本：[IEEE Communications Surveys & Tutorials](https://doi.org/10.1109/COMST.2020.2986024)
- 相关度：高，是移动边缘联邦学习的经典总览。
- 建议学习：相关综述比较、研究范围声明、FL训练流程图、挑战—解决方案—应用—趋势的章节递进方式。它特别适合帮助重写引言和第2章，而不适合直接替代通信效率专题分类。

### 4. Zhao等：Towards Efficient Communications in Federated Learning: A Contemporary Survey（2023）

- 本地全文：[`03_zhao_2023_efficient_communications_survey.pdf`](03_zhao_2023_efficient_communications_survey.pdf)
- 公开作者版：[arXiv](https://arxiv.org/abs/2208.01200)
- 正式版本：[Journal of the Franklin Institute](https://doi.org/10.1016/j.jfranklin.2022.12.053)
- 相关度：极高，专门讨论联邦学习通信问题。
- 建议学习：图2的综述主体结构，以及表1—表3将“通信效率、通信环境、通信资源配置”分别做分类和横向对比的写法。其优点是每一类都有比较表，避免逐篇流水账。

### 5. Le等：Exploring the Practicality of Federated Learning: A Survey Towards the Communication Perspective（2024）

- 本地全文：[`04_le_2024_practical_communication_survey.pdf`](04_le_2024_practical_communication_survey.pdf)
- 公开版本：[arXiv](https://arxiv.org/abs/2405.20431)
- 版本说明：目前按预印本使用，引用前应再次核验是否已有正式出版版本。
- 相关度：极高，重点是实际部署中的通信瓶颈。
- 建议学习：表2.1对通信低效来源的归纳、图4.1的方法分类、各类方法比较表以及未来方向图。它比只列算法名称的综述更重视“原因—方法—指标—部署条件”。

### 6. Xiao等：Over-the-Air Federated Learning: Status Quo, Open Challenges, and Future Directions

- 本地全文：[`05_ota_fl_2023_status_survey.pdf`](05_ota_fl_2023_status_survey.pdf)
- 公开作者版：[arXiv](https://arxiv.org/abs/2307.00974)
- 正式版本：[Fundamental Research，DOI 10.1016/j.fmre.2024.01.011](https://doi.org/10.1016/j.fmre.2024.01.011)
- 相关度：专题性高，主要用于当前论文第3.4节。
- 建议学习：图1的OTA-FL系统模型、单天线/多天线/RIS辅助分类，以及如何在介绍收益后紧接同步、信道估计、噪声、隐私和可信性限制。不要把整篇物理层细节扩展进本科综述。

## 其余已下载全文

| 序号 | 文献与本地文件 | 最适合借鉴的内容 | 使用提醒 |
|---|---|---|---|
| 7 | Wu等，*Topology-aware Federated Learning in Edge Computing: A Comprehensive Survey*（ACM CSUR，2024）[`06_topology_aware_edge_fl_2023_survey.pdf`](06_topology_aware_edge_fl_2023_survey.pdf)；[正式页面](https://doi.org/10.1145/3659205) | PRISMA检索流程、图5拓扑总览、树形/分层拓扑的优缺点表、分层消息交换图 | 用于第3.5节和图4；不要让去中心化与区块链偏离通信效率主线 |
| 8 | Shahid等，*Communication Efficiency in Federated Learning: Achievements and Challenges*（2021预印本）[`07_shahid_2021_communication_efficiency_survey.pdf`](07_shahid_2021_communication_efficiency_survey.pdf)；[arXiv](https://arxiv.org/abs/2107.10996) | 用研究问题组织综述；本地更新、客户端选择、更新缩减、去中心化与压缩分类 | 篇幅和证据深度有限，适合快速建立概念，不应作为唯一权威综述 |
| 9 | 张雪晴等，《面向边缘智能的联邦学习综述》（2023）[`08_zhang_2023_edge_intelligence_fl_cn.pdf`](08_zhang_2023_edge_intelligence_fl_cn.pdf)；[官网PDF](https://crad.ict.ac.cn/cn/article/pdf/preview/10.7544/issn1000-1239.202111100.pdf) | 中文术语、边缘智能系统背景、资源约束与无线FL问题的中文表达 | 范围比通信效率更宽，主要用于引言和基础章节 |
| 10 | Kunjumon等，*A Comprehensive Survey on Communication Optimization and Privacy Preservation in Federated Learning*（2026，OA）[`09_kunjumon_2026_comm_privacy_survey.pdf`](09_kunjumon_2026_comm_privacy_survey.pdf)；[Springer](https://doi.org/10.1007/s10791-026-10272-0) | 调查协议、PRISMA、现有综述比较表、通信与隐私的兼容矩阵和决策框架 | 很新但范围偏向隐私；适合学习方法和结构，不能把当前论文改成安全综述 |
| 11 | Asad等，*Limitations and Future Aspects of Communication Costs in Federated Learning: A Survey*（Sensors，2023）[`10_sensors_2023_communication_cost_survey.pdf`](10_sensors_2023_communication_cost_survey.pdf)；[期刊页面](https://www.mdpi.com/1424-8220/23/17/7358) | 以通信成本为问题中心组织局限和趋势；模型更新、压缩、资源管理与客户端选择 | 分类粒度较粗，适合第5章而非照搬第3章框架 |
| 12 | Pouriyeh等，*Secure Smart Communication Efficiency in Federated Learning: Achievements and Challenges*（Applied Sciences，2022）[`11_applsci_2022_communication_efficiency_survey.pdf`](11_applsci_2022_communication_efficiency_survey.pdf)；[期刊页面](https://www.mdpi.com/2076-3417/12/18/8980) | 两个研究问题驱动的综述结构、通信挑战与解决方案的对应关系 | 安全内容偏多；方法对比深度低于IEEE/ACM综述 |
| 13 | Yan等，*A Survey of Energy-Efficient Strategies for Federated Learning in Mobile Edge Computing*（FITEE，2024）[`12_yan_2024_energy_efficient_mec_cn.pdf`](12_yan_2024_energy_efficient_mec_cn.pdf)；[期刊页面](https://jzus.zju.edu.cn/article.php?doi=10.1631%2FFITEE.2300181) | 系统模型、计算/通信能耗模型、表2的学习方法—资源分配—客户端选择分类，以及图表与正文的紧密解释 | 只用于补强能耗指标和资源配置，不把论文改写为能效综述 |

## 值得保留网址但未下载的正式综述

以下论文为非开放获取或官网仅提供HTML，因此本目录只记录合法入口：

1. *Federated Learning Over Wireless Networks: Challenges and Solutions*，IEEE Internet of Things Journal，2023，10(16):14749–14763。重点学习无线带宽、能耗、隐私与实际部署之间的权衡。[IEEE Xplore](https://ieeexplore.ieee.org/document/10153432)；[DOI](https://doi.org/10.1109/JIOT.2023.3285868)。
2. Almanifi等，*Communication and Computation Efficiency in Federated Learning: A Survey*，Internet of Things，2023，22:100742。重点学习通信优化与计算优化的联动，以及为何只报告压缩率不足。[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2542660523000653)；[DOI](https://doi.org/10.1016/j.iot.2023.100742)。
3. 葛丽娜、王明禹、田蕾，《联邦学习的高效性研究综述》，《计算机应用》，2025，45(8):2387–2398。官网HTML已包含综述对比表和多张方法比较表。[期刊官网](https://www.joca.cn/CN/10.11772/j.issn.1001-9081.2024081119)。
4. 孙恩昌等，《基于联邦学习的移动通信资源管理：方法、进展与展望》。适合学习如何按无线场景组织资源管理方法。[期刊官网HTML](https://journal.bjut.edu.cn/bjgydxxb/article/doi/10.11936/bjutxb2021030017)。

## 建议阅读顺序

如果只安排约两小时，可按以下顺序阅读：

1. 先读孙兵等的摘要、引言、分类框架和结论，掌握中文课程综述的表达方式。
2. 查看Jia等2025年综述的摘要、目录和分类，与当前五类框架逐项对照。
3. 阅读Lim等的引言、相关综述比较、FL流程图和挑战章节，检查第1—2章的铺垫。
4. 阅读Zhao等的图2及表1—表3，再看Le等的表2.1、图4.1和各类比较表，学习横向比较。
5. 只针对薄弱章节阅读OTA-FL和拓扑综述：前者补第3.4节，后者补第3.5节。
6. 最后看Yan等与Asad等的局限和未来方向，用于检查第4—5章是否覆盖指标口径、附加开销和实际部署条件。

## 可以借鉴的写作方法

- 引言不要从“技术很重要”开始，而应依次回答：通信瓶颈是什么、已有综述缺什么、本文限定什么范围、本文采用什么分类维度。
- 分类图应展示方法改变了通信流程中的哪个变量或环节，而不只是列出算法名称。
- 每个方法小节都保持相同分析模板：问题来源—共同机理—代表性工作—评价指标—适用场景—局限。
- 比较表应使用统一维度，例如通信轮数、累计比特量、端到端时延、能耗、精度代价和系统假设。
- 图前提出需要解释的问题，图后明确图中关系支持了什么判断；图不能代替正文论证。
- 不能复制这些综述的分类图、文字或表格。可以学习其组织原则，再结合本项目证据矩阵原创重绘和改写。
