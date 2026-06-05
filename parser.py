import unicodedata
from dataclasses import dataclass
from typing import List


HEBREW_LETTERS = set("אבגדהוזחטיכלמנסעפצקרשתךםןףץ")
NIQQUD_RANGE = range(0x0591, 0x05C8)


@dataclass(frozen=True)
class Token:
    raw: str
    base: str
    marks: tuple[str, ...]
    category: str


def normalize_source(source: str) -> str:
    return unicodedata.normalize("NFC", source)


def is_hebrew_mark(ch: str) -> bool:
    return ord(ch) in NIQQUD_RANGE and unicodedata.combining(ch) != 0


def tokenize(source: str) -> List[Token]:
    source = normalize_source(source)
    tokens: List[Token] = []

    current_base: str | None = None
    current_marks: list[str] = []

    def flush():
        nonlocal current_base, current_marks

        if current_base is None:
            return

        if current_base in HEBREW_LETTERS:
            category = "hebrew_instruction"
        else:
            category = "symbol"

        tokens.append(
            Token(
                raw=current_base + "".join(current_marks),
                base=current_base,
                marks=tuple(current_marks),
                category=category,
            )
        )

        current_base = None
        current_marks = []

    for ch in source:
        if ch.isspace():
            flush()
            continue

        if is_hebrew_mark(ch):
            if current_base is None:
                raise SyntaxError(f"Hebrew mark {repr(ch)} appears without a base letter")
            current_marks.append(ch)
            continue

        flush()
        current_base = ch

    flush()
    return tokens


def parse(source: str) -> List[Token]:
    return tokenize(source)
