# 异步耦合粒子系统 · 三层目标—公理—要求体系 v2.2

> **T-PA-G: Three-Layer Goal–Axiom–Requirement System**  
> *for Asynchronous Coupled Particle Multi-Agent Systems*

---

## 🌐 在线可视化 · Live Visualization

> **无需安装、无需部署，直接在浏览器打开即可交互**  
> No installation required — open in any browser, fully interactive

<table>
<thead>
<tr>
  <th>视图 · View</th>
  <th>链接 · Link</th>
  <th>特点 · Feature</th>
</tr>
</thead>
<tbody>
<tr>
  <td>🗂 <strong>三列关系图谱（中文）</strong></td>
  <td><a href="https://tashangkd.github.io/tashan-docs-rule/viz/"><strong>→ 立即打开</strong></a></td>
  <td>T | PA | G 三列固定视口；悬停节点自动高亮 SVG 连线；G 层子要求直接展开可读；点击弹窗显示违反案例 / 数学表达 / 跨域类比</td>
</tr>
<tr>
  <td>⬡ <strong>有向图谱（全节点一屏）</strong></td>
  <td><a href="https://tashangkd.github.io/tashan-docs-rule/viz/viz-graph.html"><strong>→ 立即打开</strong></a></td>
  <td>23 个节点全部在单屏显示，无需滚动；悬浮矩形 + 阴影效果；hover 激活节点放大 + 相关连线逻辑标签浮现；包含层内依赖边（共 58 条有向边）</td>
</tr>
<tr>
  <td>🌐 <strong>English Version</strong></td>
  <td><a href="https://tashangkd.github.io/tashan-docs-rule/viz/viz-en.html"><strong>→ Open</strong></a></td>
  <td>Three-column view with EN as primary language; ZH as secondary; bilingual node cards; same interactive connection lines</td>
</tr>
</tbody>
</table>

> **仓库首页**：[github.com/TashanGKD/tashan-docs-rule](https://github.com/TashanGKD/tashan-docs-rule)

---

## 📋 可视化功能说明

### 三列关系图谱（主视图）

```
┌── T 列（蓝色区域）──┬── PA 列（紫色区域）──┬── G 列（绿色区域，双列）──┐
│  T1 可定义性         │  定义组: PA1 PA5      │  G0 本体结构  G1 合法状态  │
│  T2 合法性           │  边界组: PA2 PA6      │  G2 单步演化  G3 持续稳定  │
│  T3 持续演化         │  生存组: PA3 PA4      │  G4 开放演化  G5 语义耦合  │
│  T4 开放演化         │  进展组: PA8          │  G6 一致追溯  G7 认知连续  │
│  T5 有效耦合         │  耦合组: PA7 PA9      │  G8 工程鲁棒              │
│                      │  ⇄ PA 四对互补对      │  每节点展开 5+ 条子要求   │
└──────────────────────┴───────────────────────┴───────────────────────────┘
          ↑ SVG 连线层：悬停节点时实时高亮相关路径，淡化无关节点
```

**交互方式：**
- **悬停节点** → SVG 连线高亮（T→PA 蓝线，PA→G 紫线），无关节点淡至 20%
- **点击节点** → 弹窗展示：定义说明 / 数学表达式 / ⚠ 违反案例 / 跨域类比（物理·计算机·芯片）
- **展开按钮** → G 层每个节点默认显示前 4 条子要求，"展开剩余 N 条"可查看全部
- **列标题跳转** → 顶栏快速定位到对应层区域

### 有向图谱视图（viz-graph.html）

```
所有 23 个节点（T1–T5, PA1–PA9, G0–G8）一屏可见
节点为悬浮矩形（双语：中文主 + 英文副），有阴影投影效果
共 58 条有向边，分五类：
  ── T 层内部依赖   ── T→PA 公理化   -- PA 互补对（双向）
  ── PA→G 具体化    -- G 层内部依赖
```

**交互方式：**
- **悬停节点** → 相关节点放大 1.1×，无关节点淡至 12%，连线高亮至 88%
- **边标签** → 每条被激活的连线旁显示完整逻辑说明文字
- **右侧信息面板** → 显示悬停节点的全部相关边及其逻辑说明

---

## 📄 核心文档

本仓库包含两份权威规范文档及配套可视化：

| 文档 | 定位 | 回答的问题 |
|---|---|---|
| [`三层目标—公理—要求体系_v2.2.md`](./三层目标—公理—要求体系_v2.2.md) | **规格文档（应然）** | 系统应该成为什么样的系统 |
| [`三层体系元逻辑说明书_v2.md`](./三层体系元逻辑说明书_v2.md) | **逻辑说明书（为何如此）** | 为什么这样分层、如何推导、违反会怎样 |
| [`viz/`](./viz/) | **可视化工具** | 交互式理解三层体系的逻辑结构 |

> v2.2 是**规格文档**（说"是什么"）；元逻辑说明书是**逻辑说明书**（说"为什么这样、怎么推导"）。两者配合使用效果最佳。

---

## 🏗 三层体系速览

```
╔══════════════════════════════════════════════════════════════╗
║  T 层（本质目标层）· 对任何多智能体系统普遍成立，与实现无关    ║
║                                                              ║
║  T1 可定义性 → T2 合法性 → T3 持续演化 → T4 开放演化         ║
║  T1 ─────────────────────────────────── T5 有效耦合           ║
╚══════════════════════════════════════╤═══════════════════════╝
                                       │ 公理化（为保住 T，在结构上必须满足）
╔══════════════════════════════════════╧═══════════════════════╗
║  PA 层（抽象公理层）· T 与 G 之间的桥梁，与实现无关           ║
║                                                              ║
║  [定义组] PA1 存在与可区分    PA5 写权唯一性                  ║
║  [边界组] PA2 有界性          PA6 效应有终局                  ║
║  [生存组] PA3 可恢复性        PA4 持续再进入                  ║
║  [进展组] PA8 语义进展                                        ║
║  [耦合组] PA7 信息可达性      PA9 观察—行动耦合               ║
║                                                              ║
║  四对互补：PA2↔PA3  PA6↔PA7  PA7↔PA9  PA4↔PA8               ║
╚══════════════════════════════════════╤═══════════════════════╝
                                       │ 具体化（在粒子体系架构中如何落地）
╔══════════════════════════════════════╧═══════════════════════╗
║  G 层（当前系统目标层）· 与 world/agents/meta 粒子架构绑定    ║
║                                                              ║
║  串行核心链：G0→G1→G2→G3→G4                                 ║
║  并行目标：  G5 语义有效耦合   G6 一致性与可追溯性            ║
║  LLM特化：  G7 认知连续性                                     ║
║  工程增强：  G8 工程鲁棒性                                     ║
║                                                              ║
║  每个 G 目标下含 4–7 条具体子要求（Gx-Rxxx 编号）             ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 🔑 核心概念一览（中英对照）

| 层级 | 编号 | 中文名 | English |
|------|------|--------|---------|
| T | T1 | 可定义性 | Definability |
| T | T2 | 合法性 | Legality |
| T | T3 | 持续演化 | Continuous Evolution |
| T | T4 | 开放演化 | Open Evolution |
| T | T5 | 有效耦合 | Effective Coupling |
| PA | PA1 | 存在性与主体—环境可区分 | Agent-Environment Distinguishability |
| PA | PA2 | 有界性 | State Boundedness |
| PA | PA3 | 可恢复性 | Resource Recoverability |
| PA | PA4 | 持续再进入 | Guaranteed Rescheduling |
| PA | PA5 | 写权唯一性 | Unique Write Authority |
| PA | PA6 | 效应有终局 | Guaranteed Effect Resolution |
| PA | PA7 | 信息可达性 | Information Reachability |
| PA | PA8 | 语义进展 | Semantic Progression |
| PA | PA9 | 观察—行动耦合 | Observation-Action Coupling |
| G | G0 | 存在性与本体结构 | Ontological Structure |
| G | G1 | 合法状态域（硬不变量）| Legal State Domain |
| G | G2 | 单步演化完备性 | Step Completeness |
| G | G3 | 持续稳定性 | Sustained Stability |
| G | G4 | 开放演化性 | Open Evolution Property |
| G | G5 | 语义有效耦合 | Semantic Effective Coupling |
| G | G6 | 一致性与可追溯性 | Consistency & Traceability |
| G | G7 | 认知连续性 | Cognitive Continuity |
| G | G8 | 工程鲁棒性 | Engineering Robustness |

---

## 📁 文件结构

```
tashan-docs-rule/
├── README.md                              ← 本文件
├── 三层目标—公理—要求体系_v2.2.md          ← 规格文档（权威版本）
├── 三层体系元逻辑说明书_v2.md              ← 逻辑说明书（配套解读）
└── viz/                                   ← 可视化工具目录
    ├── index.html                         ← 三列关系图谱（主入口，中文）
    ├── viz-graph.html                     ← 有向图谱（全节点一屏）
    ├── viz-en.html                        ← 英文版三列图谱
    ├── data.js                            ← 共用数据层（节点/边/英文名/子要求）
    ├── viz1-flow.js                       ← 备选视图：三列流式图
    ├── viz2-neural.js                     ← 备选视图：神经网络式
    ├── viz3-radial.js                     ← 备选视图：径向同心圆
    ├── viz4-tree.js                       ← 备选视图：可折叠树
    ├── viz5-force.js                      ← 备选视图：力导向图
    ├── viz6-matrix.js                     ← PA 互补对 + PA→T 服务矩阵
    ├── viz7-trace.js                      ← G 层依赖矩阵 + 追溯链浏览器
    └── README.md                          ← 可视化子目录说明
```

---

## 📖 文档关系说明

```
三层目标—公理—要求体系_v2.2.md（规格）
    说"是什么"
    ↕ 配合使用
三层体系元逻辑说明书_v2.md（逻辑说明）
    说"为什么这样、怎么推导、违反会怎样"
    ↕ 交互式理解
viz/（可视化工具）
    让任何人无需阅读原文即可直观掌握三层体系的逻辑结构
```

**逻辑推导方向（向下）：**
```
具体要求 Gx-Rxxx
    └→ 归属的 G 目标
        └→ 具体化的 PA 公理
            └→ 服务的 T 目标
```

**裁剪方向（向上）：**  
任何进入 G 层的要求，必须能追溯到至少一条 PA 公理，该公理必须能追溯到至少一个 T 目标。无法追溯者不应进入主干。

---

## 🔗 快速访问

- **可视化主页**：https://tashangkd.github.io/tashan-docs-rule/viz/
- **有向图谱**：https://tashangkd.github.io/tashan-docs-rule/viz/viz-graph.html
- **English View**：https://tashangkd.github.io/tashan-docs-rule/viz/viz-en.html
- **GitHub 仓库**：https://github.com/TashanGKD/tashan-docs-rule

---

*版本：v2.2 · 配套元逻辑说明书 v2 · 可视化工具 v1*
