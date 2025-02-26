def test_page_has_get_started_link(page):
    page.goto("https://albertedwards.beehiiv.com/")
    page.get_by_role("link", name="How To Get More Data Science Interviews").click()
    page.get_by_role("link", name="Send Me The Guide").click()
    email_input=page.get_by_placeholder("Enter Your Email")
    email_input.fill("Hasitha.kutala@gmail.com")
    page.get_by_role("button", name="Subscribe").click()
    page.screenshot(path="datascience.png")
    assert page.url == "https://albertedwards.beehiiv.com/subscribe"