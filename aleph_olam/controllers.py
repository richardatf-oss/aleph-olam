"""
Aleph Olam Controllers
======================

The controller binds the two registers together:

1. Public Aleph Olam
   - Opened by the public phrase.
   - Safe, user-facing, subordinate.

2. Secret Aleph Olam
   - Opened only through the environment-hash access policy.
   - Root authority over Da'at, phase seed, and protected metadata.

The public controller can never promote itself into secret authority.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .access import AlephOlamAccessPolicy
from .registers import (
    Permission,
    PublicAlephOlamRegister,
    SecretAlephOlamRegister,
)


@dataclass
class AlephOlamController:
    """
    High-level authority controller for simulator sessions.
    """

    public: PublicAlephOlamRegister = field(default_factory=PublicAlephOlamRegister)
    secret: SecretAlephOlamRegister = field(default_factory=SecretAlephOlamRegister)
    access_policy: AlephOlamAccessPolicy = field(default_factory=AlephOlamAccessPolicy)
    diagnostics: List[str] = field(default_factory=list)

    def open_public(self, phrase: str) -> bool:
        """
        Open public Aleph Olam mode.

        This grants safe permissions only.
        """
        granted = self.public.unlock(phrase)

        if granted:
            self.diagnostics.append("Public Aleph Olam opened.")
        else:
            self.diagnostics.append("Public Aleph Olam phrase did not match.")

        return granted

    def open_secret(self, candidate_text: str) -> bool:
        """
        Open secret Aleph Olam mode through the environment-hash policy.

        The protected phrase is not stored in this source file.
        """
        decision = self.access_policy.check(candidate_text)

        if decision.granted:
            self.secret.unlock(reason=decision.reason)
            self.diagnostics.append(decision.reason)
            return True

        self.diagnostics.append(decision.reason)
        return False

    def can(self, permission: Permission) -> bool:
        """
        Secret authority includes all public authority.
        """
        return self.secret.can(permission) or self.public.can(permission)

    def require(self, permission: Permission) -> None:
        """
        Require either public or secret permission.

        Use secret-only methods for privileged operations.
        """
        if not self.can(permission):
            raise PermissionError(f"Aleph Olam permission denied: {permission.value}")

    def enable_daat(self) -> None:
        """
        Enable Da'at.

        This is secret-only.
        """
        self.secret.enable_daat()
        self.diagnostics.append("Da'at enabled by secret Aleph Olam.")

    def set_phase_seed(self, seed: int) -> None:
        """
        Set protected phase seed.

        This is secret-only.
        """
        self.secret.set_phase_seed(seed)
        self.diagnostics.append("Protected phase seed set.")

    def write_protected_metadata(self, key: str, value: Any) -> None:
        """
        Write protected metadata.

        This is secret-only.
        """
        self.secret.write_protected_metadata(key, value)
        self.diagnostics.append(f"Protected metadata written: {key}")

    def public_status(self) -> Dict[str, Any]:
        """
        Safe public status.

        This deliberately does not expose protected metadata,
        secret candidate text, environment variables, or phase seed values.
        """
        return {
            "public_unlocked": self.public.unlocked,
            "secret_unlocked": self.secret.unlocked,
            "daat_enabled": self.secret.daat_enabled,
            "public_permissions": sorted(p.value for p in self.public.permissions),
            "secret_permissions": sorted(p.value for p in self.secret.permissions),
            "diagnostics": list(self.diagnostics),
        }
