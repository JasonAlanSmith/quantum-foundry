from __future__ import annotations

from collections.abc import Callable
from typing import Any, Protocol

from qf.l0.enums import SqlType
from qf.l0.model.models import (
    ColumnEmitDefinition,
    ColumnInspection,  # adjust import
    PatternSuggestion,  # adjust import
)
from qf.l1.plan.context import PlanContext


class ColumnPlanner(Protocol):
    strategy: str  # registry key

    def plan(
        self,
        column: ColumnInspection,
        suggestion: PatternSuggestion,
        ctx: PlanContext,
    ) -> ColumnEmitDefinition | None: ...

    def compile(
        self,
        column: ColumnInspection,
        suggestion: PatternSuggestion,
        ctx: PlanContext,
    ) -> tuple[SqlType, Callable[[], Any | None]]: ...
