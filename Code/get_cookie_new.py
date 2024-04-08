from selenium import webdriver
import time
import json

# Khai báo trình duyệt Chrome
driver = webdriver.Chrome()

# Truy cập trang Twitter và đăng nhập bình thường
driver.get("https://twitter.com")
# Thực hiện đăng nhập và các tác vụ khác tại đây

# Đợi một chút để trang hoàn thành đăng nhập
time.sleep(80)

# Lấy danh sách cookie hiện tại
current_cookies = driver.get_cookies()

# Lưu cookie vào tệp với tên động (ví dụ: twitter_cookies_1.json, twitter_cookies_2.json, ...)
file_name = f"twitter_cookies_{int(time.time())}.json"
with open(file_name, "w") as cookie_file:
    json.dump(current_cookies, cookie_file)

# Đóng trình duyệt
driver.quit()

# Lần chạy sau
# Khai báo trình duyệt Chrome
driver = webdriver.Chrome()

# Truy cập trang Twitter
driver.get("https://twitter.com")

# Tìm tất cả các tệp cookie có thể đọc
cookie_files = [f"twitter_cookies_1.json", f"twitter_cookies_2.json", ...]  # Thêm các tệp đã lưu vào đây

# Thêm tất cả cookie từ các tệp đã lưu
for file_name in cookie_files:
    with open(file_name, "r") as cookie_file:
        saved_cookies = json.load(cookie_file)
        for cookie in saved_cookies:
            driver.add_cookie(cookie)

# Truy cập lại trang Twitter đã xác thực
driver.get("https://twitter.com")

# Bây giờ bạn đã đăng nhập bằng cookie và có thể thực hiện các tác vụ trên trang
