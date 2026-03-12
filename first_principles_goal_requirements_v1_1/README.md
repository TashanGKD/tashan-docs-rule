
# first_principles_goal_requirements_v1_1

这个压缩包包含三类内容：

1. **主文档**
   - `docs/01_目标—要求体系_v1.1.md`
   - 这是可直接继续编辑的新文档，采用“目标树 → 要求树”结构。
   - 总叶子要求数：226

2. **代码化表达**
   - `code/configs/requirement_registry.yaml`：完整要求注册表（226 条）
   - `code/schemas/requirement_registry.schema.json`：要求注册表 Schema
   - `code/schemas/system_state.schema.json`：world / agents / meta 的状态约束 Schema
   - `code/python/models.py`：核心 dataclass / enum
   - `code/python/contracts.py`：assemble / evolve / emit / apply 的协议接口
   - `code/python/validators.py`：一阶硬约束校验器
   - `code/python/example_validate.py`：最小样例

3. **模板与图**
   - `code/templates/system_state_template.yaml`：最小系统状态模板
   - `code/templates/directory_contract.yaml`：目录—持有者契约模板
   - `figures/goal_tree.png`：目标树图
   - `figures/directory_map.png`：world / agents / meta 映射图

## 三档标签
- **硬要求**：理想情况下要让系统成立、闭环、长期演化，必须满足。
- **可后置**：不属于最小主干，但对语义完整性、认知连续性、质量或后续演化重要，可后置。
- **工程增强**：实现层 / 非理想条件下的防故障、稳态化与恢复增强。

## 如何使用
先读 `docs/01_目标—要求体系_v1.1.md`。
然后：
- 用 `code/configs/requirement_registry.yaml` 做 requirement registry
- 用 `code/schemas/system_state.schema.json` 和 `code/python/validators.py` 对 state / config 做校验
- 用 `code/templates/system_state_template.yaml` 作为初始模板

## 说明
本包中的主文档是一个**新的独立文档**，正文不再显示旧版编号映射。
