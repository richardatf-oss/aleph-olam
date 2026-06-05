"""
Aleph Olam
==========

Symbolic Hebrew-inspired quantum simulator architecture.

Public Aleph Olam is safe and user-facing.
Secret Aleph Olam is protected by environment-hash access policy.
"""

from .access import AlephOlamAccessPolicy, AccessDecision, sha256_text
from .controllers import AlephOlamController
from .registers import (
    Permission,
    PublicAlephOlamRegister,
    SecretAlephOlamRegister,
)

__all__ = [
    "AlephOlamAccessPolicy",
    "AccessDecision",
    "sha256_text",
    "AlephOlamController",
    "Permission",
    "PublicAlephOlamRegister",
    "SecretAlephOlamRegister",
]
