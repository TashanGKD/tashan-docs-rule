
from __future__ import annotations
from typing import Protocol, Any, Dict, List


class AssembleFn(Protocol):
    def __call__(self, *, world_view: Dict[str, Any], agent_state: Dict[str, Any], meta_view: Dict[str, Any]) -> Dict[str, Any]:
        """读取 world/agent/meta 的可见切片，组装本轮上下文。"""
        ...


class EvolveFn(Protocol):
    def __call__(self, assembled_context: Dict[str, Any]) -> Dict[str, Any]:
        """从上下文得到动作提议与状态更新提议。"""
        ...


class EmitFn(Protocol):
    def __call__(self, evolve_output: Dict[str, Any]) -> List[Dict[str, Any]]:
        """把输出转成事件流。"""
        ...


class ApplyFn(Protocol):
    def __call__(self, durable_state: Dict[str, Any], events_in: List[Dict[str, Any]]) -> Dict[str, Any]:
        """把事件写回 durable 状态。"""
        ...
