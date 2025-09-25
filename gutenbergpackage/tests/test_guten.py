import pytest
from gutenbergpkg import list_aliases


def test_list_aliases_returns_list():
    aliases = list_aliases()
    assert isinstance(aliases, list)
