from from nodes import (
    SEPHIROT,
    get_node,
    get_node_by_hebrew,
    get_node_by_index,
)


def test_sephirot_count():
    assert len(SEPHIROT) == 10


def test_lookup_by_name():
    assert get_node("Keter").hebrew == "כתר"


def test_lookup_by_hebrew():
    assert get_node_by_hebrew("יסוד").name == "Yesod"


def test_lookup_by_index():
    assert get_node_by_index(10).name == "Malkhut"aleph_olam.nodes import QuantumNode

def test_node_creation():
    node = QuantumNode(
        name="Keter",
        hebrew="כתר",
        index=1,
        role="global_phase"
    )

    assert node.name == "Keter"
    assert node.index == 1
