"""Tests that settings.json is valid and free of caching foot-guns."""

import json

import pytest

from conftest import SETTINGS_FILE

pytestmark = pytest.mark.static


@pytest.fixture
def settings():
    return json.loads(SETTINGS_FILE.read_text())


def test_no_default_mode(settings):
    """settings.json must not set defaultMode — plan mode
    enforcement is unreliable; the blueprint must not depend on it."""
    permissions = settings.get("permissions", {})
    assert "defaultMode" not in permissions


def test_no_conditional_tool_loading(settings):
    """No defer_loading in settings — the tool set must be fixed
    per prompt caching rules (changing tools mid-session
    invalidates the cache prefix)."""
    assert "defer_loading" not in SETTINGS_FILE.read_text(), (
        "settings.json must not use defer_loading"
    )
