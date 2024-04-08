from selenium import webdriver
import time
import json

# Khai báo trình duyệt Edge
driver = webdriver.Edge(executable_path='đường/dẫn/msedgedriver.exe')

# Truy cập trang Shopify và đăng nhập
driver.get("https://admin.shopify.com/store/3bc3ae-cf/products?selectedView=all")
# Thực hiện đăng nhập và các tác vụ khác tại đây

# Đợi một chút để trang hoàn thành đăng nhập
time.sleep(200)

# Lấy danh sách cookie hiện tại
current_cookies = driver.get_cookies()

# Lưu cookie vào tệp hoặc cơ sở dữ liệu
with open("shopify_cookies.json", "w") as cookie_file:
    json.dump(current_cookies, cookie_file)

# Đóng trình duyệt
driver.quit()

# Lần chạy sau
# Khai báo trình duyệt Edge
driver = webdriver.Edge(executable_path='đường/dẫn/msedgedriver.exe')

# Truy cập trang Shopify
driver.get("https://admin.shopify.com/store/3bc3ae-cf/products?selectedView=all")

# Đọc danh sách cookie từ tệp
with open("shopify_cookies.json", "r") as cookie_file:
    saved_cookies = json.load(cookie_file)

# Thêm cookie đã lưu vào trình duyệt
for cookie in saved_cookies:
    driver.add_cookie(cookie)

# Truy cập lại trang Shopify đã xác thực
driver.get("https://admin.shopify.com/store/3bc3ae-cf/products?selectedView=all")
time.sleep(80)

# Bây giờ bạn đã đăng nhập bằng cookie và có thể thực hiện các tác vụ trên trang
