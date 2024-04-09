from pywinauto import Application
import time

# Khởi chạy trình duyệt Edge
app = Application(backend="uia").start("msedge.exe https://admin.shopify.com/store/3bc3ae-cf/products?selectedView=all")
time.sleep(5)  # Đợi cho trình duyệt mở và trang Shopify load

# Chờ cho trang Shopify load hoàn tất
main_window = app.window(title_re=".*Shopify.*")
main_window.wait('ready')

# Chờ đợi để đảm bảo đăng nhập thành công và trang cập nhật hoàn tất
time.sleep(60)

# Thêm sản phẩm mới
add_product_button = main_window.window(title="Add product")  # Tìm button "Add Product" bằng title
add_product_button.click()




# Thêm sản phẩm mới
# Ví dụ: Click vào nút "Add Product"
main_window['<add_product_button_name_or_title>'].click()

# Điền thông tin sản phẩm
# Ví dụ: Điền tên sản phẩm
main_window['<product_name_input_name_or_title>'].set_text("New Product")
# Điền giá
main_window['<product_price_input_name_or_title>'].set_text("100")
# Ví dụ: Chọn danh mục
main_window['<category_dropdown_name_or_title>'].click()
main_window['<category_option_name_or_title>'].click()

# Lưu sản phẩm
# Ví dụ: Click vào nút "Save Product"
main_window['<save_product_button_name_or_title>'].click()

# Đóng trình duyệt sau khi hoàn thành
app.kill()
