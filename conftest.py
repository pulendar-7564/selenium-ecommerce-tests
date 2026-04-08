# conftest.py - Shared pytest configuration and fixtures

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as regression test"
    )
