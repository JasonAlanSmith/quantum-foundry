"""Dispatch application work based on parsed CLI arguments.

This module receives an argparse namespace, boots the application context, and
dispatches to the appropriate handler.

Responsibilities:
- Build :class:`~qf.cli.base.AppContext` via bootstrap
- Route to subcommand handlers

This module does not:
- Parse arguments (argparse does that)
- Implement pipeline work directly
"""

import logging
from argparse import ArgumentParser, Namespace

from qf.l3.bootstrap import boot_app_from_ns
from qf.l3.cli.run_cli_command import run_cli_command

logger = logging.getLogger("dfarm")


def dispatch(parser: ArgumentParser, ns: Namespace) -> int:
    """Dispatch CLI argument processing. Returns a process exit code."""
    ARGPARSE_ERROR_CODE = 2

    ctx = boot_app_from_ns(ns)
    result = run_cli_command(ctx, ns)

    if result.exit_code == ARGPARSE_ERROR_CODE:
        parser.print_help()

    return result.exit_code
