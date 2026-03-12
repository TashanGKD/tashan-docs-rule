
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class Tier(str, Enum):
    HARD = "hard"
    DEFERRED = "deferred"
    ENGINEERING = "engineering"


class NotificationStatus(str, Enum):
    PENDING = "pending"
    SURFACED = "surfaced"
    ACKNOWLEDGED = "acknowledged"
    CONSUMED = "consumed"
    EXPIRED = "expired"
    MERGED = "merged"
    ARCHIVED = "archived"


TERMINAL_NOTIFICATION_STATUSES = {
    NotificationStatus.CONSUMED,
    NotificationStatus.EXPIRED,
    NotificationStatus.MERGED,
    NotificationStatus.ARCHIVED,
}


@dataclass
class Requirement:
    id: str
    goal: str
    group: str
    tier: Tier
    kind: str
    statement: str
    parent: str
    codifiable: bool
    representation_hint: str


@dataclass
class FieldProfile:
    arity: str
    co_presence: str
    synchrony: str
    lifecycle: str
    task_binding: str
    visibility: str
    attention_impact: str
    normative_force: str


@dataclass
class InteractionContext:
    field: FieldProfile
    participants: List[str]
    messages: List[Dict[str, Any]]
    status: str
    roles: Dict[str, Any] = field(default_factory=dict)
    agenda: List[Dict[str, Any]] = field(default_factory=list)
    obligations: List[Dict[str, Any]] = field(default_factory=list)
    place_id: Optional[str] = None


@dataclass
class ActivityProfile:
    mode: str
    medium: str
    input_openness: str
    output_bandwidth: str
    interrupt_tolerance: str
    energy_profile: str
    mobility: str


@dataclass
class ActivityInstance:
    preset: str
    profile: ActivityProfile
    object_ref: Optional[str]
    toolset: List[str] = field(default_factory=list)
    writeback_policy: Optional[str] = None
    transition_condition: Optional[str] = None
    reservation_until: Optional[float] = None
    resume_token: Optional[str] = None


@dataclass
class ControlState:
    physical_location: Optional[str]
    foreground_stack: List[Dict[str, Any]]
    current_activity: ActivityInstance
    baseline_attention_policy: str
    active_key: Optional[str]
    next_wakeup: float
    last_evolved_at: float
    energy: float
    mood: Optional[Dict[str, Any]] = None


@dataclass
class AgentState:
    memory: Dict[str, Any]
    control: ControlState
    capability: Dict[str, Any]


@dataclass
class WorldState:
    clock: float
    natural_state: Dict[str, Any]
    interaction_contexts: Dict[str, InteractionContext]


@dataclass
class MetaState:
    notification_buffer: Dict[str, List[Dict[str, Any]]]
    scheduler: Dict[str, Any]
    event_log: List[Dict[str, Any]]
    writeback_ledger: List[Dict[str, Any]] = field(default_factory=list)
    staging_ledger: List[Dict[str, Any]] = field(default_factory=list)
    resource_leases: Dict[str, Any] = field(default_factory=dict)
    active_obligations: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class SystemState:
    world: WorldState
    agents: Dict[str, AgentState]
    meta: MetaState
