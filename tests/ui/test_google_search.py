import pytest

pytestmark = pytest.mark.ui


def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
