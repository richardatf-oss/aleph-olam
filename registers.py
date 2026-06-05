"""
Aleph Olam Registers
====================

Two-level control architecture:

1. Public Aleph Olam
   - Opened by the public phrase: אלף עולם
   - Safe, read-only, demo-level controller.
   - Cannot modify code, secrets, environment variables, or hidden state.

2. Secret Aleph Olam
   - Opened only through ALEPH_OLAM_SECRET_SHA256.
   - Controls Da'at, protected metadata, phase seed, and privileged mode.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional
import time


PUBLIC_ALEPH_OLAM_PHRASE = "אלף עולם"


class Permission(str, Enum):
    VIEW_TOPOLOGY = "view_topology"
    PARSE_SYMBOLS = "parse_symbols"
    RUN_SAFE_SIMULATION = "run_safe_simulation"
    VIEW_PUBLIC_DIAGNOSTICS = "view_public_diagnostics"

    ENABLE_DAAT = "enable_daat"
    SET_PHASE_SEED = "set_phase_seed"
    WRITE_PROTECTED_METADATA = "write_protected_metadata"
    PRIVILEGED_EXECUTION = "privileged_execution"


@dataclass
class PublicAlephOlamRegister:
    """
    Public-facing Aleph Olam controller.

    This is safe to expose. It may open ceremonial/public simulator mode,
    but it cannot promote itself into secret authority.
    """

    unlocked: bool = False
    permissions: set[Permission] = field(default_factory=set)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def unlock(self, phrase: str) -> bool:
        if phrase.strip() == PUBLIC_ALEPH_OLAM_PHRASE:
            self.unlocked = True
            self.permissions = {
                Permission.VIEW_TOPOLOGY,
                Permission.PARSE_SYMBOLS,
                Permission.RUN_SAFE_SIMULATION,
                Permission.VIEW_PUBLIC_DIAGNOSTICS,
            }
            self.metadata["opened_at"] = time.time()
            self.metadata["mode"] = "public_aleph_olam"
            return True

        return False

    def can(self, permission: Permission) -> bool:
        return self.unlocked and permission in self.permissions

    def require(self, permission: Permission) -> None:
        if not self.can(permission):
            raise PermissionError(
                f"Public Aleph Olam does not permit: {permission.value}"
            )


@dataclass
class SecretAlephOlamRegister:
    """
    Secret/root Aleph Olam controller.

    This register should only be unlocked after access.py verifies the
    candidate text against ALEPH_OLAM_SECRET_SHA256.
    """

    unlocked: bool = False
    kavannah: bool = False
    daat_enabled: bool = False
    phase_seed: Optional[int] = None
    permissions: set[Permission] = field(default_factory=set)
    protected_metadata: Dict[str, Any] = field(default_factory=dict)

    def unlock(self, reason: str = "secret_hash_match") -> None:
        self.unlocked = True
        self.kavannah = True
        self.permissions = {
            Permission.VIEW_TOPOLOGY,
            Permission.PARSE_SYMBOLS,
            Permission.RUN_SAFE_SIMULATION,
            Permission.VIEW_PUBLIC_DIAGNOSTICS,
            Permission.ENABLE_DAAT,
            Permission.SET_PHASE_SEED,
            Permission.WRITE_PROTECTED_METADATA,
            Permission.PRIVILEGED_EXECUTION,
        }
        self.protected_metadata["opened_at"] = time.time()
        self.protected_metadata["reason"] = reason
        self.protected_metadata["mode"] = "secret_aleph_olam"

    def can(self, permission: Permission) -> bool:
        return self.unlocked and permission in self.permissions

    def require(self, permission: Permission) -> None:
        if not self.can(permission):
            raise PermissionError(
                f"Secret Aleph Olam does not permit: {permission.value}"
            )

    def enable_daat(self) -> None:
        self.require(Permission.ENABLE_DAAT)
        self.daat_enabled = True
        self.protected_metadata["daat_enabled"] = True

    def set_phase_seed(self, seed: int) -> None:
        self.require(Permission.SET_PHASE_SEED)
        self.phase_seed = int(seed)
        self.protected_metadata["phase_seed_set"] = True

    def write_protected_metadata(self, key: str, value: Any) -> None:
        self.require(Permission.WRITE_PROTECTED_METADATA)
        self.protected_metadata[key] = value
