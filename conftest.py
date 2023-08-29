import pytest

"""
pytest -v -s -m users --html=reports/report.html --self-contained-html
"""


@pytest.fixture(scope="class")
def setup():
    return "Hello from setup"
