from __future__ import annotations

from pathlib import Path

from qf.l1.ports.pattern_source import PatternSource
from qf.l1.ports.pattern_source_factory import PatternSourceFactory
from qf.l2.patterns.filesystem_pattern_source import (
    FilesystemPatternSource,
)


class FilesystemPatternSourceFactory(PatternSourceFactory):
    def create(self, patterns_dir: Path) -> PatternSource:
        return FilesystemPatternSource(patterns_dir=patterns_dir)
