import os
from dotenv import load_dotenv
import pytest

pytest_plugins = (
    "fixtures.settings",
)
load_dotenv()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Передаём параметры запуска браузера (headless / не headless)."""
    headless = os.getenv("CI", "false").lower() == "true"
    return {"headless": headless, "slow_mo": 2000}


@pytest.fixture
def clear_context_before_test(context):
    context.clear_cookies()
