"""
Aleph Olam
==========

A symbolic quantum simulator architecture inspired by Hebrew letters,
the Sephirot, and transformation paths.

This package exposes the main public API for the simulator.
"""

try:
    from nodes import QuantumNode
except ImportError:
    QuantumNode = None

try:
    from topology import SephirotTopology
except ImportError:
    SephirotTopology = None

try:
    from simulator import QuantumSimulator
except ImportError:
    QuantumSimulator = None

try:
    from parser import parse_program
except ImportError:
    parse_program = None

__all__ = [
    "QuantumNode",
    "SephirotTopology",
    "QuantumSimulator",
    "parse_program",
]
