from playwright.sync_api import sync_playwright


def dump_frame_tree(frame, indent):
    print(indent + frame.name + "@" + frame.url)
    for child in frame.child_frames:
        dump_frame_tree(child, indent + "    ")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()
    page.goto("file:///D:/Project/web_ui/2_23%20iframe_xuexi/home.html")

    # 1.定位iframe 元素
    # frame1 = page.frame_locator('[name="yoyo"]')
    # print(frame1)
    # frame1.locator("#username").type("yoyo", delay=100)
    # frame1.locator("#password").type("123456", delay=100)

    # 2.frame(name, url)
    # frame2 = page.frame(name="yoyo")
    # print(frame2)
    # frame2.locator("#username").fill("yoyo")
    # frame2.locator("#password").fill("123456")

    # print(page.main_frame)  # 主 iframe
    # main = page.main_frame
    # print(main.child_frames)  # 查看所有的子 iframe
    # # 查看全部 包含主 iframe
    # print(page.frames)

    # for item in page.frames:
    #     print(item.name)
    #     print(item.url)

    # 遍历页面上 iframe 的层级结构
    # dump_frame_tree(page.main_frame, "")

    # 动态的id的iframe 如何定位
    # css 的正则匹配
    # frame3 = page.frame_locator('[id^="iframe-auto"]')
    # print(frame3)
    # frame3.locator("#username").fill("yoyo")
    # frame3.locator("#password").fill("123456")

    # xpath contains
    # frame4 = page.frame_locator('//*[contains(@id, "iframe-auto")]')
    # frame4.locator("#username").fill("yoyo")
    # frame4.locator("#password").fill("123456")

    # src 属性定位
    # frame5 = page.frame_locator('[src="down.html"]')
    # frame5.locator("#username").fill("yoyo")
    # frame5.locator("#password").fill("123456")

    # name url 属性定位
    # name 属性 id/name 全称
    # frame6 = page.frame(name="yoyo")
    # frame6.locator("#username").fill("yoyo")
    # frame6.locator("#password").fill("123456")

    # frame7 = page.frame(name="yoyo2")
    # frame7.locator("#alert").click()

    # url 地址 包含部分
    # frame8 = page.frame(url="http://47.116.12.183/login.html")
    # frame8.locator("#username").fill("yoyo")
    # frame8.locator("#password").fill("123456")

    # 2层的iframe
    # frame9 = page.frame(name="yoyo2").frame_locator('[src="down.html"]')
    # frame9.locator("#username").fill("yoyo")
    # frame9.locator("#password").fill("123456")

    page.pause()
