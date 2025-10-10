from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///D:/Project/web_ui/section2/svg.html")

    # svg 元素定位
    svg1 = page.locator('//*[@id="box1"]//*[name()="svg"]')
    print(svg1.get_attribute("width"))

    svg2 = page.locator('//*[@id="box2"]//*[name()="svg"]')
    print(svg2.get_attribute("width"))

    page.pause()
