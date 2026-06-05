from dataclasses import dataclass, field
import numpy as np

ComplexVec = np.ndarray


@dataclass
class QuantumNode:
    name: str
    hebrew: str
    index: int
    role: str
    state: ComplexVec = field(
        default_factory=lambda: np.array([1 + 0j, 0 + 0j], dtype=complex)
    )

    def normalize(self) -> None:
        norm = np.linalg.norm(self.state)
        if norm == 0:
            raise ValueError(f"Cannot normalize zero state for node {self.name}")
        self.state = self.state / norm


SEPHIROT = [
    QuantumNode("Keter", "כתר", 1, "global phase, initialization, root coherence"),
    QuantumNode("Chokhmah", "חכמה", 2, "superposition generator, Hadamard-like branching"),
    QuantumNode("Binah", "בינה", 3, "basis formation, constraint, measurement frame"),
    QuantumNode("Chesed", "חסד", 4, "amplitude spreading, constructive coupling"),
    QuantumNode("Gevurah", "גבורה", 5, "filtering, projection, destructive interference"),
    QuantumNode("Tiferet", "תפארת", 6, "phase harmony, balanced interference, routing"),
    QuantumNode("Netzach", "נצח", 7, "persistence, repeated evolution, loops"),
    QuantumNode("Hod", "הוד", 8, "readout, symbolic encoding, diagnostics"),
    QuantumNode("Yesod", "יסוד", 9, "entanglement bus, correlation layer"),
    QuantumNode("Malkhut", "מלכות", 10, "output manifold, observable result"),
]


SEPHIROT_BY_NAME = {node.name: node for node in SEPHIROT}
SEPHIROT_BY_HEBREW = {node.hebrew: node for node in SEPHIROT}
SEPHIROT_BY_INDEX = {node.index: node for node in SEPHIROT}


def get_node(name: str) -> QuantumNode:
    return SEPHIROT_BY_NAME[name]


def get_node_by_hebrew(hebrew: str) -> QuantumNode:
    return SEPHIROT_BY_HEBREW[hebrew]


def get_node_by_index(index: int) -> QuantumNode:
    return SEPHIROT_BY_INDEX[index]
