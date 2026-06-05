import pytest

from aleph_olam.access import sha256_text
from aleph_olam.controllers import AlephOlamController
from aleph_olam.registers import Permission


def test_public_aleph_olam_opens_with_public_phrase(monkeypatch):
    monkeypatch.delenv("ALEPH_OLAM_SECRET", raising=False)
    monkeypatch.delenv("ALEPH_OLAM_SECRET_SHA256", raising=False)

    controller = AlephOlamController()

    assert controller.open_public("אלף עולם") is True
    assert controller.can(Permission.VIEW_TOPOLOGY) is True
    assert controller.can(Permission.PARSE_SYMBOLS) is True
    assert controller.can(Permission.RUN_SAFE_SIMULATION) is True


def test_public_aleph_olam_cannot_enable_daat(monkeypatch):
    monkeypatch.delenv("ALEPH_OLAM_SECRET", raising=False)
    monkeypatch.delenv("ALEPH_OLAM_SECRET_SHA256", raising=False)

    controller = AlephOlamController()
    controller.open_public("אלף עולם")

    with pytest.raises(PermissionError):
        controller.enable_daat()


def test_secret_aleph_olam_opens_from_environment_hash(monkeypatch):
    monkeypatch.delenv("ALEPH_OLAM_SECRET", raising=False)
    monkeypatch.setenv("ALEPH_OLAM_SECRET_SHA256", sha256_text("test-secret"))

    controller = AlephOlamController()

    assert controller.open_secret("test-secret") is True
    assert controller.secret.unlocked is True
    assert controller.can(Permission.ENABLE_DAAT) is True


def test_secret_aleph_olam_can_enable_daat(monkeypatch):
    monkeypatch.delenv("ALEPH_OLAM_SECRET", raising=False)
    monkeypatch.setenv("ALEPH_OLAM_SECRET_SHA256", sha256_text("test-secret"))

    controller = AlephOlamController()
    controller.open_secret("test-secret")
    controller.enable_daat()

    assert controller.secret.daat_enabled is True


def test_public_status_does_not_expose_phase_seed(monkeypatch):
    monkeypatch.delenv("ALEPH_OLAM_SECRET", raising=False)
    monkeypatch.setenv("ALEPH_OLAM_SECRET_SHA256", sha256_text("test-secret"))

    controller = AlephOlamController()
    controller.open_secret("test-secret")
    controller.set_phase_seed(777)

    status = controller.public_status()

    assert status["secret_unlocked"] is True
    assert "phase_seed" not in status
    assert "protected_metadata" not in status
