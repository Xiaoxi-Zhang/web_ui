from playwright.sync_api import sync_playwright

"""
速度太快 slow_mo=1000
往右移动距离
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("file:///D:/Project/web_ui/slider.html")

    slider = page.locator(".slider").bounding_box()
    # print(slider.bounding_box())
    print(slider)
    page.mouse.move(
        x=slider["x"] + slider["width"] / 2, y=slider["y"] + slider["height"] / 2
    )
    page.mouse.down()
    page.mouse.move(
        x=slider["x"] + slider["width"] / 2 + 250, y=slider["y"] + slider["height"] / 2
    )
    page.mouse.up()

    page.pause()
