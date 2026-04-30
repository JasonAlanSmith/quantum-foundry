from __future__ import annotations

from pathlib import Path
from typing import Any

from qf.l1_application.ports.project_settings_store import ProjectSettingsStore
from qf.l2.config.default_qf_config_loader import load_qf_config
from qf.utils.config import qf_config, store_qf_config

ConfigDict = dict[str, Any]


class DefaultProjectSettingsStore(ProjectSettingsStore):
    def set_projects_root(self, config_path: Path, projects_root: str) -> None:
        cd = load_qf_config(config_path) or dict(qf_config)
        cd.setdefault("project", {})["projects_root"] = projects_root
        store_qf_config(config_path, cd)
