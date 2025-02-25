#logging in gmail and saving, reusing our authentication

from playwright.sync_api import sync_playwright
from creds import EMAIL, PASSWORD 
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless= False, slow_mo=500)
    context = browser.new_context() # broswer context allow us to store authentication state when we login 
    page=context.new_page()
    page.goto("https://accounts.google.com")

    #Enter email 
    email_input= page.get_by_label("Email or phone")
    email_input.fill(EMAIL)
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Try again")

    #save authentication state 
    context.storage_state(path="playwr/.auth/state.json")


    context.close()