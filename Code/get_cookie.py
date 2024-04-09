import time
import json
from selenium import webdriver

# Khai báo options cho Chrome
chrome_options = webdriver.ChromeOptions()

# Nếu bạn muốn tắt thông báo:
chrome_options.add_argument("--disable-notifications")

# Nếu bạn muốn ẩn trình duyệt:
# chrome_options.add_argument("--headless")

# Khởi tạo trình duyệt Chrome với options
driver = webdriver.Chrome(options=chrome_options)


"""
# Truy cập trang Shopify và đăng nhập
driver.get("https://accounts.shopify.com/lookup?rid=7ed6e7f2-ab94-479c-8ad2-a7e4ca6a6e73&verify=1712633039-iJAGEwGBUqxtGXvR4QKVRXZpXDF6pveqyzKQJ3YK%2FRA%3Dhttps://accounts.shopify.com/lookup?rid=7ed6e7f2-ab94-479c-8ad2-a7e4ca6a6e73&verify=1712633039-iJAGEwGBUqxtGXvR4QKVRXZpXDF6pveqyzKQJ3YK%2FRA%3D")

# Đợi một chút để trang hoàn thành đăng nhập
time.sleep(90)

# Lấy danh sách cookie hiện tại
current_cookies = driver.get_cookies()

# Lưu cookie vào tệp hoặc cơ sở dữ liệu
with open("shopify_cookies.json", "w") as cookie_file:
    json.dump(current_cookies, cookie_file)
"""


# Truy cập trang Shopify
driver.get("https://accounts.shopify.com/lookup?rid=7ed6e7f2-ab94-479c-8ad2-a7e4ca6a6e73&verify=1712633039-iJAGEwGBUqxtGXvR4QKVRXZpXDF6pveqyzKQJ3YK%2FRA%3Dhttps://accounts.shopify.com/lookup?rid=7ed6e7f2-ab94-479c-8ad2-a7e4ca6a6e73&verify=1712633039-iJAGEwGBUqxtGXvR4QKVRXZpXDF6pveqyzKQJ3YK%2FRA%3D")

# Đọc danh sách cookie từ tệp
with open("shopify_cookies.json", "r") as cookie_file:
    saved_cookies = json.load(cookie_file)

# Thêm cookie đã lưu vào trình duyệt
for cookie in saved_cookies:
    driver.add_cookie(cookie)

# Truy cập lại trang Shopify đã xác thực
#driver.get("https://www.shopify.com/")
time.sleep(80)

# Bây giờ bạn đã đăng nhập bằng cookie và có thể thực hiện các tác vụ trên trang
