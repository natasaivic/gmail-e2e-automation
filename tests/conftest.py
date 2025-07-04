import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

@pytest.fixture(scope="session")
def browser_context_args():
    """Configure browser context arguments."""
    return {
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
        "record_video_dir": "videos/" if os.getenv("VIDEO_ON_FAILURE", "false").lower() == "true" else None,
        "record_video_size": {"width": 1920, "height": 1080},
    }

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Configure browser launch arguments."""
    return {
        "headless": os.getenv("HEADLESS", "false").lower() == "true",
        "slow_mo": 500,  # Slow down operations for better visibility (500ms)
        "args": [
            "--start-maximized",  # Start browser maximized
            "--disable-blink-features=AutomationControlled",  # Hide automation indicators
        ]
    }

@pytest.fixture
def page(page: Page):
    """Configure page with extended timeout."""
    page.set_default_timeout(int(os.getenv("TIMEOUT", "30000")))
    return page

@pytest.fixture
def gmail_base_url():
    """Gmail base URL from environment."""
    return os.getenv("BASE_URL", "https://mail.google.com")

@pytest.fixture
def test_credentials():
    """Test account credentials from environment."""
    return {
        "email": os.getenv("GMAIL_TEST_EMAIL"),
        "password": os.getenv("GMAIL_TEST_PASSWORD"),
    }

@pytest.fixture
def test_data():
    """Test data configuration."""
    return {
        "recipient_email": os.getenv("TEST_RECIPIENT_EMAIL"),
        "subject_prefix": os.getenv("TEST_SUBJECT_PREFIX", "E2E_TEST"),
    }

def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "login: mark test as login test"
    )
    config.addinivalue_line(
        "markers", "email: mark test as email functionality test"
    )
    config.addinivalue_line(
        "markers", "search: mark test as search functionality test"
    )