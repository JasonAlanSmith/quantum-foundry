from __future__ import annotations

from collections.abc import Callable
from typing import Any

from qf.emitters.sql import ColumnEmitDefinition
from qf.field.text import TextFieldDefinition
from qf.l0.enums import SqlType
from qf.l0.generators.text import TextGenerator
from qf.l0.model.models import (
    ColumnInspection,  # adjust import
    PatternSuggestion,
)
from qf.l1.plan.context import PlanContext


class JSONBPlanner:
    strategy = "jsonb"

    def compile(
        self,
        column: ColumnInspection,
        suggestion: PatternSuggestion,
        ctx: PlanContext,
    ) -> tuple[SqlType, Callable[[], Any | None]]:
        """
        Compile a per-column generator to remove planning work from the
        hot row loop.
        """
        pattern_key = self._pattern_key_for_strategy(
            suggestion.strategy
        )

        if pattern_key and ctx.patterns.exists(pattern_key):
            choices = ctx.patterns.get_choices(pattern_key)
        else:
            choices = [
                '{"row": 42,"seed":12345}',
                '{"col": 65,"lot":538}',
            ]

        field_def = TextFieldDefinition(
            allow_null=column.nullable,
            fixed_length=None,
            min_length=0,
            max_length=100,
        )

        gen = TextGenerator(ctx.rng, choices, field_def)
        return (SqlType.JSONB, gen.generate)

    def plan(
        self,
        column: ColumnInspection,
        suggestion: PatternSuggestion,
        ctx: PlanContext,
    ) -> ColumnEmitDefinition | None:
        pattern_key = self._pattern_key_for_strategy(
            suggestion.strategy
        )

        if pattern_key and ctx.patterns.exists(pattern_key):
            choices = ctx.patterns.get_choices(pattern_key)
        else:
            choices = [
                '{"row": 42,"seed":12345}',
                '{"col": 65,"lot":538}',
            ]

        field_def = TextFieldDefinition(
            allow_null=column.nullable,
            fixed_length=None,
            min_length=0,
            max_length=100,
        )

        value = TextGenerator(ctx.rng, choices, field_def).generate()
        if value is None:
            return None

        return ColumnEmitDefinition(
            name=column.name,
            data_type=SqlType.JSONB,
            value=value,
        )

    @staticmethod
    def _pattern_key_for_strategy(strategy: str) -> str | None:
        s = (strategy or "").strip().lower()
        if s == "age":
            return "ages"

        return None
