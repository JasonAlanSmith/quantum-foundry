# qf/suggestors/defaults.py
from __future__ import annotations

from qf.l0.suggestors.builtins import (
    EmailSuggestor,
    FirstNameSuggestor,
    ForeignKeySuggestor,
    StatusCodeSuggestor,
    TimestampSuggestor,
    UuidSuggestor,
)
from qf.l0.suggestors.registry import SuggestorRegistry


def build_default_registry() -> SuggestorRegistry:
    reg = SuggestorRegistry()
    reg.register_many(
        [
            FirstNameSuggestor(),
            ForeignKeySuggestor(),
            EmailSuggestor(),
            UuidSuggestor(),
            TimestampSuggestor(),
            StatusCodeSuggestor(),
        ]
    )
    return reg
