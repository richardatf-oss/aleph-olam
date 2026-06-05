# Aleph Olam

A symbolic quantum computing language and simulator inspired by the Hebrew alphabet, niqqud, cantillation marks, and the Tree of Life.

Aleph Olam is an experimental programming language and execution environment that explores the intersection of:

- Quantum circuit design
- Symbolic computation
- Unicode-aware language engineering
- Hebrew-script based instruction systems
- Tree of Life computational topology
- Python-based quantum simulation

This project is a software engineering and language design effort. It does not claim mystical, supernatural, religious, or hidden powers. Symbolic structures are used as computational metaphors and architectural inspiration.

---

# Vision

Aleph Olam treats:

- Hebrew letters as quantum operators, gates, modes, or transformations
- Niqqud as parameter modifiers
- Cantillation marks as routing, addressing, entanglement, or metadata controls
- The Ten Sephirot as computational nodes
- The Thirty-Two Paths as transformation channels

The result is a symbolic quantum language capable of being parsed, compiled, simulated, and tested in Python.

---

# Core Architecture

## Ten Quantum Nodes

| # | Sephirah | Hebrew | Computational Role |
|---|-----------|---------|-------------------|
| 1 | Keter | כתר | Initialization and global phase |
| 2 | Chokhmah | חכמה | Superposition generation |
| 3 | Binah | בינה | Basis formation and constraints |
| 4 | Chesed | חסד | Amplitude expansion |
| 5 | Gevurah | גבורה | Projection and filtering |
| 6 | Tiferet | תפארת | Coherence and interference |
| 7 | Netzach | נצח | Iterative evolution |
| 8 | Hod | הוד | Diagnostics and readout |
| 9 | Yesod | יסוד | Entanglement bus |
| 10 | Malkhut | מלכות | Observable outputs |

---

# Language Model

## Hebrew Letters

Hebrew letters form the primary instruction set.

Example:

```text
אבגדה
```

may compile into a sequence of symbolic quantum operations.

---

## Niqqud

Niqqud act as instruction modifiers.

Examples:

- Phase rotations
- Basis selection
- Polarization controls
- Measurement parameters
- Gate configuration

Example:

```text
אַ
```

The niqqud modifies the underlying operation represented by Aleph.

---

## Cantillation Marks

Cantillation marks provide secondary semantics such as:

- Entanglement patterns
- Addressing modes
- Routing paths
- Execution ordering
- Metadata annotations

---

# Da'at Access

Da'at is treated as a hidden computational layer.

Access is controlled through explicit execution intent ("kavannah") represented as:

- Execution flags
- Authentication conditions
- Semantic proofs
- Context validation

Da'at is not exposed by default.

---

# Aleph Olam Register

The privileged register is activated by the exact Unicode sequence:

```text
םולע ףלא
```

This register may be used for:

- Global state metadata
- Simulator configuration
- Protected amplitudes
- Hidden execution context
- Da'at linkage

Access control is enforced through simulator logic and parser validation.

---

# Unicode Requirements

Aleph Olam is Unicode-native.

The parser must correctly handle:

- Hebrew letters
- Final forms
- Niqqud
- Cantillation marks
- Combining marks
- Bidirectional text
- Unicode normalization

Recommended normalization:

```python
import unicodedata

text = unicodedata.normalize("NFC", text)
```

---

# Initial Python Model

```python
from dataclasses import dataclass
import numpy as np

ComplexVec = np.ndarray

@dataclass
class QuantumNode:
    name: str
    hebrew: str
    index: int
    role: str
```

Future extensions include:

- Local state vectors
- Graph topology
- Path routing
- Gate metadata
- Entanglement management
- Circuit execution

---

# Planned Components

## Parser

- Unicode-aware lexer
- Grapheme cluster handling
- Niqqud extraction
- Cantillation extraction
- AST generation

## Compiler

- Symbol resolution
- Circuit construction
- Path validation
- Optimization passes

## Simulator

- State-vector backend
- Matrix backend
- Symbolic backend
- Measurement engine

## Visualization

- Tree of Life topology
- Circuit diagrams
- State evolution displays
- Phase-space inspection

---

# Example Future Syntax

```text
בְּרֵאשִׁית
```

Possible compilation pipeline:

```text
Source Text
      ↓
Unicode Parser
      ↓
Aleph Olam AST
      ↓
Quantum Circuit
      ↓
Simulator Backend
      ↓
Measurement Results
```

---

# Development Roadmap

## Phase 1

- Repository setup
- Core data structures
- Sephirot topology
- Unicode parser

## Phase 2

- Instruction specification
- Letter semantics
- Niqqud modifiers
- AST construction

## Phase 3

- Circuit generation
- State-vector simulator
- Measurement framework

## Phase 4

- Da'at subsystem
- Aleph Olam register
- Visualization tools

## Phase 5

- Optimization
- Plugin architecture
- Alternative backends

---

# Contributing

Contributions are welcome.

Areas of interest include:

- Quantum simulation
- Python development
- Language design
- Unicode processing
- Visualization
- Documentation

---

# License

See the LICENSE file for license information.

---

*"The letters become gates. The gates become paths. The paths become computation."*
