采用**严格唯一编号**（`R-001` 起）

---

# 《要求总表 v1》

## A. 系统存在、对象与状态空间

**R-001** 系统至少由一个世界粒子 `A` 和有限个智能体粒子 `{B₁...Bₙ}` 组成。
**R-002** 每个粒子都必须满足三元组形式 `P = (V_P, View_P, R_P)`。
**R-003** `V_P` 是粒子的本体变量集，只能由粒子自身或授权的系统外力写入。
**R-004** `View_P(observer)` 是对 `V_P` 的可见投影，不持有新信息，不独立存储。
**R-005** `R_P` 必须至少细分为 `assemble / evolve / emit / apply` 四子规则。
**R-006** 系统必须区分 `S_global` 与 `S_total`。
**R-007** `S_global` 仅由粒子本体真状态组成。
**R-008** `S_total` 必须至少包含 `S_global × notification_buffer × M_meta^persist`。
**R-009** `notification_buffer` 不属于任何单个粒子，但属于系统前向演化状态。
**R-010** `M_meta^persist` 不属于任何单个粒子，但属于系统前向演化状态。
**R-011** 当前权威结构下，世界粒子的最小骨架应为 `V_A = { clock, natural_state, interaction_contexts }`。
**R-012** 当前权威结构下，智能体粒子的最小骨架应为 `V_B = { memory, control, capability }`。
**R-013** `interaction_contexts` 应属于 `V_A`，而不是从现有权威定义中独立拆出为第三类本体变量。
**R-014** 系统应承认存在系统级非粒子对象，如 `notification_buffer`、`Scheduler`、`Global Event Log` 与持久元状态。
**R-015** durable 持有者应至少能被映射为 `world / agents / meta` 三类顶层归属。 

---

## B. world / agents / meta 的持有者归属

**R-016** `world` 应持有世界粒子 A 的 durable 真状态。
**R-017** `agents/role_i` 应持有第 i 个智能体粒子的 durable 真状态。
**R-018** `meta` 应持有不属于任何单个粒子、但影响系统下一步演化的系统级对象。
**R-019** `world` 至少应包含 `clock`、`natural_state`、`interaction_contexts`。
**R-020** `agents/role_i` 至少应包含 `memory`、`control`、`capability`。
**R-021** `meta` 至少应包含 `notification_buffer` 与调度相关持久态。
**R-022** `meta` 应承载 `Global Event Log` 或其等价唯一真源。
**R-023** `FieldProfile` 的 durable 真源应位于 `world/interaction_contexts/<ctx>/field`。
**R-024** `ActivityRuntimeProfile` 的 durable 真源应位于 `agents/<role>/control/current_activity/profile`。
**R-025** `notification_buffer` 的 durable 真源应位于 `meta/notification_buffer/*`。
**R-026** `ForegroundStack` 的 durable 真源应位于 `agents/<role>/control/foreground_stack`。
**R-027** `next_wakeup` 的 durable 真源应位于 `agents/<role>/control/next_wakeup`。
**R-028** `Global Event Log` 作为唯一真源，不能被误写成 agent 私有文件。
**R-029** `WritebackLedger` 若存在，应位于 `meta/`，且不得被解释为第二真源。
**R-030** `ResourceLease`、活跃 `Obligation` 集合、`Scheduler.pending_wakeups` 若存在，也应位于 `meta/`。 

---

## C. 世界粒子 A 相关要求

**R-031** `clock` 必须存在，且作为系统统一时间基底。
**R-032** `clock` 必须参与世界侧的自主推进或触发逻辑。
**R-033** `natural_state` 必须保留为世界粒子的自然基底变量，即使当前版本对其建模较轻。
**R-034** `interaction_contexts` 必须是世界粒子的直接组成部分。
**R-035** `interaction_contexts[*]` 必须是场参数化的交互容器。
**R-036** 每个 `InteractionContext` 至少应持有 `field`、`participants`、`messages`。
**R-037** 对 bounded / task-bound 场，`InteractionContext` 应能持有 `agenda / conclusion / status / deadline` 等任务相关变量。
**R-038** 对规范性较强的场，`InteractionContext` 应能持有 `roles / obligations`。
**R-039** co-located 场应支持 `place_id`。
**R-040** `ContextState` 应允许扩展 `files / org_memory / metadata`，但这些不是最小核必需。
**R-041** `R_A^apply` 必须能够接收来自 agent 的事件并更新 `interaction_contexts`。
**R-042** `R_A^apply` 在更新 `interaction_contexts` 后，必须能向 `notification_buffer` 路由后续影响。
**R-043** 世界粒子不应直接修改某个 agent 的本体变量。
**R-044** 世界粒子的可见投影 `View_A(B_i)` 必须基于 `interaction_contexts` 及其 `field` 决定。
**R-045** 世界粒子必须支持对 `ephemeral / bounded / persistent` 等不同生命周期 context 的关闭或归档语义。 

---

## D. 智能体粒子 B 相关要求

**R-046** 每个 agent 必须持有 `memory`。
**R-047** 每个 agent 必须持有 `control`。
**R-048** 每个 agent 必须持有 `capability`。
**R-049** `control` 至少应包含 `physical_location`。
**R-050** `control` 至少应包含 `foreground_stack`。
**R-051** `control` 至少应包含 `current_activity`。
**R-052** `control` 至少应包含 `baseline_attention_policy`。
**R-053** `control` 至少应包含 `active_key`。
**R-054** `control` 至少应包含 `next_wakeup`。
**R-055** `control` 至少应包含 `last_evolved_at`。
**R-056** `control` 至少应包含 `energy`。
**R-057** `control` 当前可包含 `mood`，但它不应阻塞主闭环。
**R-058** 旧式单值 `foreground_field_id` 不应再作为权威 durable 结构。
**R-059** 旧式裸 `activity_profile` 不应再作为权威 durable 结构。
**R-060** `current_activity` 应统一为 `ActivityInstance`。
**R-061** `ActivityInstance` 应至少包含 `preset + profile + object_ref`。
**R-062** `ActivityInstance` 可进一步包含 `toolset / writeback_policy / transition_condition / reservation_until / resume_token`。
**R-063** `current_object_ref` 不应再作为 `ControlState` 顶层字段保留为权威结构，应并入 `current_activity.object_ref`。
**R-064** agent 的 `memory`、`control` 与 `capability` 均属于 durable 真状态，不应被误当作可随时丢弃的缓存。 

---

## E. Field / Activity 相关要求

**R-065** `Field` 与 `Activity` 必须分开建模。
**R-066** `Field` 表示外部交互环境/上下文结构。
**R-067** `Activity` 表示主体当前在做什么/以何种方式耦合环境。
**R-068** 运行时行为必须由 `field_profile × activity_profile × agent_state` 共同决定。
**R-069** `Field Schema` 只是完整 Field 本体的 runtime projection。
**R-070** `Activity Schema` 只是完整 Activity 本体的 runtime projection。
**R-071** 不能把 `FieldProfile` 误写成完整 Field 本体。
**R-072** 不能把 `ActivityRuntimeProfile` 误写成完整 Activity 本体。
**R-073** `FieldProfile` 必须作为 `interaction_contexts[*]` 的内部变量块承载。
**R-074** `ActivityRuntimeProfile` 必须作为 `current_activity.profile` 的内部变量块承载。
**R-075** 任何进入高层的 Field 维度，都必须影响输入、输出、状态更新、通知优先级、调度或生命周期闭合中的至少一项。
**R-076** 任何进入高层的 Activity 维度，都必须影响输入门控、输出带宽、打断容忍度、能量动力学、切换能力或调度中的至少一项。
**R-077** `FieldProfile` 当前最小权威维度集为 8 维。
**R-078** `ActivityRuntimeProfile` 当前最小权威维度集为 7 维。
**R-079** 系统不应再优先按“论坛/群聊/chat/topic”等产品名称建模，而应优先按场参数建模。
**R-080** 具体产品形态应通过少数通用函数 + `field_profile` 参数化生成。  

---

## F. 演化与函数接口方面的要求

**R-081** 每次粒子演化必须经过 `assemble → evolve → emit → apply` 四阶段。
**R-082** `assemble` 必须组装本轮演化可见的上下文。
**R-083** `evolve` 必须从上下文得到动作提议与状态更新提议。
**R-084** `emit` 必须把输出转成事件流。
**R-085** `apply` 必须把事件写回粒子本体变量。
**R-086** 世界粒子的 `evolve` 可退化为确定性硬编码函数。
**R-087** 智能体粒子的 `evolve` 通常由 LLM 或等价决策器承担。
**R-088** 粒子函数对任意合法状态必须产生合法下一状态，不允许“无死状态”破坏。
**R-089** `assemble` 至少要能读取本体状态、必要的可见上下文和系统级待处理输入。
**R-090** `emit` 产生的外部效应必须通过事件路由，不允许直接跨粒子写状态。
**R-091** 世界侧与主体侧都应采用尽量少数的统一函数，而非为每种产品类型单写规则。
**R-092** 推荐保留的统一函数至少包括：`visibleSlice / priorityOf / canInject / canWakeup / defaultAttention / defaultActiveKey / closeCondition / allowedActions`。
**R-093** 系统应存在把 `Field × Activity × ControlState` 闭合成运行时门控对象的桥接函数（即 RuntimeEnvelope 或等价物）。
**R-094** 该桥接函数至少要输出：感知注入结果、允许动作集、状态增量建议、下次唤醒建议。  

---

## G. 调度与唤醒相关要求

**R-095** 系统必须支持 time-driven 调度。
**R-096** 系统必须支持 event-driven 调度。
**R-097** 对最小无限演化而言，至少 time-driven 触发链不能断。
**R-098** 任意时刻 `next_wakeup` 必须有定义值。
**R-099** 若本轮输出未给出 `next_wakeup`，系统必须自动填默认值。
**R-100** 当前前景场内部事件与场外事件的唤醒门槛不能相同。
**R-101** `canWakeup` 应至少区分 local 与 external 两种来源。
**R-102** 当前前景场内部事件应具备更低的唤醒门槛。
**R-103** 对语义类 `hazard / evacuation / emergency` 的事件，应存在强制唤醒覆盖通道。
**R-104** 用户直接输入应作为特殊高权限触发路径，允许绕过常规注意力门槛。
**R-105** `next_wakeup` 的默认推荐应受活动模式、场类型与当前 energy 影响。
**R-106** 系统应允许 `discussing + live` 等场景主要依赖 event-driven，而不要求高频 fallback。
**R-107** 系统应允许 `sleeping / resting / recovering` 等状态拉长 fallback。
**R-108** 调度器必须持有瞬时运行态，但不应把瞬时运行态写回任何粒子 durable 状态。 

---

## H. 写隔离、可见性、动作合法性

**R-109** 粒子不能直接写其他粒子的本体状态。
**R-110** 跨粒子影响必须经由事件与目标方 `apply` 实现。
**R-111** `View_P(observer)` 的 observer 域至少应包括其他粒子、被授权的系统元设施和外部用户。
**R-112** 不同 observer 应适用不同访问规则。
**R-113** 动作可达域应由当前场与当前活动共同决定。
**R-114** 当前权威体系中，effective_actions 应至少是“物理场允许动作 ∪ 前景场允许动作”再受 medium/bandwidth/mobility 约束。
**R-115** 不能因为当前前景在数字场，就完全忽略物理所在场的动作可达域。
**R-116** 物理现场点名/面向面的强局部信号，应拥有比一般 external 事件更高或更特殊的处理路径。
**R-117** 对 co-located 场，`place_id` 必须进入可见性与动作合法性判断。
**R-118** 系统必须允许“共享世界 + 各 agent 局部耦合通道”的结构，而不应把每个 agent 误建成各自拥有一整套独立介质本体。 

---

## I. 前景、焦点与活动切换相关要求

**R-119** v1/v5 体系下，应采用单前景场假设。
**R-120** 任意时刻只有一个栈顶前景场是生效前景。
**R-121** 其他场的事件只能通过 notification / external input 路径进入。
**R-122** `ForegroundStack` 的引入不能改变“单前景场”语义，只能增加返回路径。
**R-123** 前景切换只能通过 `ForegroundStack` 操作实现。
**R-124** 直接赋值 durable `foreground_field_id` 应被禁止。
**R-125** `ContextClosedEvent` 广播后，所有引用该 `field_id` 的前景帧都应被 pop 并触发返回逻辑。
**R-126** `active_key` 应与当前工作上下文绑定，但其真源仍在 `control.active_key`。
**R-127** `ForegroundFrame.active_key` 更适合作为前景历史快照，而非新的独立真源。
**R-128** `LLM` 不应直接输出完整 `ActivityInstance` JSON。
**R-129** `LLM` 只能输出活动 preset 名称，由系统展开为 `ActivityInstance`。
**R-130** 自定义活动若存在，必须经过合法性校验后才能写回。  

---

## J. 能量、注意力、记忆相关要求

**R-131** energy 的取值域必须固定为 `[0,100]`。
**R-132** 所有 energy 更新后都必须 clamp 到该区间。
**R-133** 只要 agent 能消耗能量，就必须存在恢复路径。
**R-134** 恢复路径必须有严格正恢复速率。
**R-135** 当前体系下，energy 动力学应采用“场 × 活动 × 时间”的 per-hour 模型。
**R-136** 旧 v4 的 per-minute 表不应再作为权威主模型。
**R-137** `fieldEnergyModifier(F_cur)` 应进入 energy 更新。
**R-138** `activityEnergyModifier(A_cur)` 应进入 energy 更新。
**R-139** `llmAdjustment` 若存在，应被 clamp 到有限范围。
**R-140** `baseline_attention_policy` 是 agent 的绝对人格基线。
**R-141** 场与活动不得通过 `R_B^apply` 自动覆写 `baseline_attention_policy`。
**R-142** 运行时有效阈值应由基线与场/活动瞬时门槛共同计算，但不写回基线。
**R-143** memory 必须有界。
**R-144** memory 必须支持压缩/遗忘/分层检索机制。
**R-145** 不能将所有记忆全量注入上下文。
**R-146** tiered memory + retrievable access 是当前最小可接受实现。
**R-147** 每条 `MemoryEntry` 应强制携带 `source_field_id`。
**R-148** `source_field_id` 应由系统注入，不允许 LLM 自由覆写。
**R-149** assembleMemory 时应优先检索同源记忆。
**R-150** 跨场记忆进入必须满足严格语义阈值（当前讨论过的典型值是 `cross_context_relevance ≥ 0.85` 且条数上限有限）。
**R-151** `mood` 当前可作为弱闭环变量存在。
**R-152** `mood` 在 v1 阶段不应参与 `canInject / canWakeup / effective_actions` 的硬决策。 

---

## K. 通知、消息、义务与 context 生命周期

**R-153** `notification_buffer` 必须有界。
**R-154** 每条通知都必须有终局。
**R-155** 最小终局实现至少应支持 `consumed / expired` 或等价语义。
**R-156** 当前权威扩展终局还包括 `merged / archived`。
**R-157** 通知不得无限 pending、无限 surfaced。
**R-158** 通知应支持 `ttl_sec`。
**R-159** 通知应支持 `semantic_class`。
**R-160** 对可以合并的通知，应支持 `collapse_key` 或等价去重机制。
**R-161** `surfaced` 不等于 `acknowledged`。
**R-162** `ack_required` 类通知若存在，必须有后继迁移路径。
**R-163** bounded / ephemeral context 不能只增不减。
**R-164** `closeCondition(field, contextState)` 必须存在。
**R-165** `lifecycle=ephemeral` 的场应有空闲关闭或成员散尽关闭语义。
**R-166** `lifecycle=bounded` 的场应有截止/结论/关闭语义。
**R-167** `mission_locked` 或 `normative_force=binding` 的场应能持有并暴露义务。
**R-168** agent 自身的 pending obligations 必须在 assemble 时被全量注入，不得因 context window 被截断。
**R-169** Obligation 系统必须有正式状态机，不能只有松散布尔值。
**R-170** 创建义务时应避免 `blocking_on` 循环。
**R-171** 义务、议程、deliverable 的组合，至少要能支持“强任务 session”的闭环。  

---

## L. 真源、日志、可回放与审计

**R-172** Global Event Log 必须是 append-only。
**R-173** Global Event Log 必须是唯一真源。
**R-174** 所有 durable 状态变更最终都必须产生可重放的事件记录。
**R-175** `WritebackLedger` 若存在，只能是 Global Event Log 的细粒度展开。
**R-176** `WritebackLedger` 不能被解释为第二真源。
**R-177** `StagingLedger` 若存在，只能作为提交前暂存区，不应被解释为真状态。
**R-178** 审计视图应被理解为 Event Log 的派生，而不是额外 durable 本体。
**R-179** 只要保证“能重建”，最弱形式的可追溯即成立；不要求每个派生投影都实时持久化。
**R-180** 如果使用因果顺序机制，WriteEvent 的应用顺序不应依赖 wall clock。
**R-181** `created_at` 更适合用于展示与 TTL，而不是因果顺序真源。
**R-182** 任何 durable 写回先写事件、再物化状态，是目前较强且被反复认可的实现语义。
**R-183** LLM 不应在 action 发出同时假设成功并把后果写回记忆；若有 `ActionReceipt` 语义，应等 receipt 再提交 durable 写回。  

---

## M. 最小无限演化判准

**R-184** 系统必须能在理想条件下无限时间演化。
**R-185** “理想条件”下的无限演化至少要求：energy 有界、memory 有界、通知有终局、next_wakeup 不断链。
**R-186** 若删掉某个对象、字段或规则后，不破坏闭环、不破坏长期稳定、不破坏恢复能力，则该对象不应占据高层。
**R-187** 任何高层规则至少应能回答：到达、看见、中断、输出、写回、再调度六问之一。
**R-188** 若一个维度不能影响输入、输出、状态更新或调度，它不应进入第一性原理层。
**R-189** 最小闭环核至少应包含：粒子三元组、`S_total`、写隔离、四阶段演化、再进入机制、唯一真源、energy bounded、memory bounded、notification terminal。
**R-190** 单前景场假设、P0 生存规则、Field × Activity 组合，是当前最小闭环核的重要组成。
**R-191** 如果一个系统会因为 context、通知或记忆无限积压而在有限时间内失效，则它不满足第一性原理要求。
**R-192** 如果一个系统会因为注意力基线被场/活动永久污染而失去调度恢复能力，则它不满足长期演化要求。 

---

## N. 工程实现阶段仍建议满足的要求（但不属于理想主干）

**R-193** busy-loop 防护应存在。
**R-194** crash recovery 语义应存在。
**R-195** split-brain 防护应存在。
**R-196** lease / queue / cleanup 机制应存在。
**R-197** overload / 大规模运行下降载策略应存在。
**R-198** Hysteresis Lock 可用于防止 energy 在临界区微震荡。
**R-199** `MAX_DELTA_T_HOURS` 可用于极端离线截断。
**R-200** `MIN_WAKEUP_INTERVAL` 可用于防止 next_wakeup ≤ now 导致忙等。
**R-201** `CLOCK_SKEW_TOLERANCE` 可用于多节点时钟偏差容忍。
**R-202** `N-tick` 超时逃生可用于 obligation deadlock 或长期无进展场景。
**R-203** `sleep_debt` 可用于生命威胁覆盖后恢复代价建模。
**R-204** `wakeup_refractory_until` 可用于防止过度唤醒抖动。
**R-205** `active_lease_refs` 可用于发言权、主持权等资源排他。
**R-206** `causal_parent_ids` 可用于逻辑时钟与拓扑应用顺序。
**R-207** `Notification Sweeper` 可用于通知队列清理。
**R-208** 这些机制虽然强烈建议实现，但不应与“理想闭环硬要求”混写。 

---

## O. 后续优化方向（我们反复认为值得满足，但可后置）

**R-209** 尽量优先通过**增加维度**解决问题，而不是堆越来越多的补丁规则。
**R-210** `attention_impact` 后续宜拆为 `cognitive_load + external_shield`。
**R-211** `task_binding` 后续宜拆为 `purpose_binding + deliverable_binding + exit_constraint`。
**R-212** `mobility` 后续宜拆为 `physical_mobility + context_switchability`。
**R-213** 系统后续宜补显式 `power_structure / permission_model`。
**R-214** 系统后续宜补显式 `resource_pressure / exclusivity`。
**R-215** `mood` 后续宜从弱闭环升级为强闭环。
**R-216** 物理世界边界（自然灾害、身体约束、生命安全级撤离等）后续宜用新本体类型而不是只靠补丁规则表达。
**R-217** 如果未来引入“耦合介质 M”作为第三类本体实体，必须明确这属于新版本体重构，而不是对当前权威结构的直接解释。 

---

## P. 文档与写法本身应满足的要求

**R-218** 主文档应优先按 durable 持有者组织：`world / agents / meta`。
**R-219** Field 与 Activity 在主文档里不应再被写成与粒子并列的顶层对象。
**R-220** 更合适的写法是：

* Field 作为 `V_A.interaction_contexts[*]` 的内部变量块
* Activity 作为 `V_B.control.current_activity.profile` 的内部变量块。
  **R-221** 主文档应尽量采用：

0. 持有者与目录映射
1. 本体（粒子与变量）
2. 演化方程
3. 约束
4. 目标
5. 工程补丁
   的组织方式。
   **R-222** 若需要讲 projection / bridge，更适合放在“演化方程章”的内部小节，而不必另起平行大章。
   **R-223** 兼容别名、旧字段名、迁移映射应单独放附录，不应污染正文。
   **R-224** 主文档应显式给出 Source of Truth Table，钉死每个关键概念的 durable 真源。
   **R-225** 主文档应显式区分：本体变量、派生变量、耦合缓冲变量、可见投影、审计投影。
   **R-226** 文档写法应尽量做到：概念先归属，再谈行为；先 durable，再谈 runtime；先理想闭环，再谈工程补丁。 

---
