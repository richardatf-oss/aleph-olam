from .nodes import QuantumNode

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
