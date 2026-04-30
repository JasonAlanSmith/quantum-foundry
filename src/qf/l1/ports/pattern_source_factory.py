from __future__ import annotations

from pathlib import Path
from typing import Protocol

from qf.l1.ports.pattern_source import PatternSource


class PatternSourceFactory(Protocol):
    """
    Creates a PatternSource for a given project patterns directory.
    """

    def create(self, patterns_dir: Path) -> PatternSource: ...
