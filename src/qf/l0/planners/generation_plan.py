from __future__ import annotations

from dataclasses import dataclass

from qf.l0.model.models import PatternSuggestion
from qf.l0.planners.protocols import ColumnPlanner


@dataclass(frozen=True)
class GenerationPlan:
    table: str
    column: str
    suggestion: PatternSuggestion
    col_planner: ColumnPlanner
