"""
Aleph Olam Parser
=================

Unicode-aware parser for Hebrew symbolic quantum instructions.

Primary semantics:
- Hebrew base letters become gate instructions.
- Niqqud become primary modifiers.
- Cantillation marks become secondary modifiers.
- The exact sequence םולע ףלא unlocks the protected Aleph Olam marker.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import unicodedata

try:
    from .gates import get_gate, SymbolicGate
except ImportError:
    from gates import get_gate, SymbolicGate


ALEPH_OLAM_SECRET = "םולע ףלא"


HEBREW_BASE_START = "\u05D0"
HEBREW_BASE_END = "\u05EA"

FINAL_LETTERS = {
    "ך",
    "ם",
    "ן",
    "ף",
    "ץ",
}

NIQQUD_RANGE = range(0x05B0, 0x05BD + 1)
NIQQUD_EXTRA = {
    0x05BF,  # rafe
    0x05C1,  # shin dot
    0x05C2,  # sin dot
    0x05C4,  # upper dot
    0x05C5,  # lower dot
    0x05C7,  # qamats qatan
}

CANTILLATION_RANGE = range(0x0591, 0x05AF + 1)


@dataclass
class ParsedInstruction:
    """
    One symbolic instruction.

    A glyph is a Hebrew base letter plus any attached combining marks.
    """

    glyph: str
    base: str
    gate: Optional[SymbolicGate] = None
    niqqud: List[str] = field(default_factory=list)
    cantillation: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def known_gate(self) -> bool:
        return self.gate is not None


@dataclass
class ParsedProgram:
    """
    A parsed Aleph Olam program.
    """

    source: str
    normalized_source: str
    instructions: List[ParsedInstruction]
    aleph_olam_unlocked: bool = False
    diagnostics: List[str] = field(default_factory=list)


def normalize_source(source: str) -> str:
    """
    Normalize Hebrew Unicode into canonical composed/decomposed order.

    NFC keeps text display-friendly while stabilizing combining mark order.
    """
    return unicodedata.normalize("NFC", source)


def is_hebrew_base(ch: str) -> bool:
    return HEBREW_BASE_START <= ch <= HEBREW_BASE_END or ch in FINAL_LETTERS


def is_niqqud(ch: str) -> bool:
    return ord(ch) in NIQQUD_RANGE or ord(ch) in NIQQUD_EXTRA


def is_cantillation(ch: str) -> bool:
    return ord(ch) in CANTILLATION_RANGE


def split_hebrew_glyphs(source: str) -> List[str]:
    """
    Split text into Hebrew glyph clusters.

    This is intentionally simple and explicit:
    each Hebrew base letter begins a glyph, and Hebrew combining marks
    attach to the most recent glyph.

    Non-Hebrew whitespace and punctuation are ignored.
    """
    glyphs: List[str] = []

    for ch in source:
        if is_hebrew_base(ch):
            glyphs.append(ch)
        elif is_niqqud(ch) or is_cantillation(ch):
            if not glyphs:
                continue
            glyphs[-1] += ch
        else:
            continue

    return glyphs


def parse_glyph(glyph: str) -> ParsedInstruction:
    """
    Parse one Hebrew glyph into a symbolic instruction.
    """
    base = glyph[0]
    marks = glyph[1:]

    niqqud = [mark for mark in marks if is_niqqud(mark)]
    cantillation = [mark for mark in marks if is_cantillation(mark)]

    gate = get_gate(base)

    metadata: Dict[str, Any] = {
        "unicode_names": [unicodedata.name(ch, "UNKNOWN") for ch in glyph],
        "raw_codepoints": [f"U+{ord(ch):04X}" for ch in glyph],
    }

    return ParsedInstruction(
        glyph=glyph,
        base=base,
        gate=gate,
        niqqud=niqqud,
        cantillation=cantillation,
        metadata=metadata,
    )


def parse_program(source: str) -> ParsedProgram:
    """
    Parse Aleph Olam source text.

    The secret Aleph Olam register unlocks only when the exact normalized
    sequence םולע ףלא appears in the source.
    """
    normalized = normalize_source(source)
    glyphs = split_hebrew_glyphs(normalized)

    instructions = [parse_glyph(glyph) for glyph in glyphs]

    diagnostics: List[str] = []

    for instruction in instructions:
        if instruction.gate is None:
            diagnostics.append(
                f"Unknown gate for glyph {instruction.glyph!r} "
                f"base={instruction.base!r}"
            )

    aleph_olam_unlocked = ALEPH_OLAM_SECRET in normalized

    if aleph_olam_unlocked:
        diagnostics.append("Aleph Olam register access condition satisfied.")

    return ParsedProgram(
        source=source,
        normalized_source=normalized,
        instructions=instructions,
        aleph_olam_unlocked=aleph_olam_unlocked,
        diagnostics=diagnostics,
    )
