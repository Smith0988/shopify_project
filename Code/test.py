import re


def xu_ly_chuoi(chuoi):
    # Loại bỏ ký tự không phải chữ cái hoặc số
    text_anpha = re.sub(r'[^a-zA-Z0-9\s]', '', chuoi)
    # Thay thế khoảng trắng bằng dấu -
    text_no_space = text_anpha.replace(' ', '-')
    # Chuyển đổi thành chữ thường
    text_handle = text_no_space.lower()
    return text_handle

# Đoạn văn bản ban đầu
van_ban = "6Pcs(5IN) I Don't Care What The Bible Says Bumper Sticker"

# Xử lý chuỗi
ket_qua = xu_ly_chuoi(van_ban)

print("Kết quả:", ket_qua)