
from __future__ import annotations
import yaml
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "configs" / "requirement_registry.yaml"


def main() -> None:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    reqs = data["requirements"]
    ids = [r["id"] for r in reqs]
    assert len(ids) == len(set(ids)), "Requirement IDs must be unique."
    assert data["meta"]["total_requirements"] == len(reqs), "Total requirement count mismatch."
    tier_counts = Counter(r["tier"] for r in reqs)
    goal_counts = Counter(r["goal"] for r in reqs)

    print("Registry OK")
    print("Total:", len(reqs))
    print("By tier:", dict(tier_counts))
    print("By goal:", dict(goal_counts))


if __name__ == "__main__":
    main()
