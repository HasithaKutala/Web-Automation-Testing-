from playwright.sync_api import expect, Page
def test_page_has_get_started_link(page:Page):
    page.goto("http://uitestingplayground.com/progressbar")
    bar = page.get_by_role("progressbar")
    start = page.get_by_role("button", name="Start")
    stop = page.get_by_role("button", name="Stop")
    start.click()
    while True:
        valuenow = int(bar.get_attribute("aria-valuenow"))
        if valuenow >=75:
            break
        else: 
            print(f"Percent is{valuenow}%")
        
    stop.click()
        