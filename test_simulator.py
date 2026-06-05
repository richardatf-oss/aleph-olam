import numpy as np

from nodes import get_node
from simulator import hadamard


def test_hadamard():
    node = get_node("Chokhmah")

    node.state = np.array([1 + 0j, 0 + 0j])

    hadamard(node)

    assert np.isclose(abs(node.state[0]), 1 / np.sqrt(2))
    assert np.isclose(abs(node.state[1]), 1 / np.sqrt(2))
