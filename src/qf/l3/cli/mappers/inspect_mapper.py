from pathlib import Path

from qf.l1.commands.inspect_command import InspectCommand
from qf.l3.cli.base import InspectNamespace


def to_inspect_command(ns: InspectNamespace) -> InspectCommand:
    return InspectCommand(
        project=Path(ns.project),
        rows=ns.rows,
        schema=ns.schema,
        insert_batch_size=ns.insert_batch_size,
        output_file=ns.output_file,
    )
