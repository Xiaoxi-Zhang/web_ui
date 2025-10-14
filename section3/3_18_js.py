"""
page.evaluate()
执行js，返回调用执行的结果
"""

from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")

    res1 = page.evaluate("1+3")
    print(res1)
    x = 10
    res2 = page.evaluate(f"1+ {x}")
    print(res2)

    res3 = page.evaluate('()=> "hello world!"')
    print(res3)

    res4 = page.evaluate("document.title")
    print(res4)

    js = """
    document.getElementById('username').value='yoyo';
    document.getElementById('password').value='aa123456';
    document.getElementById('loginBtn').click();
    """
    page.evaluate(js)

    page.pause()

    context.close()
    browser.close()
