from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///D:/Project/web_ui/section2/alert.html")

    def handle_dialog(dialog):
        print(f"dialog message: {dialog.message}")
        print(f"dialog type: {dialog.type}")
        if dialog.type == "prompt":
            print(f"dialog default value: {dialog.default_value}")
            dialog.accept(prompt_text="hello world")
        else:
            dialog.dismiss()

    page.on("dialog", handle_dialog)

    page.locator("#alert").click()
    page.locator("#confirm").click()
    page.locator("#prompt").click()

    # page.pause()
    page.wait_for_timeout(6000)

    context.close()
    browser.close()
