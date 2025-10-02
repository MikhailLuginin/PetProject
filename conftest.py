import os

import pytest

pytest_plugins = (
    "fixtures.settings",
)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


# @pytest.fixture(scope="session")
# def launch_options():
#     """Настройки запуска браузера (headless / headed)"""
#     if os.getenv("CI") == "true":
#         return {
#             "headless": True,
#         }
#     else:
#         return {
#             "headless": False,
#         }
@pytest.fixture(scope="session")
def launch_options():
    """Настройки запуска браузера (headless / headed)"""
    if os.getenv("CI") is None:
        return {
            "headless": False,
        }
    else:
        return {
            "headless": True,
        }
