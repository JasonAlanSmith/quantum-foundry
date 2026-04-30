"""Compatibility wrapper for project CLI handling.

Project orchestration now lives in the application layer. This module remains
as a thin bridge for any legacy callers that still import `handle_project`.
"""

from __future__ import annotations

from qf.l1_application.commands.project_command import ProjectCommand
from qf.l1_application.context import AppContext
from qf.l1_application.project_workflow import run_project_workflow


def handle_project(ctx: AppContext, cmd: ProjectCommand) -> None:
    """Delegate project command handling to the application workflow."""
    run_project_workflow(ctx, cmd)
