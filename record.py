from playwright.sync_api import Browser, Page
def test_page_has_get_started_link(browser: Browser):
    context = browser.new_context(
        record_video_dir="videp/"
    )
    page=context.new_page()
    page.goto("https://playwright.dev/python/")
    btn=page.get_by_role("link", name="GET STARTED")
    btn.click()
    theme = page.get_by_title("Switch between dark and light mode (currently light mode)").click()
    assert page.url == "https://playwright.dev/python/docs/intro"
    