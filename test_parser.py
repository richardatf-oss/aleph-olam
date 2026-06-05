from parser import tokenize, parse


def test_single_hebrew_letter():
    tokens = tokenize("א")

    assert len(tokens) == 1
    assert tokens[0].base == "א"
    assert tokens[0].category == "hebrew_instruction"


def test_hebrew_letter_with_niqqud():
    tokens = tokenize("אָ")

    assert len(tokens) == 1
    assert tokens[0].base == "א"
    assert len(tokens[0].marks) == 1


def test_multiple_letters():
    tokens = parse("א ב ג")

    assert [token.base for token in tokens] == ["א", "ב", "ג"]
