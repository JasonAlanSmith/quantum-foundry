from __future__ import annotations

from typing import Any

from qf.l1.ports.inspector import Inspector
from qf.l1.ports.inspector_factory import InspectorFactory
from qf.l2.factories.inspector_registry import create_inspector


class DefaultInspectorFactory(InspectorFactory):
    def create(self, config_data: dict[str, Any]) -> Inspector:
        return create_inspector(config_data)
