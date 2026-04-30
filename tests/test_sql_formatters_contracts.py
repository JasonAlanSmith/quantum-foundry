from __future__ import annotations

import pytest

from qf.emitters.sql import build_vals
from qf.l0.enums import SqlType
from qf.l0.model.models import ColumnEmitDefinition


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (True, "true"),
        (False, "false"),
        ("true", "true"),
        ("TrUe", "true"),
        ("t", "true"),
        ("1", "true"),
        ("yes", "true"),
        ("y", "true"),
        ("false", "false"),
        ("0", "false"),
        ("no", "false"),
        ("", "false"),
    ],
)
def test_boolean_formatter_accepts_common_inputs(
    raw: bool | str, expected: str
) -> None:
    vals = build_vals(
        [
            ColumnEmitDefinition(
                name="b", data_type=SqlType.BOOLEAN, value=raw
            )
        ]
    )
    assert vals == expected


def test_json_formatter_emits_jsonb_cast() -> None:
    vals = build_vals(
        [
            ColumnEmitDefinition(
                name="j", data_type=SqlType.JSON, value='{"a":1}'
            )
        ]
    )
    expected = "'{\"a\":1}'::jsonb"
    assert vals == expected
