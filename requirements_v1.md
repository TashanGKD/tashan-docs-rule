# 异步耦合粒子系统 · 目标驱动要求体系（v1）

> 版本：v1.0  
> 日期：2026-03-12  
> 前驱文档：`rule_gpt_0.md`（R-001–R-226）、`goal_gpt.md`（目标树初稿）  
> 核心原则：**先定目标，再立要求**。每条要求的存在必须能被追溯到其服务的目标；无法被追溯的要求不应进入高层。

---

## 前言：为什么要以目标树组织要求

传统做法是将所有要求罗列为平铺的编号列表（R-001、R-002……）。这种方式的问题在于：

- **无法判断轻重**：看不出哪条是"系统不满足就崩溃"的硬约束，哪条是"工程层的优化增强"。
- **无法判断依赖**：看不出缺少某条要求时，哪些其他要求会随之失效。
- **无法判断取舍**：在资源有限时，无法决定先实现哪些、后实现哪些。

**物理学提供了一个清晰的范式**：

- **守恒律（不变量）**：任意时刻必须成立，违反即系统状态非法。
- **稳定性条件**：保证系统不在有限时间内死亡（李雅普诺夫稳定性）。
- **鲁棒性**：在扰动/噪声下仍能维持稳定。

本文档将所有 226 条原始要求，按照类似的目标层级重新定位，并重新编号。

**编号规则**：

| 前缀 | 层级 | 含义 |
|---|---|---|
| `Gm-Rxxx` | 元原则 | 裁剪判准（设计哲学，非系统性质）|
| `G0-Rxxx` | 物理不变量 | 任意时刻必须成立，违反 = 系统状态非法 |
| `G1-Rxxx` | 存在性 | 系统能被形式化定义 |
| `G2-Rxxx` | 单步可行性 | 系统能完成一次完整演化 |
| `G3-Rxxx` | 长时稳定性 | 系统可无限时间演化 |
| `G4-Rxxx` | 功能正确性 | 系统按预期语义工作 |
| `G5-Rxxx` | 可追溯性 | 系统状态可重建、可审计、可恢复 |
| `G6-Rxxx` | 工程鲁棒性 | 在真实计算机环境下不失控 |
| `Gf-Rxxx` | 后续优化方向 | 当前可后置，未来应实现 |
| `Gd-Rxxx` | 文档规范元要求 | 关于文档本身写法的元规范 |

每条要求的格式：

```
Gx-Rxxx  [简称]  要求正文
         次目标：Gy [若有]
         原编号：R-xxx
```

---

## 第一章：目标分级树总览

### 1.1 目标树结构

```
Gₘ  裁剪元原则（Meta-Principle）
    ↓ "不服务任何目标的概念不进入高层"
G0  物理不变量（Hard Invariants）
    ↓ "任意时刻必须成立，否则系统非法"
G1  存在性（Existence）
    ↓ "系统能被形式化定义"
G2  单步可行性（One-step Liveness）
    ↓ "系统能完整跑一轮"
G3  长时稳定性（Asymptotic Stability）
    ↓ "系统在理想条件下可无限时间演化"
G4  功能正确性（Functional Correctness）   ←─→  G5  可追溯性（Auditability）
    ↓ "系统按预期语义工作"                          ↓ "状态可重建、可审计"
G6  工程鲁棒性（Engineering Robustness）
    "在非理想计算机环境下不失控"
```

**注意**：G4 与 G5 是**并行关系**（非严格顺序依赖）：系统可以无限演化（G3）且功能正确（G4）但不可追溯（G5）。两者共同支撑 G6 的崩溃恢复。

### 1.2 各层"回答的问题"

| 层级 | 回答的核心问题 | 缺失后果 |
|---|---|---|
| **Gₘ** | 这个概念/规则值得存在吗？ | 系统臃肿，高层被工程补丁污染 |
| **G0** | 系统在任意时刻的状态合法吗？ | 系统状态非法，不可形式化定义 |
| **G1** | 系统能被形式化描述吗？ | 系统根本没有定义 |
| **G2** | 系统能完整跑一次演化吗？ | 系统一轮都跑不完 |
| **G3** | 系统能永远跑下去吗？ | 系统跑几轮就死 |
| **G4** | 系统的行为是我们想要的吗？ | 系统虽然活着，但行为无效 |
| **G5** | 系统能被解释、检查、恢复吗？ | 系统不可调试、崩溃后不可恢复 |
| **G6** | 系统在工程环境中能稳定运行吗？ | 理论成立，但工程实现不稳 |

### 1.3 要求与目标的挂载规则

每条要求都标注：
- **主目标**：该要求主要服务哪个目标（如缺失，该目标首先失效）
- **次目标**：该要求顺带支持哪些其他目标
- **层级**：硬要求（不可删除）/ 增强项（可选但推荐）/ 禁止项（明确禁止某行为）

---

## 第二章：各层目标的详细要求

---

### 第一节：Gₘ — 裁剪元原则

> **定义**：这不是一个系统性质，而是一个**设计判准**。  
> 任何概念、维度或规则，如果删掉之后不破坏 G0–G5 中的任何目标，则它不应进入高层理论。

**Gm-R001**  [存在理由判准]  
对任何进入高层的概念、对象或规则，必须能给出它直接服务 G0–G5 中哪个目标的理由；若无法给出，该概念不应占据高层位置。  
层级：**判准（最高）**  
原编号：R-186

**Gm-R002**  [维度必须有行为影响]  
任何进入高层的 Field 维度，必须至少影响以下之一：输入门控、输出约束、状态更新、通知优先级、调度策略、生命周期闭合。  
任何进入高层的 Activity 维度，必须至少影响以下之一：输入门控、输出带宽、打断容忍度、能量动力学、切换能力、调度策略。  
否则该维度不应进入第一性原理层。  
层级：**判准**  
原编号：R-075、R-076、R-188

**Gm-R003**  [工程层不混入理想主干]  
工程补丁（Gm-R003 所指的 G6 级机制）不应与理想闭环的硬要求混写在同一层级。删掉工程补丁后，理想闭环的逻辑结构不应坍塌。  
层级：**判准**  
原编号：R-208

**Gm-R004**  [优先增加维度而非补丁]  
当需要表达复杂性时，优先通过增加参数维度解决，而不是叠加越来越多的 if-else 补丁规则。  
层级：**设计原则**  
原编号：R-209

---

### 第二节：G0 — 物理不变量（Hard Invariants）

> **定义**：这些性质在系统的**任意时刻、任意演化步骤后**都必须成立。  
> 违反任何一条 → 系统进入非法状态，相当于物理守恒律被破坏。  
> 这一层的要求**不依赖工程条件**，在理想系统中也必须成立。

#### G0-A：写隔离不变量

**G0-R001**  [写隔离：跨粒子禁止直写]  
任何粒子不能直接写入另一粒子的本体变量集（V_P）。跨粒子影响只能通过"发射事件 → 目标方的 R_P^apply 接收 → 目标方自己写回 V_P"的路径实现。  
层级：**硬要求**  
次目标：G1（存在性边界定义）、G5（审计边界定义）  
原编号：R-109、R-110

**G0-R002**  [本体写权限]  
V_P 只能由粒子自身或授权的系统外力（scheduler-originated / system-maintenance / system-physics 三类事件）写入。  
层级：**硬要求**  
次目标：G1  
原编号：R-003

**G0-R003**  [View 不持有新信息]  
View_P(observer) 是对 V_P 的可见投影，不持有任何新信息，不独立存储。View_P 的值随 V_P 实时派生，不是第二真源。  
层级：**硬要求**  
次目标：G5  
原编号：R-004

**G0-R004**  [世界粒子禁止直写 agent 状态]  
世界粒子 A 不能直接修改任何智能体粒子的本体变量。（G0-R001 的特化实例）  
层级：**硬要求**  
原编号：R-043

#### G0-B：注意力基线不变量

**G0-R005**  [基线不被场/活动污染]  
`baseline_attention_policy` 是 agent 的绝对人格基线。场进入、活动切换、系统周期性调用均不得通过 `R_B^apply` 修改此字段。只有 LLM 通过 `Output.control_delta.attention_policy` 或用户显式操作才可修改。  
层级：**硬要求**  
次目标：G3（防止调度恢复能力被永久污染）  
原编号：R-140、R-141

**G0-R006**  [有效门槛不写回基线]  
运行时有效注意力阈值由基线与场/活动联合计算，结果只在本轮生效，不写回 `baseline_attention_policy`。  
层级：**硬要求**  
次目标：G4  
原编号：R-142

#### G0-C：能量范围不变量

**G0-R007**  [能量有界]  
任意时刻、任意演化步骤后：`energy ∈ [0, 100]`。所有 energy 更新（系统物理规则 + LLM 提议）之后都必须执行 clamp。  
层级：**硬要求**  
次目标：G3（能量恢复路径的前提）  
原编号：R-131、R-132

#### G0-D：前景不变量

**G0-R008**  [单前景场假设]  
在 v1 体系下，任意时刻只有一个栈顶前景场是生效前景。其他场的事件只能通过 notification / external input 路径进入。ForegroundStack 的引入不改变此语义，只增加返回路径。  
层级：**硬要求**  
次目标：G1  
原编号：R-119、R-120、R-122

**G0-R009**  [前景切换只能通过栈操作]  
前景切换只能通过 ForegroundStack 的 push/pop 操作实现。直接赋值 durable `foreground_field_id` 字段是禁止操作。  
层级：**禁止项**  
原编号：R-123、R-124

#### G0-E：通知终局不变量

**G0-R010**  [通知必须有终局]  
每条 Notification 对象必须最终进入以下终态之一：`consumed / expired / merged / archived`（或等价语义）。不允许存在无 TTL 的永久 pending 通知。  
层级：**硬要求**  
次目标：G3（通知空间有界的前提）  
原编号：R-154、R-157

**G0-R011**  [surfaced ≠ acknowledged]  
通知被注入到某次 assemble（surfaced）不等于 agent 已显式确认处理（acknowledged）。两者是系统中不同的状态，不可合并。  
层级：**硬要求**  
次目标：G4  
原编号：R-161

#### G0-F：唯一真源不变量

**G0-R012**  [Global Event Log 为 append-only 唯一真源]  
Global Event Log 必须是 append-only 的，且是系统所有 durable 状态变更的唯一真源。任何对 Log 的删改是非法操作。WritebackLedger 若存在，只是 Event Log 某轮事件的细粒度展开，不是第二真源。  
层级：**硬要求**  
次目标：G5（审计依赖此性质）  
原编号：R-172、R-173、R-175、R-176

---

### 第三节：G1 — 存在性（Existence）

> **定义**：系统必须能被形式化定义和描述。这一层回答"系统有没有"，而不是"系统能不能跑"。

#### G1-A：粒子系统基本结构

**G1-R001**  [系统由粒子构成]  
系统至少由一个世界粒子 `A` 和有限个智能体粒子 `{B₁...Bₙ}` 组成。  
层级：**硬要求**  
原编号：R-001

**G1-R002**  [粒子三元组]  
每个粒子必须满足三元组形式 `P = (V_P, View_P, R_P)`：  
- `V_P`：粒子的本体变量集（真状态）  
- `View_P(observer)`：对 V_P 的可见投影函数，按 observer 决定可见子集  
- `R_P`：演化规则集  
层级：**硬要求**  
次目标：G2（演化依赖此结构）  
原编号：R-002

**G1-R003**  [R_P 细分为四子规则]  
R_P 必须至少细分为：  
- `R_P^assemble`：组装本次演化的输入上下文  
- `R_P^evolve`：从上下文计算输出  
- `R_P^emit`：将输出转化为向外发出的事件序列  
- `R_P^apply`：将事件写回 V_P  
层级：**硬要求**  
次目标：G2  
原编号：R-005

**G1-R004**  [系统级非粒子对象]  
系统应承认存在不属于任何单个粒子、但参与系统前向演化的系统级非粒子对象，包括：`notification_buffer`、`Scheduler`、`Global Event Log`、持久元状态（WritebackLedger、StagingLedger、ResourceLease 等）。  
层级：**硬要求**  
原编号：R-014

#### G1-B：状态空间定义

**G1-R005**  [S_global 与 S_total 的区分]  
系统必须区分两种状态空间：  
- `S_global(t) = V_A(t) × V_B₁(t) × ... × V_Bₙ(t)`（粒子本体真状态空间）  
- `S_total(t) = S_global(t) × notification_buffer(t) × M_meta^persist(t)`（完整前向演化状态空间）  
后者是预测系统下一步是否触发演化的正确输入。  
层级：**硬要求**  
原编号：R-006、R-007、R-008

**G1-R006**  [notification_buffer 的归属]  
`notification_buffer` 不属于任何单个粒子，但属于系统前向演化状态（`S_total` 的一部分）。  
层级：**硬要求**  
原编号：R-009

**G1-R007**  [M_meta^persist 的归属]  
`M_meta^persist`（调度器待处理队列、WritebackLedger、StagingLedger、ResourceLease、活跃 Obligation 集合等）不属于任何单个粒子，但属于系统前向演化状态。  
层级：**硬要求**  
原编号：R-010

#### G1-C：存储归属拓扑（world / agents / meta）

**G1-R008**  [三类顶层归属]  
系统所有 durable 持有者应能映射为以下三类顶层归属：  
- `world/`：世界粒子 A 的 durable 真状态  
- `agents/role_i/`：第 i 个智能体粒子的 durable 真状态  
- `meta/`：不属于任何单个粒子、但影响系统下一步演化的系统级对象  
层级：**硬要求**  
原编号：R-015、R-016、R-017、R-018

**G1-R009**  [world/ 最小内容]  
`world/` 至少应包含：`clock`、`natural_state`、`interaction_contexts`。  
层级：**硬要求**  
原编号：R-019

**G1-R010**  [agents/role_i/ 最小内容]  
`agents/role_i/` 至少应包含：`memory`、`control`、`capability`。  
层级：**硬要求**  
原编号：R-020

**G1-R011**  [meta/ 最小内容]  
`meta/` 至少应包含：`notification_buffer`、调度相关持久态（Scheduler.pending_wakeups）。  
`meta/` 应承载 Global Event Log 或其等价唯一真源。  
`meta/` 还应包含：WritebackLedger、StagingLedger、ResourceLease、活跃 Obligation 索引（若存在）。  
层级：**硬要求**  
次目标：G5  
原编号：R-021、R-022、R-029、R-030

**G1-R012**  [各关键概念的 durable 真源位置]  
以下概念的 durable 真源位置已钉死，不得更改：  

| 概念 | durable 真源路径 |
|---|---|
| `FieldProfile` | `world/interaction_contexts/<ctx>/field` |
| `ActivityRuntimeProfile` | `agents/<role>/control/current_activity/profile` |
| `notification_buffer` | `meta/notification_buffer/*` |
| `ForegroundStack` | `agents/<role>/control/foreground_stack` |
| `next_wakeup` | `agents/<role>/control/next_wakeup` |
| `Global Event Log` | `meta/`（不能误写成 agent 私有文件）|
| `WritebackLedger` | `meta/`（不是第二真源）|

层级：**硬要求**  
原编号：R-023–R-029

**G1-R013**  [调度器不写回 durable 状态]  
调度器（Scheduler）持有瞬时运行态，决定哪些粒子何时演化，但不应把瞬时运行态写回任何粒子的 durable 状态。  
层级：**硬要求**  
原编号：R-108

#### G1-D：世界粒子 A 的最小骨架

**G1-R014**  [V_A 最小骨架]  
世界粒子的最小骨架：`V_A = { clock, natural_state, interaction_contexts }`  
- `clock`：必须存在，作为系统唯一时间基底，必须参与世界侧的自主推进或触发逻辑  
- `natural_state`：必须保留为自然基底变量，即使当前建模较轻  
- `interaction_contexts`：必须是世界粒子的直接组成部分，不应独立拆出为第三类本体变量  
层级：**硬要求**  
原编号：R-011、R-013、R-031、R-032、R-033、R-034

**G1-R015**  [InteractionContext 最小结构]  
每个 `InteractionContext` 至少必须持有：`field`（FieldProfile）、`participants`、`messages`。  
层级：**硬要求**  
原编号：R-036

**G1-R016**  [interaction_contexts 是场参数化容器]  
`interaction_contexts[*]` 必须是场参数化的交互容器。场的行为由 FieldProfile 的参数维度驱动，而不是由产品名称（"论坛"/"群聊"）决定。  
层级：**硬要求**  
次目标：G4  
原编号：R-035

**G1-R017**  [共享世界结构]  
系统必须允许"共享世界 + 各 agent 局部耦合通道"的结构，不应把每个 agent 误建成各自拥有独立世界介质本体。  
层级：**硬要求**  
原编号：R-118

#### G1-E：智能体粒子 B 的最小骨架

**G1-R018**  [V_B 最小骨架]  
智能体粒子的最小骨架：`V_B = { memory, control, capability }`  
- `memory`、`control`、`capability` 均属于 durable 真状态，不得被误当作可随时丢弃的缓存  
层级：**硬要求**  
原编号：R-012、R-046、R-047、R-048、R-064

**G1-R019**  [control 的最小必需字段]  
`control` 至少应包含以下字段（缺少任一则系统存在性不完整）：  

| 字段 | 作用 |
|---|---|
| `physical_location` | 物理位置（co-located 场感知）|
| `foreground_stack` | 认知前景栈（替代旧的单值 foreground_field_id）|
| `current_activity` | 当前活动（ActivityInstance，替代旧的裸 activity_profile）|
| `baseline_attention_policy` | 注意力基线 |
| `active_key` | 当前工作上下文键 |
| `next_wakeup` | 下次唤醒时间戳 |
| `last_evolved_at` | 上次演化时间戳（Δt 计算基准）|
| `energy` | 能量值 |

层级：**硬要求**  
原编号：R-049–R-056

**G1-R020**  [旧结构禁止再作为权威 durable 结构]  
以下旧式结构不应再作为权威 durable 结构使用：  
- 旧式单值 `foreground_field_id`（已被 `ForegroundStack` 替代）  
- 旧式裸 `activity_profile`（已被 `ActivityInstance` 统一）  
- `current_object_ref` 作为 ControlState 顶层字段（应并入 `current_activity.object_ref`）  
层级：**禁止项**  
原编号：R-058、R-059、R-063

**G1-R021**  [ActivityInstance 最小结构]  
`current_activity` 应统一为 `ActivityInstance`，至少包含：`preset`（活动预设名称）+ `profile`（ActivityRuntimeProfile）+ `object_ref`（当前工作对象引用）。  
层级：**硬要求**  
原编号：R-060、R-061

**G1-R022**  [active_key 的权威真源]  
`active_key` 的权威真源在 `control.active_key`。`ForegroundFrame.active_key` 是压栈时的历史快照，不是新的独立权威来源。  
层级：**硬要求**  
原编号：R-126、R-127

#### G1-F：FieldProfile 和 ActivityRuntimeProfile 的存储归属

**G1-R023**  [FieldProfile 存储位置]  
`FieldProfile` 必须作为 `interaction_contexts[*]` 的内部变量块承载，不能独立成为顶层本体对象。  
层级：**硬要求**  
次目标：G4  
原编号：R-073

**G1-R024**  [ActivityRuntimeProfile 存储位置]  
`ActivityRuntimeProfile` 必须作为 `current_activity.profile` 的内部变量块承载，不能独立成为顶层本体对象。  
层级：**硬要求**  
次目标：G4  
原编号：R-074

---

### 第四节：G2 — 单步可行性（One-step Liveness）

> **定义**：系统能完整走完一次演化的四个阶段，并产生合法的下一状态。  
> 这是"系统能跑起来"的最低门槛——连一轮都跑不完，谈长时稳定性没有意义。

**G2-R001**  [四阶段演化必须完整]  
每次粒子演化必须经过完整的四阶段：  
```
assemble → evolve → emit → apply
```
任何跳过某阶段的实现都是非法的。  
层级：**硬要求**  
原编号：R-081

**G2-R002**  [assemble：合法上下文组装]  
`assemble` 必须能组装本轮演化可见的上下文，至少包括：本体状态（V_P）、必要的可见上下文（通过 View_Q(P) 过滤）、系统级待处理输入（notification_buffer 中满足注入条件的通知）。  
层级：**硬要求**  
原编号：R-082、R-089

**G2-R003**  [evolve：产生合法输出]  
`evolve` 必须能从上下文得到动作提议（action_proposals）与状态更新提议（control_delta 等）。  
- 世界粒子 A 的 evolve 可退化为确定性硬编码函数  
- 智能体粒子 B 的 evolve 通常由 LLM 或等价决策器承担  
层级：**硬要求**  
原编号：R-083、R-086、R-087

**G2-R004**  [emit：事件路由合法性]  
`emit` 必须把输出转化为事件序列，通过事件路由影响目标粒子。禁止通过 emit 直接跨粒子写状态（G0-R001 的行为层对应）。  
层级：**硬要求**  
次目标：G0  
原编号：R-084、R-090

**G2-R005**  [apply：写回合法状态]  
`apply` 必须把事件写回粒子自身的本体变量。R_A^apply 必须能接收来自 agent 的事件并更新 `interaction_contexts`；更新后，必须能向 `notification_buffer` 路由后续影响。  
层级：**硬要求**  
次目标：G4  
原编号：R-085、R-041、R-042

**G2-R006**  [无死状态原则]  
演化函数对任意合法状态必须产生合法下一状态，不允许存在"永久停滞"的死状态。  
（工程层中 LLM 幻觉导致的停滞由 G6 级 N-tick 超时逃生处理，不是此要求的范畴。）  
层级：**硬要求**  
次目标：G3  
原编号：R-088

**G2-R007**  [六问判准]  
高层的任意一条演化规则，至少必须能回答以下六问之一：  
到达（事件如何到达粒子）、看见（粒子能看到什么）、中断（如何打断当前演化）、输出（粒子输出什么）、写回（输出如何写入状态）、再调度（下次何时演化）。  
不能回答任何一问的规则不应进入高层。  
层级：**判准**  
次目标：Gₘ  
原编号：R-187

---

### 第五节：G3 — 长时稳定性（Asymptotic Stability）

> **定义**：系统在理想条件下可以无限时间演化，而不会在有限时间内因内部逻辑停止。  
> 这一层的充要条件即"最小无限演化判准"。

#### G3-A：调度链不断

**G3-R001**  [time-driven 调度必须存在]  
系统必须支持 time-driven 调度。对最小无限演化而言，至少 time-driven 触发链不能在任何时刻断裂。  
层级：**硬要求**  
原编号：R-095、R-097

**G3-R002**  [event-driven 调度必须存在]  
系统必须支持 event-driven 调度。  
层级：**硬要求**  
原编号：R-096

**G3-R003**  [next_wakeup 永不为 null]  
任意时刻，任意 agent 的 `next_wakeup` 必须是有效时间戳，不得为 null 或 undefined。  
若本轮 LLM 输出未给出 `next_wakeup`，系统必须按默认策略自动填入。  
层级：**硬要求**（与 G0 的写隔离同等级，是系统稳定链的关键节点）  
次目标：G0（可看作运行时调度不变量）  
原编号：R-098、R-099

#### G3-B：能量有界与恢复路径

**G3-R004**  [能量恢复路径必须存在]  
系统中必须存在至少一种活动预设，使得 `energy_profile = recovering`（即 `Δenergy > 0`）。  
该路径必须有**严格正的恢复速率**，保证 agent 不会永久能量耗竭。  
最小要求：sleeping/resting 类活动必须产生正能量增益。  
层级：**硬要求**  
次目标：G4（能量状态影响功能行为）  
原编号：R-133、R-134

**G3-R005**  [能量动力学模型：场 × 活动 × 时间]  
energy 动力学采用"场 × 活动 × 时间"的 per-hour 模型：  
```
energy(t+Δt) = clamp(energy(t) + fieldEnergyModifier × Δt + activityEnergyModifier × Δt + llmAdjustment, 0, 100)
```  
- `fieldEnergyModifier`：由 FieldProfile 参数决定  
- `activityEnergyModifier`：由 ActivityRuntimeProfile.energy_profile 决定  
- `llmAdjustment`：LLM 提议的微调，必须被 clamp 到有限范围  
旧 v4 的 per-minute 表不应再作为权威主模型。  
层级：**硬要求**  
次目标：G4  
原编号：R-135、R-136、R-137、R-138、R-139

#### G3-C：记忆有界

**G3-R006**  [memory 必须有界]  
Memory Store 必须是有界的，必须支持压缩/遗忘/分层检索机制，确保 context window 不会因记忆无限增长而溢出。  
层级：**硬要求**  
原编号：R-143、R-144

**G3-R007**  [禁止全量注入 memory]  
不能将所有记忆全量无条件注入到 assemble 上下文。最小可接受实现：tiered memory + retrievable access（分层记忆 + 按需检索）。  
层级：**禁止项**  
原编号：R-145、R-146

#### G3-D：通知空间有界

**G3-R008**  [notification_buffer 必须有界]  
notification_buffer 必须是有界的，必须有 TTL 清理机制，确保通知队列不无限积压。  
层级：**硬要求**  
次目标：G0（与 G0-R010 联合保证终局）  
原编号：R-153

**G3-R009**  [通知终局最小实现]  
最小终局实现必须支持 `consumed / expired`（或等价语义）。  
推荐扩展终局：`merged`（collapse_key 去重）、`archived`（正常归档）。  
层级：**硬要求**  
原编号：R-155、R-156

**G3-R010**  [通知必须支持 TTL]  
每条通知应支持 `ttl_sec` 字段，到期后系统自动迁移至 expired 状态。`ack_required` 类通知若超过 deadline 且未 acknowledged，必须有后继迁移路径（如 expired 或 escalation）。  
层级：**硬要求**  
原编号：R-158、R-162

#### G3-E：上下文可关闭

**G3-R011**  [bounded/ephemeral context 可关闭]  
`lifecycle=bounded` 或 `lifecycle=ephemeral` 的 InteractionContext 不能只增不减。系统必须存在明确的关闭路径。  
- `ephemeral`：成员散尽或空闲超时关闭  
- `bounded`：有截止/结论/显式关闭语义  
- `persistent`：手动关闭  
层级：**硬要求**  
次目标：G4  
原编号：R-163

#### G3-F：最小无限演化判准汇总

**G3-R012**  [最小无限演化充要条件]  
系统在理想条件下能无限时间演化，当且仅当同时满足以下所有条件：  
1. `energy` 有界且存在严格正恢复路径（G0-R007 + G3-R004）  
2. `memory` 有界且有遗忘机制（G3-R006）  
3. 每条通知必须有终局（G0-R010 + G3-R008）  
4. `next_wakeup` 任意时刻不为 null（G3-R003）  
5. 演化函数无死状态（G2-R006）  
层级：**判准**  
原编号：R-184、R-185、R-189

**G3-R013**  [最小闭环核必须包含的最小集合]  
最小闭环核必须包含：粒子三元组、S_total 定义、写隔离、四阶段演化、再进入机制（next_wakeup）、唯一真源（Global Event Log）、energy bounded、memory bounded、notification terminal。  
当前额外必要组成：单前景场假设、P0 生存规则（energy=0 时强制切 recovering）、Field × Activity 组合驱动行为。  
层级：**判准**  
原编号：R-189、R-190

**G3-R014**  [稳定性破坏的两个典型模式]  
以下两种情况表明系统不满足 G3：  
1. 系统因 context/通知/记忆无限积压而在有限时间内失效  
2. 系统因 `baseline_attention_policy` 被场/活动永久污染而失去调度恢复能力（注：第二点与 G0-R005 联合保证）  
层级：**验证判准**  
原编号：R-191、R-192

---

### 第六节：G4 — 功能正确性（Functional Correctness）

> **定义**：系统不仅"活着"且能"跑一轮"，还要按预期语义运转。  
> 这一层决定系统的行为是否真正有效，而不仅仅是形式上合法。

#### G4-Ⅰ：Field 与 Activity 的分离建模

**G4-R001**  [Field 与 Activity 必须分开建模]  
`Field` 表示**外部交互环境/上下文结构**（场是外在的，不依赖主体当前在做什么）。  
`Activity` 表示**主体当前在做什么/以何种方式耦合环境**（活动是主体内在的认知-行为状态）。  
两者必须分开建模，不能合并。  
层级：**硬要求**  
原编号：R-065、R-066、R-067

**G4-R002**  [运行时行为由三者共同决定]  
系统的运行时行为必须由 `field_profile × activity_profile × agent_state` 三者共同决定，而不是任意两者的子集。  
层级：**硬要求**  
原编号：R-068

**G4-R003**  [FieldProfile 与 ActivityRuntimeProfile 是 runtime projection]  
`FieldProfile` 只是完整 Field 本体的 runtime projection（运行时投影），不能被误写成完整 Field 本体。  
`ActivityRuntimeProfile` 只是完整 Activity 本体的 runtime projection，不能被误写成完整 Activity 本体。  
层级：**禁止项**  
原编号：R-069、R-070、R-071、R-072

**G4-R004**  [FieldProfile 最小维度集]  
`FieldProfile` 当前最小权威维度集为 8 维：  
`arity / co_presence / synchrony / lifecycle / task_binding / visibility / attention_impact / normative_force`  
层级：**硬要求**  
原编号：R-077

**G4-R005**  [ActivityRuntimeProfile 最小维度集]  
`ActivityRuntimeProfile` 当前最小权威维度集为 7 维：  
`mode / medium / input_openness / output_bandwidth / interrupt_tolerance / energy_profile / mobility`  
层级：**硬要求**  
原编号：R-078

**G4-R006**  [按场参数建模，不按产品名称建模]  
系统不应优先按"论坛/群聊/chat/topic"等产品名称建模，而应优先按场参数（FieldProfile 的维度组合）建模。具体产品形态通过少数通用函数 + `field_profile` 参数化生成。  
层级：**设计原则**  
原编号：R-079、R-080

**G4-R007**  [RuntimeEnvelope 桥接函数]  
系统必须存在将 `Field × Activity × ControlState` 闭合为运行时门控对象的桥接函数（RuntimeEnvelope 或等价物），至少输出：  
- 感知注入结果（哪些事件可以注入本轮上下文）  
- 允许动作集（当前合法的动作类型）  
- 状态增量建议（energy delta、next_wakeup 建议等）  
- 下次唤醒建议  
层级：**硬要求**  
原编号：R-093、R-094

**G4-R008**  [统一函数原则]  
世界侧与主体侧都应采用尽量少数的统一函数，而非为每种产品类型单写规则。推荐至少保留的统一函数：  
`visibleSlice / priorityOf / canInject / canWakeup / defaultAttention / defaultActiveKey / closeCondition / allowedActions`  
层级：**设计原则**  
原编号：R-091、R-092

#### G4-Ⅱ：感知正确性（Perception Correctness）

**G4-R009**  [local/external 阈值必须区分]  
来自当前前景场内部的事件（local）与来自其他场的事件（external）必须使用不同的注入门槛（canInject）和唤醒门槛（canWakeup）。禁止对所有来源使用相同门槛。  
前景场内部事件应具备更低的注入/唤醒门槛（优先处理当前工作场的信号）。  
层级：**硬要求**  
原编号：R-100、R-101、R-102

**G4-R010**  [生命威胁强制唤醒]  
对 `semantic_class ∈ {hazard, evacuation, emergency}` 的通知，系统必须存在强制唤醒覆盖通道，无视当前所有注意力门槛（包括 sleeping 保护期）。  
层级：**硬要求**  
原编号：R-103

**G4-R011**  [用户直接输入是高权限路径]  
用户直接输入应作为特殊高权限触发路径，允许绕过常规注意力门槛，立即触发 agent 演化。  
层级：**硬要求**  
原编号：R-104

**G4-R012**  [next_wakeup 默认值受多因素影响]  
`next_wakeup` 的默认推荐值应受以下因素影响：  
- 活动模式（sleeping/discussing+live/writing 等）  
- 场类型（live+mission_locked 场缩短；async+casual 场放宽）  
- 当前 energy（energy 低时拉长 wakeup 间隔）  
具体数值属于 L3 策略层，可配置。  
层级：**硬要求**  
原编号：R-105、R-106、R-107

**G4-R013**  [View_P 观察者域与访问差异]  
`View_P(observer)` 的 observer 域至少应包括：其他粒子、被授权的系统元设施、外部用户。  
不同的 observer 应适用不同的访问规则。  
层级：**硬要求**  
原编号：R-111、R-112

**G4-R014**  [View_A(Bᵢ) 基于 field 决定]  
世界粒子的可见投影 `View_A(Bᵢ)` 必须基于 `interaction_contexts` 及其 `field` 参数来决定每个 agent 能看到什么。  
层级：**硬要求**  
原编号：R-044

**G4-R015**  [Memory 的 source_field_id 隔离]  
每条 `MemoryEntry` 应强制携带 `source_field_id`（产生该记忆时的前景场 id）。  
- `source_field_id` 必须由系统在 commitWriteEvent 时自动注入，不允许 LLM 自由覆写  
- `assembleMemory` 时应优先检索同源记忆（source_field_id 与当前前景场匹配）  
- 跨场记忆进入必须满足严格语义阈值（当前讨论过的典型值：cross_context_relevance ≥ 0.85，且条数有上限）  
层级：**硬要求**  
次目标：G5（记忆域隔离防止认知污染）  
原编号：R-147、R-148、R-149、R-150

**G4-R016**  [mood 在 v1 阶段不参与硬决策]  
`mood` 当前可作为弱闭环变量存在（影响 agent 输出风格等），但在 v1 阶段不应参与 `canInject / canWakeup / effective_actions` 的硬决策。  
层级：**约束**（v1 阶段）  
原编号：R-151、R-152

#### G4-Ⅲ：动作正确性（Action Correctness）

**G4-R017**  [动作可达域由场与活动共同决定]  
agent 在某时刻的有效动作集（effective_actions）应由以下联合约束：  
```
effective_actions = 
  (allowedActions(foreground_field) ∪ allowedActions(physical_location_field))
  ∩ actionsAffordedByMedium(current_activity)
  ∩ actionsAllowedByBandwidth(current_activity)
  ∩ actionsAllowedByMobility(current_activity)
  ∩ actionsSupportedByCapability(agent)
```  
层级：**硬要求**  
原编号：R-113、R-114

**G4-R018**  [低头族悖论：物理场动作不可忽略]  
不能因为当前认知前景在数字场，就完全忽略物理所在场的动作可达域。  
物理现场点名/面向面的强局部信号，应拥有比一般外部事件更高或更特殊的处理路径。  
层级：**硬要求**  
原编号：R-115、R-116

**G4-R019**  [co-located 场必须使用 place_id]  
对 `co_presence = co_located` 的场，`place_id` 必须进入可见性与动作合法性判断。  
层级：**硬要求**  
原编号：R-039、R-117

**G4-R020**  [LLM 只能输出 activity preset 名称]  
LLM 不能直接输出完整 `ActivityInstance` JSON 或完整 `ActivityRuntimeProfile`。  
LLM 只能输出活动 preset 名称（字符串），由系统负责展开为完整 `ActivityInstance`。  
自定义活动若存在，必须经过合法性校验后才能写回。  
层级：**禁止项**  
原编号：R-128、R-129、R-130

#### G4-Ⅳ：规范性正确性（Normative Correctness）

**G4-R021**  [context 扩展字段按场类型]  
- 对 `lifecycle=bounded` 或 `task_binding≥strong` 的场：`InteractionContext` 应能持有 `agenda / conclusion / status / deadline` 等任务相关变量  
- 对 `normative_force≥formal` 的场：应能持有 `roles / obligations`  
- 可选扩展（非最小核必需）：`files / org_memory / metadata`  
层级：**硬要求**  
原编号：R-037、R-038、R-040

**G4-R022**  [closeCondition 必须存在]  
`closeCondition(field, contextState)` 函数必须存在，并按以下语义执行：  
- `ephemeral`：物理成员全部离场 OR 空闲超时关闭  
- `bounded`：满足 agenda 全完成 / deadline 到达 / 主持人显式关闭等条件  
- `persistent`：手动关闭  
层级：**硬要求**  
原编号：R-164、R-165、R-166、R-045

**G4-R023**  [义务系统要求]  
对 `normative_force=binding` 或 `task_binding=mission_locked` 的场：  
- 系统应能持有并暴露 Obligation 对象  
- agent 自身的 active/accepted/proposed Obligation 必须在 assemble 时全量注入，不得因 context window 限制被截断  
- Obligation 必须有正式状态机（不少于 5 态），不能只用松散布尔值  
- 创建义务时应避免 `blocking_on` 形成循环依赖  
层级：**硬要求**  
原编号：R-167、R-168、R-169、R-170

**G4-R024**  [Obligation + Agenda + Deliverable 支持强任务 session]  
义务、议程、deliverable 的组合，至少要能支持"强任务 session"的完整闭环：任务分配 → 执行 → 完成/取消 → 场关闭。  
层级：**硬要求**  
原编号：R-171

**G4-R025**  [ContextClosedEvent 必须触发前景帧 pop]  
`ContextClosedEvent` 广播后，所有 ForegroundStack 中引用该 `field_id` 的帧都应被 pop，并触发返回逻辑（不直接写 agent 的本体变量，通过通知触发 agent 自己 pop）。  
层级：**硬要求**  
原编号：R-125

**G4-R026**  [世界粒子必须支持多种生命周期语义]  
世界粒子必须支持对 `ephemeral / bounded / persistent` 三类生命周期 context 的关闭或归档语义，包括消息分层存储（hot/warm/cold）和结论生成（bounded 场）。  
层级：**硬要求**  
原编号：R-045

#### G4-Ⅴ：可见性与通知语义

**G4-R027**  [通知 semantic_class]  
通知应支持 `semantic_class` 字段，区分：ambient / mention / direct / alarm / reactive_local / hazard / evacuation / emergency 等类别，用于优先级计算和强制唤醒路径。  
层级：**硬要求**  
原编号：R-159

**G4-R028**  [collapse_key 去重机制]  
对可以合并的通知，应支持 `collapse_key` 或等价去重机制，防止通知爆炸（同一场大量消息导致通知队列无限增长）。  
层级：**增强项**  
原编号：R-160

**G4-R029**  [ActivityInstance 可扩展字段]  
`ActivityInstance` 可进一步包含：`toolset / writeback_policy / reservation_until / resume_token` 等扩展字段（不是最小核必需，但推荐实现）。  
层级：**增强项**  
原编号：R-062

**G4-R030**  [mood 作为弱闭环变量]  
`mood` 当前可作为弱闭环变量（valence × activation 二维结构）存在，影响 agent 的输出风格和长期行为倾向，但不进入调度或动作硬决策（见 G4-R016）。  
层级：**增强项**  
原编号：R-057、R-151

---

### 第七节：G5 — 可追溯性（Auditability）

> **定义**：系统状态变更必须能被重建、审计、重放。  
> 这一层与 G4 是**并行关系**（非严格顺序依赖），但支撑 G6 中的崩溃恢复机制。

**G5-R001**  [所有 durable 变更必须产生可重放事件记录]  
所有 durable 状态变更最终都必须产生可重放的事件记录，写入 Global Event Log。系统状态必须能从 Event Log 完整重建。  
层级：**硬要求**  
次目标：G0（Event Log 唯一真源是 G0 不变量）  
原编号：R-174

**G5-R002**  [StagingLedger 是暂存区，非真状态]  
`StagingLedger`（PendingIntent 暂存）若存在，只能作为提交前的暂存区（在 ActionReceipt 到来前持久化 LLM 推理意图），不应被解释为 durable 真状态。  
层级：**硬要求**  
原编号：R-177

**G5-R003**  [审计视图是派生，非独立本体]  
审计视图（如"某 agent 今日的所有动作"）应被理解为 Global Event Log 的派生查询结果，而不是额外的 durable 本体。不要求每个派生投影都实时持久化；只要保证"能重建"，最弱形式的可追溯即成立。  
层级：**硬要求**  
原编号：R-178、R-179

**G5-R004**  [因果顺序不依赖 wall clock]  
若使用因果顺序机制，WriteEvent 的应用顺序应由 `causal_parent_ids`（逻辑时钟）决定，而不是 `created_at`（wall clock）。  
`created_at` 更适合用于展示和 TTL 计算，不用于因果顺序的权威来源。  
层级：**硬要求**  
次目标：G6（防断网重连后事件乱序）  
原编号：R-180、R-181

**G5-R005**  [durable 写回先写事件再物化]  
任何影响 durable 状态的写回，原则上应先写 WriteEvent（包含 idempotency_key），再物化状态。  
这保证崩溃恢复时可以从 WriteEvent 日志 replay，且幂等性保证多次 replay 不产生副作用。  
层级：**硬要求**  
次目标：G6  
原编号：R-182

**G5-R006**  [LLM 等 ActionReceipt 再提交 durable 写回]  
LLM 不应在动作发出的同时假设成功并立即把后果写回记忆（Split-Brain 问题）。  
若系统有 `ActionReceipt` 语义，LLM 必须等到 ActionReceipt 确认后才提交 durable 写回。  
推荐实现：先将推理意图持久化到 StagingLedger，等 ActionReceipt 后正式提交 WriteEvent。  
层级：**硬要求**  
次目标：G6  
原编号：R-183

---

### 第八节：G6 — 工程鲁棒性（Engineering Robustness）

> **定义**：在真实计算机系统的有限资源和故障环境中，系统不因数值问题、并发、掉线、分布式异常而失控。  
> **重要原则**：工程补丁不修改 G0–G5 的定义，只是实现层的防护性代码。删掉后理想闭环的逻辑结构未必立刻坍塌，但实现层更容易出现抖动、漂移、double-write 或崩溃。

**G6-R001**  [busy-loop 防护]  
`next_wakeup ≤ now` 时不能进入忙等。推荐机制：`MIN_WAKEUP_INTERVAL`（最小唤醒间隔，建议 60s）保证 `next_wakeup = max(computed, now + MIN_WAKEUP_INTERVAL_SEC)`。  
原编号：R-193、R-200

**G6-R002**  [crash recovery 语义]  
系统崩溃重启后，必须能从 WritebackLedger replay 未物化的 WriteEvent，恢复到崩溃前的 durable 状态。  
推荐：重启时对所有过期的 `next_wakeup` 进行 jitter 重置（防唤醒风暴）。  
原编号：R-194

**G6-R003**  [split-brain 防护]  
防止"记忆说动作成功了，世界说没成功"的不一致状态。通过 StagingLedger + ActionReceipt 状态机实现（G5-R006 的工程保障）。  
原编号：R-195

**G6-R004**  [lease / queue / cleanup 机制]  
排他性资源（发言权、主持权等）应通过 ResourceLease 管理（token fence + Sweeper 定期清理）。  
大量 agent 并发争抢同一任务时，应支持队列化认领（AgendaItem claim_queue）防止乐观锁饥饿活锁。  
原编号：R-196、R-205

**G6-R005**  [overload / 降载策略]  
大规模运行时应存在降载策略（overload_mode: normal / degraded / shed），在系统算力不足时有序降级，优先保证 urgent 级事件处理。  
原编号：R-197

**G6-R006**  [Hysteresis Lock（能量迟滞锁）]  
防止 energy 在阈值附近产生高频微震荡（consuming→resting→consuming 无限循环）。  
当 `energy ≤ 0` 时激活 `energy_recovery_lock`，强制切换 recovering 活动；满足解锁双条件（energy ≥ SAFE_ENERGY 或 连续 N 小时 energy ≥ CRITICAL_ENERGY）后解锁。  
原编号：R-198

**G6-R007**  [极端 Δt 截断（MAX_DELTA_T）]  
`Δt = clamp(max(0, now - last_evolved_at), 0, MAX_DELTA_T_HOURS)`  
防止系统离线后重连时 Δt 过大导致 energy 语义失真。推荐值：72h（可配置）。  
实现层使用 monotonic clock 计算 Δt，wall clock 只用于人类可读时间戳。  
原编号：R-199

**G6-R008**  [多节点时钟偏差容忍]  
多节点部署时，节点间时间差 < `CLOCK_SKEW_TOLERANCE`（推荐 5s）视为同时发生，超过则发 `clock_skew_warning`，不自动修正数据。  
原编号：R-201

**G6-R009**  [N-tick 超时逃生]  
对前景场长期无有效进展（LLM 幻觉或 Obligation 循环依赖），调度器应有定时检测：  
- 软超时（N tick 无进展）：注入 urgent 系统告警，agent 可选择 pop 当前帧  
- 严格超时（2N tick）：强制解绑  
有效进展的定义由 PROGRESS_ACTIONS 白名单决定（submit_deliverable / update_agenda / satisfy_obligation 等），普通 send_message 不算有效进展。  
原编号：R-202

**G6-R010**  [sleep_debt 建模]  
用于在生命威胁覆盖（G4-R010 中的 hazard/evacuation/emergency 强制唤醒）后，积累透支惩罚（sleep_debt_hours += 8），影响下次睡眠目标计算，模拟生理恢复成本。  
原编号：R-203

**G6-R011**  [wakeup 不应期（refractory period）]  
`wakeup_refractory_until` 可用于防止 agent 在短时间内被过度频繁唤醒（唤醒风暴）。冷却期内非 P0 级别的唤醒请求被拒绝。  
原编号：R-204

**G6-R012**  [因果拓扑排序（causal_parent_ids）]  
WriteEvent 的应用顺序由 `causal_parent_ids` 决定，使用 Kahn 算法拓扑排序，防止断网重连后批量提交的 Event 乱序导致因果颠倒。  
原编号：R-206

**G6-R013**  [Notification Sweeper]  
`notification_buffer` 需要定期清理（Sweeper），将过期（TTL 到期）、已归档的通知从队列中移除，保证 notification_buffer 空间有界（对应 G3-R008 的工程实现）。  
原编号：R-207

---

## 第三章：后续优化方向（Gf — Future，当前可后置）

> 这些方向是我们反复认为值得实现的，但目前可后置到 v2 或更后的版本。  
> 后置意味着：缺少这些，v1 系统仍满足 G0–G6 的要求。

**Gf-R001**  [attention_impact 维度拆分]  
`attention_impact` 后续宜拆为两个独立维度：  
- `cognitive_load`：认知负荷程度（影响 agent 的输入处理能力）  
- `external_shield`：外界屏蔽强度（影响外部事件的注入门槛）  
原编号：R-210

**Gf-R002**  [task_binding 维度拆分]  
`task_binding` 后续宜拆为：  
- `purpose_binding`：目的绑定强度  
- `deliverable_binding`：产出物绑定强度  
- `exit_constraint`：退出约束强度  
原编号：R-211

**Gf-R003**  [mobility 维度拆分]  
`mobility` 后续宜拆为：  
- `physical_mobility`：物理移动自由度  
- `context_switchability`：认知场切换容忍度  
原编号：R-212

**Gf-R004**  [显式 power_structure / permission_model]  
系统后续宜补充显式的权力结构和权限模型建模，超出当前 roles + allowedActions 的粗粒度表达。  
原编号：R-213

**Gf-R005**  [显式 resource_pressure / exclusivity]  
系统后续宜补充显式的资源压力和排他性建模，超出当前 ResourceLease 的粗粒度表达。  
原编号：R-214

**Gf-R006**  [mood 从弱闭环升为强闭环]  
`mood` 后续宜从弱闭环变量（仅影响输出风格）升级为参与 `canInject / canWakeup / effective_actions` 等硬决策的强闭环变量。  
原编号：R-215

**Gf-R007**  [物理世界边界用新本体类型表达]  
自然灾害、身体约束、生命安全级撤离等物理世界边界事件，后续宜引入新的本体类型来表达，而不是只靠工程补丁（如 Life Threat Override 是当前的补丁级处理）。  
原编号：R-216

**Gf-R008**  [耦合介质 M 的引入需明确为版本体重构]  
如果未来引入"耦合介质 M"（如当前 v6 中的 C 粒子）作为第三类本体实体，必须明确声明：这属于新版本体重构（如 v7），而不是对当前 v1 权威结构的直接解释或兼容扩展。  
原编号：R-217

---

## 第四章：文档规范元要求（Gd — Document）

> 关于主文档本身写法的元规范。满足这些要求的文档才能清晰表达系统设计意图。

**Gd-R001**  [主文档按 durable 持有者组织]  
主文档应优先按 durable 持有者（world / agents / meta）组织，而不是按产品类型或历史演化顺序组织。  
`Field` 作为 `V_A.interaction_contexts[*]` 的内部变量块；`Activity` 作为 `V_B.control.current_activity.profile` 的内部变量块。  
原编号：R-218、R-219、R-220

**Gd-R002**  [推荐章节顺序]  
主文档推荐的章节组织顺序：  
0. 持有者与目录映射  
1. 本体（粒子与变量）  
2. 演化方程  
3. 约束（不变量 + 稳定性条件）  
4. 目标  
5. 工程补丁  
原编号：R-221

**Gd-R003**  [projection/bridge 的位置]  
若需要讲述 projection / bridge（如 RuntimeEnvelope），更适合放在"演化方程章"的内部小节，而不必另起平行大章。  
原编号：R-222

**Gd-R004**  [兼容别名放附录]  
兼容别名、旧字段名、迁移映射应单独放附录，不应污染正文。  
原编号：R-223

**Gd-R005**  [显式 Source of Truth Table]  
主文档应显式给出 Source of Truth Table，钉死每个关键概念的 durable 真源位置。  
原编号：R-224

**Gd-R006**  [显式区分五类变量]  
主文档应显式区分：  

| 类型 | 定义 |
|---|---|
| 本体变量 | 粒子的独立真状态，只有粒子自身可写 |
| 派生变量 | 由本体变量完全决定，不独立存储，实时计算 |
| 耦合缓冲变量 | 粒子间的中间容器（属于 meta/）|
| 可见投影 | 本体变量经访问规则后的投影函数 |
| 审计投影 | Global Event Log 的派生查询视图，非独立本体 |

原编号：R-225

**Gd-R007**  [文档写法原则]  
文档写法应尽量做到：  
- 概念先归属（属于哪个粒子/哪个层级），再谈行为  
- 先 durable（真状态是什么），再谈 runtime（运行时如何计算）  
- 先理想闭环（G0–G5 的逻辑），再谈工程补丁（G6）  
原编号：R-226

---

## 附录：原编号与新编号对照表

| 原编号 | 新编号 | 主目标 |
|---|---|---|
| R-001 | G1-R001 | G1 存在性 |
| R-002 | G1-R002 | G1 存在性 |
| R-003 | G0-R002 | G0 物理不变量 |
| R-004 | G0-R003 | G0 物理不变量 |
| R-005 | G1-R003 | G1 存在性 |
| R-006 | G1-R005 | G1 存在性 |
| R-007 | G1-R005 | G1 存在性 |
| R-008 | G1-R005 | G1 存在性 |
| R-009 | G1-R006 | G1 存在性 |
| R-010 | G1-R007 | G1 存在性 |
| R-011 | G1-R014 | G1 存在性 |
| R-012 | G1-R018 | G1 存在性 |
| R-013 | G1-R014 | G1 存在性 |
| R-014 | G1-R004 | G1 存在性 |
| R-015 | G1-R008 | G1 存在性 |
| R-016 | G1-R008 | G1 存在性 |
| R-017 | G1-R008 | G1 存在性 |
| R-018 | G1-R008 | G1 存在性 |
| R-019 | G1-R009 | G1 存在性 |
| R-020 | G1-R010 | G1 存在性 |
| R-021 | G1-R011 | G1 存在性 |
| R-022 | G1-R011 | G1/G5 |
| R-023 | G1-R012 | G1 存在性 |
| R-024 | G1-R012 | G1 存在性 |
| R-025 | G1-R012 | G1 存在性 |
| R-026 | G1-R012 | G1 存在性 |
| R-027 | G1-R012 | G1 存在性 |
| R-028 | G1-R012 | G1/G5 |
| R-029 | G1-R011 | G1/G5 |
| R-030 | G1-R011 | G1 存在性 |
| R-031 | G1-R014 | G1 存在性 |
| R-032 | G1-R014 | G1 存在性 |
| R-033 | G1-R014 | G1 存在性 |
| R-034 | G1-R014 | G1 存在性 |
| R-035 | G1-R016 | G1/G4 |
| R-036 | G1-R015 | G1 存在性 |
| R-037 | G4-R021 | G4 功能正确性 |
| R-038 | G4-R021 | G4 功能正确性 |
| R-039 | G4-R019 | G4 功能正确性 |
| R-040 | G4-R021 | G4 功能正确性 |
| R-041 | G2-R005 | G2 单步可行性 |
| R-042 | G2-R005 | G2/G4 |
| R-043 | G0-R004 | G0 物理不变量 |
| R-044 | G4-R014 | G4 功能正确性 |
| R-045 | G4-R026 | G4 功能正确性 |
| R-046 | G1-R018 | G1 存在性 |
| R-047 | G1-R018 | G1 存在性 |
| R-048 | G1-R018 | G1 存在性 |
| R-049 | G1-R019 | G1 存在性 |
| R-050 | G1-R019 | G1 存在性 |
| R-051 | G1-R019 | G1 存在性 |
| R-052 | G1-R019 | G1/G0 |
| R-053 | G1-R019 | G1 存在性 |
| R-054 | G1-R019 | G1/G3 |
| R-055 | G1-R019 | G1 存在性 |
| R-056 | G1-R019 | G1/G3 |
| R-057 | G4-R030 | G4 功能正确性 |
| R-058 | G1-R020 | G1（禁止项）|
| R-059 | G1-R020 | G1（禁止项）|
| R-060 | G1-R021 | G1 存在性 |
| R-061 | G1-R021 | G1 存在性 |
| R-062 | G4-R029 | G4 功能正确性 |
| R-063 | G1-R020 | G1（禁止项）|
| R-064 | G1-R018 | G1 存在性 |
| R-065 | G4-R001 | G4 功能正确性 |
| R-066 | G4-R001 | G4 功能正确性 |
| R-067 | G4-R001 | G4 功能正确性 |
| R-068 | G4-R002 | G4 功能正确性 |
| R-069 | G4-R003 | G4 功能正确性 |
| R-070 | G4-R003 | G4 功能正确性 |
| R-071 | G4-R003 | G4（禁止项）|
| R-072 | G4-R003 | G4（禁止项）|
| R-073 | G1-R023 | G1/G4 |
| R-074 | G1-R024 | G1/G4 |
| R-075 | Gm-R002 | Gₘ 元原则 |
| R-076 | Gm-R002 | Gₘ 元原则 |
| R-077 | G4-R004 | G4 功能正确性 |
| R-078 | G4-R005 | G4 功能正确性 |
| R-079 | G4-R006 | G4 功能正确性 |
| R-080 | G4-R006 | G4 功能正确性 |
| R-081 | G2-R001 | G2 单步可行性 |
| R-082 | G2-R002 | G2 单步可行性 |
| R-083 | G2-R003 | G2 单步可行性 |
| R-084 | G2-R004 | G2 单步可行性 |
| R-085 | G2-R005 | G2 单步可行性 |
| R-086 | G2-R003 | G2 单步可行性 |
| R-087 | G2-R003 | G2 单步可行性 |
| R-088 | G2-R006 | G2/G3 |
| R-089 | G2-R002 | G2 单步可行性 |
| R-090 | G2-R004 | G2/G0 |
| R-091 | G4-R008 | G4/Gₘ |
| R-092 | G4-R008 | G4 功能正确性 |
| R-093 | G4-R007 | G4 功能正确性 |
| R-094 | G4-R007 | G4 功能正确性 |
| R-095 | G3-R001 | G3 长时稳定性 |
| R-096 | G3-R002 | G3 长时稳定性 |
| R-097 | G3-R001 | G3 长时稳定性 |
| R-098 | G3-R003 | G3/G0 |
| R-099 | G3-R003 | G3 长时稳定性 |
| R-100 | G4-R009 | G4 功能正确性 |
| R-101 | G4-R009 | G4 功能正确性 |
| R-102 | G4-R009 | G4 功能正确性 |
| R-103 | G4-R010 | G4 功能正确性 |
| R-104 | G4-R011 | G4 功能正确性 |
| R-105 | G4-R012 | G4/G3 |
| R-106 | G4-R012 | G4/G3 |
| R-107 | G4-R012 | G3/G4 |
| R-108 | G1-R013 | G1 存在性 |
| R-109 | G0-R001 | G0 物理不变量 |
| R-110 | G0-R001 | G0 物理不变量 |
| R-111 | G4-R013 | G4 功能正确性 |
| R-112 | G4-R013 | G4 功能正确性 |
| R-113 | G4-R017 | G4 功能正确性 |
| R-114 | G4-R017 | G4 功能正确性 |
| R-115 | G4-R018 | G4 功能正确性 |
| R-116 | G4-R018 | G4 功能正确性 |
| R-117 | G4-R019 | G4 功能正确性 |
| R-118 | G1-R017 | G1 存在性 |
| R-119 | G0-R008 | G0 物理不变量 |
| R-120 | G0-R008 | G0 物理不变量 |
| R-121 | G4-R009 | G4 功能正确性 |
| R-122 | G0-R008 | G0/G1 |
| R-123 | G0-R009 | G0（禁止项）|
| R-124 | G0-R009 | G0（禁止项）|
| R-125 | G4-R025 | G4 功能正确性 |
| R-126 | G1-R022 | G1 存在性 |
| R-127 | G1-R022 | G1 存在性 |
| R-128 | G4-R020 | G4（禁止项）|
| R-129 | G4-R020 | G4（禁止项）|
| R-130 | G4-R020 | G4 功能正确性 |
| R-131 | G0-R007 | G0 物理不变量 |
| R-132 | G0-R007 | G0 物理不变量 |
| R-133 | G3-R004 | G3 长时稳定性 |
| R-134 | G3-R004 | G3 长时稳定性 |
| R-135 | G3-R005 | G3/G4 |
| R-136 | G3-R005 | G3/G4 |
| R-137 | G3-R005 | G3/G4 |
| R-138 | G3-R005 | G3/G4 |
| R-139 | G3-R005 | G3/G4 |
| R-140 | G0-R005 | G0 物理不变量 |
| R-141 | G0-R005 | G0 物理不变量 |
| R-142 | G0-R006 | G0/G4 |
| R-143 | G3-R006 | G3 长时稳定性 |
| R-144 | G3-R006 | G3 长时稳定性 |
| R-145 | G3-R007 | G3（禁止项）|
| R-146 | G3-R007 | G3 长时稳定性 |
| R-147 | G4-R015 | G4/G5 |
| R-148 | G4-R015 | G4/G5 |
| R-149 | G4-R015 | G4 功能正确性 |
| R-150 | G4-R015 | G4 功能正确性 |
| R-151 | G4-R016 | G4 功能正确性 |
| R-152 | G4-R016 | G4 功能正确性 |
| R-153 | G3-R008 | G3 长时稳定性 |
| R-154 | G0-R010 | G0 物理不变量 |
| R-155 | G3-R009 | G3 长时稳定性 |
| R-156 | G3-R009 | G3 长时稳定性 |
| R-157 | G0-R010 | G0 物理不变量 |
| R-158 | G3-R010 | G3 长时稳定性 |
| R-159 | G4-R027 | G4 功能正确性 |
| R-160 | G4-R028 | G4 功能正确性 |
| R-161 | G0-R011 | G0 物理不变量 |
| R-162 | G3-R010 | G3 长时稳定性 |
| R-163 | G3-R011 | G3 长时稳定性 |
| R-164 | G4-R022 | G4 功能正确性 |
| R-165 | G4-R022 | G4 功能正确性 |
| R-166 | G4-R022 | G4 功能正确性 |
| R-167 | G4-R023 | G4 功能正确性 |
| R-168 | G4-R023 | G4 功能正确性 |
| R-169 | G4-R023 | G4 功能正确性 |
| R-170 | G4-R023 | G4 功能正确性 |
| R-171 | G4-R024 | G4 功能正确性 |
| R-172 | G0-R012 | G0/G5 |
| R-173 | G0-R012 | G0/G5 |
| R-174 | G5-R001 | G5 可追溯性 |
| R-175 | G0-R012 | G0/G5 |
| R-176 | G0-R012 | G0/G5 |
| R-177 | G5-R002 | G5 可追溯性 |
| R-178 | G5-R003 | G5 可追溯性 |
| R-179 | G5-R003 | G5 可追溯性 |
| R-180 | G5-R004 | G5/G6 |
| R-181 | G5-R004 | G5 可追溯性 |
| R-182 | G5-R005 | G5/G6 |
| R-183 | G5-R006 | G5/G6 |
| R-184 | G3-R012 | G3 长时稳定性 |
| R-185 | G3-R012 | G3 长时稳定性 |
| R-186 | Gm-R001 | Gₘ 元原则 |
| R-187 | G2-R007 | G2/Gₘ |
| R-188 | Gm-R002 | Gₘ 元原则 |
| R-189 | G3-R013 | G3 长时稳定性 |
| R-190 | G3-R013 | G3 长时稳定性 |
| R-191 | G3-R014 | G3 长时稳定性 |
| R-192 | G3-R014 | G3/G0 |
| R-193 | G6-R001 | G6 工程鲁棒性 |
| R-194 | G6-R002 | G6 工程鲁棒性 |
| R-195 | G6-R003 | G6 工程鲁棒性 |
| R-196 | G6-R004 | G6 工程鲁棒性 |
| R-197 | G6-R005 | G6 工程鲁棒性 |
| R-198 | G6-R006 | G6 工程鲁棒性 |
| R-199 | G6-R007 | G6 工程鲁棒性 |
| R-200 | G6-R001 | G6 工程鲁棒性 |
| R-201 | G6-R008 | G6 工程鲁棒性 |
| R-202 | G6-R009 | G6 工程鲁棒性 |
| R-203 | G6-R010 | G6 工程鲁棒性 |
| R-204 | G6-R011 | G6 工程鲁棒性 |
| R-205 | G6-R004 | G6 工程鲁棒性 |
| R-206 | G6-R012 | G6 工程鲁棒性 |
| R-207 | G6-R013 | G6 工程鲁棒性 |
| R-208 | Gm-R003 | Gₘ 元原则 |
| R-209 | Gm-R004 | Gₘ 元原则 |
| R-210 | Gf-R001 | Gf 后续优化 |
| R-211 | Gf-R002 | Gf 后续优化 |
| R-212 | Gf-R003 | Gf 后续优化 |
| R-213 | Gf-R004 | Gf 后续优化 |
| R-214 | Gf-R005 | Gf 后续优化 |
| R-215 | Gf-R006 | Gf 后续优化 |
| R-216 | Gf-R007 | Gf 后续优化 |
| R-217 | Gf-R008 | Gf 后续优化 |
| R-218 | Gd-R001 | Gd 文档规范 |
| R-219 | Gd-R001 | Gd 文档规范 |
| R-220 | Gd-R001 | Gd 文档规范 |
| R-221 | Gd-R002 | Gd 文档规范 |
| R-222 | Gd-R003 | Gd 文档规范 |
| R-223 | Gd-R004 | Gd 文档规范 |
| R-224 | Gd-R005 | Gd 文档规范 |
| R-225 | Gd-R006 | Gd 文档规范 |
| R-226 | Gd-R007 | Gd 文档规范 |

---

*文档结束*
