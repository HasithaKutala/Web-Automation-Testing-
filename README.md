# Web-Automation-Testing - PlayWright with Python Pytest 

Playwright Authentication State Storage

A Python script that uses Playwright to automate browser actions and save authentication state (cookies, localStorage, etc.) to a JSON file. Useful for preserving sessions across tests or automating login workflows.

The files test_app.py, check.py how to automate browser interactions using Playwright and pytest. The test simulates user actions such as navigating through a website, clicking links, filling out forms, and capturing screenshots. The goal is to validate functionality, such as submitting an email and navigating to a confirmation page, while ensuring that the workflow behaves as expected.

The record.py has the code- clicks the "GET STARTED" link, switches between light and dark modes, and records the session video. It then checks if the page redirects correctly to the expected URL.

Trace Generator and Viewer tools

This test script uses Playwright with pytest to generate a trace of browser interactions during the test execution. 

Trace Generation:
Trace Capture: The trace_test fixture automatically starts tracing for every test, capturing snapshots, screenshots, and sources.
Trace Output: At the end of the test, the trace is saved as a trace.zip file, which contains detailed information about the browser interactions.
Trace Viewer:
The generated trace (trace.zip) can be opened using Playwright's Trace Viewer tool, allowing you to visualize and debug the test interactions step by step.
