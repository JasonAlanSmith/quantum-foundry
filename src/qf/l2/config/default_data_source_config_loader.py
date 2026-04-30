from __future__ import annotations

from pathlib import Path
from typing import Any

from qf.l1.ports.data_source_config_loader import (
    DataSourceConfigLoader,
)
from qf.utils.config import load_data_source_config


class DefaultDataSourceConfigLoader(DataSourceConfigLoader):
    def load(self, config_path: Path) -> list[dict[str, Any]]:
        return load_data_source_config(config_path)
