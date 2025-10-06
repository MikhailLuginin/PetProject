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
