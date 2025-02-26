import pytest
from playwright.sync_api import BrowserContext, Page
@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
    context.tracing.start(
        name="playwright",
        snapshots=True,
        screenshots=True,
        sources=True,

    )
    yield
    context.tracing.stop(path="trace.zip")
def test_page(page:Page):
    page.goto("https://playwright.dev/python/")
    btn=page.get_by_role("link", name="GET STARTED")
    btn.click()
    assert page.url == "https://playwright.dev/python/docs/intro"
    