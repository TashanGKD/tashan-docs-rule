
from __future__ import annotations
from typing import Any, Dict, Iterable, List
from models import SystemState, TERMINAL_NOTIFICATION_STATUSES, NotificationStatus


class ContractError(ValueError):
    """Raised when a system state violates a hard contract."""


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def validate_world_state(state: SystemState) -> None:
    ensure(state.world.clock >= 0, "world.clock 必须存在且非负。")
    ensure(isinstance(state.world.interaction_contexts, dict), "interaction_contexts 必须属于 world 且为映射。")
    for ctx_id, ctx in state.world.interaction_contexts.items():
        ensure(ctx.field is not None, f"context={ctx_id} 缺少 field。")
        ensure(isinstance(ctx.participants, list), f"context={ctx_id} participants 必须为列表。")
        ensure(isinstance(ctx.messages, list), f"context={ctx_id} messages 必须为列表。")


def validate_agent_state(state: SystemState) -> None:
    for agent_id, agent in state.agents.items():
        c = agent.control
        ensure(c.next_wakeup is not None, f"{agent_id}.control.next_wakeup 不能为空。")
        ensure(0 <= c.energy <= 100, f"{agent_id}.control.energy 必须在 [0,100]。")
        ensure(c.current_activity is not None, f"{agent_id}.control.current_activity 不能为空。")
        ensure(c.current_activity.profile is not None, f"{agent_id}.control.current_activity.profile 不能为空。")
        ensure(c.baseline_attention_policy not in ("", None), f"{agent_id}.baseline_attention_policy 不能为空。")
        ensure(isinstance(c.foreground_stack, list), f"{agent_id}.foreground_stack 必须为列表。")
        # 单前景场语义：栈顶唯一生效；这里仅验证 durable 结构是“单栈”而非多并行字段
        ensure(not hasattr(c, "foreground_field_id"), f"{agent_id} 不应再持有 durable foreground_field_id。")


def validate_meta_state(state: SystemState) -> None:
    ensure(isinstance(state.meta.notification_buffer, dict), "notification_buffer 必须属于 meta 并按 recipient 分桶。")
    for recipient, queue in state.meta.notification_buffer.items():
        ensure(isinstance(queue, list), f"notification_buffer[{recipient}] 必须为列表。")
        for n in queue:
            ensure("status" in n, f"notification 缺少 status。")
            ensure("ttl_sec" in n, f"notification 缺少 ttl_sec。")
            ensure(n["ttl_sec"] >= 0, f"notification.ttl_sec 必须非负。")


def validate_truth_source_placement(state: SystemState) -> None:
    # 这些检查表达“目录/持有者归属”的一阶契约
    ensure(hasattr(state, "world"), "SystemState 必须包含 world。")
    ensure(hasattr(state, "agents"), "SystemState 必须包含 agents。")
    ensure(hasattr(state, "meta"), "SystemState 必须包含 meta。")


def validate_notification_terminality(meta_dict: Dict[str, List[Dict[str, Any]]]) -> None:
    # 静态检查：允许的终局值是否存在于队列状态枚举中
    statuses = {n.get("status") for q in meta_dict.values() for n in q}
    allowed = {s.value for s in TERMINAL_NOTIFICATION_STATUSES}
    ensure(bool(allowed), "必须定义通知终局状态集合。")
    ensure(all(s is not None for s in statuses), "notification.status 不得缺失。")


def validate_event_log_uniqueness(meta_event_log: List[Dict[str, Any]]) -> None:
    ids = [e.get("id") for e in meta_event_log]
    ids = [i for i in ids if i is not None]
    ensure(len(ids) == len(set(ids)), "event_log 中的 event id 不得重复。")


def validate_system_state(state: SystemState) -> None:
    validate_truth_source_placement(state)
    validate_world_state(state)
    validate_agent_state(state)
    validate_meta_state(state)
    validate_notification_terminality(state.meta.notification_buffer)
    validate_event_log_uniqueness(state.meta.event_log)
