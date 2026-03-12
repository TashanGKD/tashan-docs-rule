
from __future__ import annotations
import yaml
from models import (
    ActivityInstance, ActivityProfile, AgentState, ControlState, FieldProfile,
    InteractionContext, MetaState, SystemState, WorldState
)
from validators import validate_system_state


def build_example() -> SystemState:
    field = FieldProfile(
        arity="group",
        co_presence="remote",
        synchrony="live",
        lifecycle="persistent",
        task_binding="casual",
        visibility="members_only",
        attention_impact="engaged",
        normative_force="soft",
    )
    ctx = InteractionContext(field=field, participants=["role_001"], messages=[], status="open")
    activity = ActivityInstance(
        preset="thinking_deep",
        profile=ActivityProfile(
            mode="thinking",
            medium="computer",
            input_openness="mention",
            output_bandwidth="medium",
            interrupt_tolerance="medium",
            energy_profile="consuming",
            mobility="switchable",
        ),
        object_ref=None,
    )
    agent = AgentState(
        memory={"self": {"name": "role_001"}},
        control=ControlState(
            physical_location=None,
            foreground_stack=[],
            current_activity=activity,
            baseline_attention_policy="mention",
            active_key=None,
            next_wakeup=60.0,
            last_evolved_at=0.0,
            energy=80.0,
        ),
        capability={"tools": []},
    )
    world = WorldState(clock=0.0, natural_state={}, interaction_contexts={"ctx_001": ctx})
    meta = MetaState(notification_buffer={"role_001": []}, scheduler={"pending_wakeups": {}}, event_log=[])
    return SystemState(world=world, agents={"role_001": agent}, meta=meta)


if __name__ == "__main__":
    state = build_example()
    validate_system_state(state)
    print("SystemState contract validation: OK")
