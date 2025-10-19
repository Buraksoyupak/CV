import os
import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--base-url", action="store", default=os.getenv("BASE_URL", "http://localhost:3000"))
    parser.addoption("--headless", action="store_true", default=True)


@pytest.fixture(scope="session")
def base_url(pytestconfig: pytest.Config) -> str:
    return str(pytestconfig.getoption("--base-url"))
