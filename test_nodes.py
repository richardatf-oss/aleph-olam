from aleph_olam.nodes import QuantumNode

def test_node_creation():
    node = QuantumNode(
        name="Keter",
        hebrew="כתר",
        index=1,
        role="global_phase"
    )

    assert node.name == "Keter"
    assert node.index == 1
