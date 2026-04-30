from __future__ import annotations

from qf.l0.model.models import PatternSuggestion
from qf.l0.planners.generation_plan import GenerationPlan
from qf.l0.planners.string_planner import StringPlanner


def test_generation_plan_accepts_tables() -> None:
    ps = PatternSuggestion(
        strategy="test",
        pattern_id=None,
        confidence=1.0,
        reason="t",
        suggestor="t",
        priority=0,
    )
    sp = StringPlanner()
    gp = GenerationPlan(
        table="t1", column="test", suggestion=ps, col_planner=sp
    )
    assert gp.table == "t1"
