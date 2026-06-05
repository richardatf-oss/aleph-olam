from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class QuantumNode:
    name: str
    hebrew: str
    index: int
    role: str
    metadata: Dict[str, Any] = field(default_factory=dict)
