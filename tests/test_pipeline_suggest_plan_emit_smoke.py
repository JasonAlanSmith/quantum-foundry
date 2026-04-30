from __future__ import annotations

from qf.emitters.sql import SqlEmitter
from qf.l0.model.models import ColumnInspection
from qf.l0.planners.registry import PlannerRegistry
from qf.l0.suggestors.defaults import build_default_registry
from qf.l0.suggestors.engine import suggest_for_column
from qf.l1.plan.context import PlanContext


def test_pipeline_suggest_plan_emit_for_first_name(
    col_first_name: ColumnInspection, plan_context: PlanContext
) -> None:
    # Suggest
    sreg = build_default_registry()
    suggestion = suggest_for_column(col_first_name, sreg.all())
    assert suggestion.pattern_id == "first_names"

    # Plan
    preg = PlannerRegistry.default()
    planner = preg.get(suggestion.strategy)
    assert planner is not None
    ed = planner.plan(col_first_name, suggestion, plan_context)
    assert ed is not None

    # Emit
    sql_lines = list(SqlEmitter().emit(col_first_name.table, [ed]))
    assert any("INSERT" in s.upper() for s in sql_lines)
    assert any(col_first_name.table in s for s in sql_lines)
