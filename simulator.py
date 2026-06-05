import numpy as np

from nodes import QuantumNode


def hadamard(node: QuantumNode) -> None:
    h = (1 / np.sqrt(2)) * np.array(
        [
            [1, 1],
            [1, -1],
        ],
        dtype=complex,
    )

    node.state = h @ node.state
    node.normalize()
