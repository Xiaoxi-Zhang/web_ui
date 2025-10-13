"""
text_content() 用来获取某个元素内所有文本内容，包含子元素内容，隐藏元素也能获取。
inner_text() 的返回值会被格式化，但是text_content()的返回值不会被格式化
最重要的区别 inner_text()返回的值，依赖于页面的显示，text_content()依赖于代码的内容
"""

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cnblogs.com/yoyoketang/?_wv=1031")

    # 依赖于页面的显示 UI看得到的内容
    res = page.locator("#blogTitle")
    print(res.inner_text())
    print("-----------------------------")
    # 依赖于html 代码的内容 隐藏的文本也可以获取
    print(res.text_content())

    # all_inner_texts() 与 all_text_contents()
    print(res.all_text_contents())
    print(res.all_inner_texts())

    page.pause()

    context.close()
    browser.close()
