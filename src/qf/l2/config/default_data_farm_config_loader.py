from __future__ import annotations

from pathlib import Path
from typing import Any

from qf.utils.config import load_qf_config as _load_qf_config

ConfigDict = dict[str, Any]


def load_qf_config(config_path: Path) -> ConfigDict | None:
    return _load_qf_config(config_path)
