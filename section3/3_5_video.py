from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(
        record_video_dir="videos/", record_video_size={"width": 648, "height": 488}
    )  # 录制视频
    page = context.new_page()
    page.goto("http://47.116.12.183/login.html")  # load

    page.get_by_placeholder("请输入用户名").fill("test")
    page.get_by_placeholder("请输入密码").fill("123456")
    page.get_by_role("button", name="立即登录").click()

    # 获取当前录制视频的路径
    video_path = page.video.path()
    print(f"视频保存路径: {video_path}")

    # context.close()  关闭页面时，视频会自动保存
    context.close()
    browser.close()
