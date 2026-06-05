from parser import parse_program, ALEPH_OLAM_SECRET


def test_parse_known_gate_aleph():
    program = parse_program("א")

    assert len(program.instructions) == 1
    assert program.instructions[0].base == "א"
    assert program.instructions[0].known_gate is True


def test_parse_known_gate_chet():
    program = parse_program("ח")

    assert len(program.instructions) == 1
    assert program.instructions[0].base == "ח"
    assert program.instructions[0].known_gate is True


def test_niqqud_attaches_to_base_letter():
    program = parse_program("אָ")

    assert len(program.instructions) == 1
    assert program.instructions[0].base == "א"
    assert len(program.instructions[0].niqqud) >= 1


def test_aleph_olam_secret_unlocks_only_exact_sequence():
    locked = parse_program("אלף עולם")
    unlocked = parse_program(ALEPH_OLAM_SECRET)

    assert locked.aleph_olam_unlocked is False
    assert unlocked.aleph_olam_unlocked is True
