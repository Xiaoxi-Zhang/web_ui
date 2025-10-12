from playwright.sync_api import sync_playwright
import pprint


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    pprint.pprint(p.devices)
    iphone12 = p.devices["iPhone 12"]  # dict 字典
    pprint.pprint(iphone12)
    context = browser.new_context(**iphone12)
    page = context.new_page()
    page.goto("https://m.baidu.com")

    page.pause()

    context.close()
    browser.close()
