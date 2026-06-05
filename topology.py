frfrom dataclasses import dataclass
from typing import Dict, List

from nodes import QuantumNode, SEPHIROT_BY_NAME


@dataclass(frozen=True)
class QuantumPath:
    name: str
    source: str
    target: str
    hebrew_gate: str
    role: str

    def endpoints(self) -> tuple[QuantumNode, QuantumNode]:
        return (
            SEPHIROT_BY_NAME[self.source],
            SEPHIROT_BY_NAME[self.target],
        )


TREE_PATHS: List[QuantumPath] = [
    QuantumPath("Path 1", "Keter", "Chokhmah", "א", "source breath; initiates branching"),
    QuantumPath("Path 2", "Keter", "Binah", "ב", "source container; forms basis"),
    QuantumPath("Path 3", "Chokhmah", "Binah", "ג", "wisdom into structure"),

    QuantumPath("Path 4", "Chokhmah", "Chesed", "ד", "creative expansion"),
    QuantumPath("Path 5", "Binah", "Gevurah", "ה", "constraint and boundary"),
    QuantumPath("Path 6", "Chesed", "Gevurah", "ו", "balance expansion with restriction"),

    QuantumPath("Path 7", "Chesed", "Tiferet", "ז", "constructive coupling to harmony"),
    QuantumPath("Path 8", "Gevurah", "Tiferet", "ח", "filtered coherence"),
    QuantumPath("Path 9", "Tiferet", "Netzach", "ט", "persistent phase flow"),
    QuantumPath("Path 10", "Tiferet", "Hod", "י", "phase into symbolic readout"),

    QuantumPath("Path 11", "Netzach", "Hod", "כ", "loop diagnostic bridge"),
    QuantumPath("Path 12", "Netzach", "Yesod", "ל", "persistent correlation"),
    QuantumPath("Path 13", "Hod", "Yesod", "מ", "encoded correlation"),
    QuantumPath("Path 14", "Yesod", "Malkhut", "נ", "foundation into observable output"),
]


PATHS_BY_NAME: Dict[str, QuantumPath] = {
    path.name: path for path in TREE_PATHS
}

PATHS_BY_GATE: Dict[str, QuantumPath] = {
    path.hebrew_gate: path for path in TREE_PATHS
}


def get_path(name: str) -> QuantumPath:
    return PATHS_BY_NAME[name]


def get_path_by_gate(hebrew_gate: str) -> QuantumPath:
    return PATHS_BY_GATE[hebrew_gate]


def adjacency() -> Dict[str, List[str]]:
    graph: Dict[str, List[str]] = {name: [] for name in SEPHIROT_BY_NAME}

    for path in TREE_PATHS:
        graph[path.source].append(path.target)
        graph[path.target].append(path.source)

    return graphom .nodes import QuantumNode

SEPHIROT = [
    QuantumNode("Keter", "כתר", 1, "global_phase"),
    QuantumNode("Chokhmah", "חכמה", 2, "superposition"),
    QuantumNode("Binah", "בינה", 3, "basis"),
    QuantumNode("Chesed", "חסד", 4, "expansion"),
    QuantumNode("Gevurah", "גבורה", 5, "filter"),
    QuantumNode("Tiferet", "תפארת", 6, "coherence"),
    QuantumNode("Netzach", "נצח", 7, "iteration"),
    QuantumNode("Hod", "הוד", 8, "readout"),
    QuantumNode("Yesod", "יסוד", 9, "entanglement"),
    QuantumNode("Malkhut", "מלכות", 10, "output"),
]
