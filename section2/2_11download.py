from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = browser.new_page()
    page.goto("file:///D:\Project\web_ui\section2\demo.html")

    with page.expect_download() as download_info:
        page.get_by_text("点我下载").click()
    download = download_info.value
    # 保存下载的文件
    path = download.path()
    print(path)  # 文件下载路径
    print(download.url)  # 下载链接
    # 保存到本地
    download.save_as(download.suggested_filename)

    page.pause()

    context.close()
    browser.close()
