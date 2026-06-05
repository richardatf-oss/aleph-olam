from dataclasses import dataclass, field
import numpy as np

ComplexVec = np.ndarray

@dataclass
class QuantumNode:
    name: str
    hebrew: str
    index: int
    role: str
    state: ComplexVec = field(default_factory=lambda: np.array([1+0j, 0+0j]))

SEPHIROT = [
    QuantumNode("Keter",   "כתר",   1,  "global phase, initialization, root coherence"),
    QuantumNode("Chokhmah","חכמה",  2,  "superposition generator, Hadamard-like branching"),
    QuantumNode("Binah",   "בינה",  3,  "basis formation, constraint, measurement frame"),
    QuantumNode("Chesed",  "חסד",   4,  "amplitude spreading, constructive coupling"),
    QuantumNode("Gevurah", "גבורה", 5,  "filtering, projection, destructive interference"),
    QuantumNode("Tiferet", "תפארת", 6,  "phase harmony, balanced interference, routing"),
    QuantumNode("Netzach", "נצח",   7,  "persistence, repeated evolution, loops"),
    QuantumNode("Hod",     "הוד",   8,  "readout, symbolic encoding, diagnostics"),
    QuantumNode("Yesod",   "יסוד",  9,  "entanglement bus, correlation layer"),
    QuantumNode("Malkhut", "מלכות", 10, "output manifold, observable result"),
]
