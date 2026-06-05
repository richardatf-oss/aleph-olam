from dataclasses import dataclass, field
from typing import Callable, Optional, Dict, Any
import numpy as np

ComplexMatrix = np.ndarray


@dataclass
class SymbolicGate:
    """
    A symbolic gate in Aleph Olam.

    Hebrew letters represent primary gate identities.
    Niqqud and cantillation marks may later modify phase, rotation,
    addressing, entanglement, or measurement semantics.
    """

    name: str
    hebrew: str
    matrix: ComplexMatrix
    role: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    def apply(self, state: np.ndarray) -> np.ndarray:
        """
        Apply this gate to a state vector.
        """
        result = self.matrix @ state
        norm = np.linalg.norm(result)

        if norm == 0:
            raise ValueError(f"Gate {self.name} collapsed state to zero norm.")

        return result / norm


def identity_gate() -> SymbolicGate:
    return SymbolicGate(
        name="Identity",
        hebrew="א",
        matrix=np.array(
            [
                [1, 0],
                [0, 1],
            ],
            dtype=complex,
        ),
        role="Stillness / no-op / preserved coherence",
    )


def hadamard_gate() -> SymbolicGate:
    return SymbolicGate(
        name="Hadamard",
        hebrew="ח",
        matrix=(1 / np.sqrt(2))
        * np.array(
            [
                [1, 1],
                [1, -1],
            ],
            dtype=complex,
        ),
        role="Chokhmah-like branching / superposition",
    )


def phase_gate(theta: float = np.pi / 2) -> SymbolicGate:
    return SymbolicGate(
        name="Phase",
        hebrew="ת",
        matrix=np.array(
            [
                [1, 0],
                [0, np.exp(1j * theta)],
            ],
            dtype=complex,
        ),
        role="Tiferet-like phase harmony",
        metadata={"theta": theta},
    )


def projection_zero_gate() -> SymbolicGate:
    return SymbolicGate(
        name="ProjectZero",
        hebrew="ג",
        matrix=np.array(
            [
                [1, 0],
                [0, 0],
            ],
            dtype=complex,
        ),
        role="Gevurah-like filtering / boundary enforcement",
    )


DEFAULT_GATES: Dict[str, SymbolicGate] = {
    "א": identity_gate(),
    "ח": hadamard_gate(),
    "ת": phase_gate(),
    "ג": projection_zero_gate(),
}


def get_gate(symbol: str) -> Optional[SymbolicGate]:
    """
    Return a symbolic gate by Hebrew letter.
    """
    return DEFAULT_GATES.get(symbol)
