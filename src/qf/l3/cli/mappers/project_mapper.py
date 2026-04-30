from __future__ import annotations

from qf.l1_application.commands.project_command import ProjectCommand
from qf.l3.cli.base import ProjectNamespace


def to_project_command(ns: ProjectNamespace) -> ProjectCommand:
    return ProjectCommand(
        projects_root=ns.projects_root,
        init=ns.init,
    )
