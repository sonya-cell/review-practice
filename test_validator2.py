import pytest
from validator2 import *

def test_username_valid():
    assert validate_username("user_123") is True

def test_username_too_short():
    with pytest.raises(ValueError):
        validate_username("ab")

def test_name_with_digits():
    with pytest.raises(ValueError):
        validate_name("Иван123")

def test_url_https():
    assert validate_url("https://example.com/path") is True

def test_ip_boundary():
    assert validate_ip("0.0.0.0") is True
    assert validate_ip("255.255.255.255") is True

def test_ip_invalid():
    with pytest.raises(ValueError):
        validate_ip("256.1.1.1")
