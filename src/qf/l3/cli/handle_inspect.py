"""Handle the `dfarm inspect` command.

This module orchestrates a data source inspection and generation run:

- Build an inspection context
- Inspect the source schema (tables/columns/types)
- Suggest strategies for each column
- Build generation plans
- Generate output to stdout or a file

This module coordinates layers; it should not contain low-level inspector or
planner implementations.
"""

from __future__ import annotations

from qf.l1_application.context import AppContext
from qf.l1_application.use_cases.inspect_use_case import run_inspect
from qf.l3.cli.base import InspectNamespace
from qf.l3.cli.run_cli_command import to_inspect_command


def handle_inspect(app_ctx: AppContext, ns: InspectNamespace) -> None:
    run_inspect(app_ctx, to_inspect_command(ns))
