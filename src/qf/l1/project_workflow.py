from __future__ import annotations

from pathlib import Path

from qf.l1.commands.project_command import ProjectCommand
from qf.l1.context import AppContext


def run_project_workflow(
    ctx: AppContext,
    cmd: ProjectCommand,
) -> None:
    if cmd.projects_root:
        ctx.project_settings_store.set_projects_root(
            Path(ctx.config_path),
            cmd.projects_root,
        )

    if cmd.init:
        target = ctx.project_initializer.resolve_target(
            cmd.init,
            config_path=Path(ctx.config_path),
        )
        ctx.project_initializer.initialize(target)
