from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("file:///D:/Project/web_ui/section2/drag/snap_events.html")

    # svg 元素定位
    circle = page.locator('//*[name()="svg"]/*[name()="circle"]')
    # 元素添加监听事件
    circle.evaluate(
        'node => node.addEventListener("mousedown", function(){console.log("鼠标按下")})'
    )

    # 获取坐标
    print(circle.bounding_box())
    box = circle.bounding_box()
    # 按住元素正中心位置拖动
    page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
    page.mouse.down()
    page.mouse.move(
        box["x"] + box["width"] / 2 + 100, box["y"] + box["height"] / 2 + 100
    )
    page.mouse.up()

    page.pause()
