import time

from split_sentence import *
from export_to_photoshop_form import *


base_data = resource_path("base_data\\sentence_data.txt")
used_data = resource_path("use_data\\sentence_used.txt")
temp_used_data = resource_path("use_data\\temp_sentence_used.txt")
temp_used_data_2 = resource_path("use_data\\temp_sentence_used_2.txt")
temp_used_data_2_change = resource_path("use_data\\temp_sentence_used_2_change.txt")
temp_used_data_3 = resource_path("use_data\\temp_sentence_used_3.txt")
temp_used_data_4 = resource_path("use_data\\temp_sentence_used_4.txt")
temp_used_data_4_change = resource_path("use_data\\temp_sentence_used_4_change.txt")


upload_shopify = resource_path("temp_data\\upload_shopify.csv")




import shutil
import os

# Đường dẫn tới tệp ảnh ban đầu
source_path = resource_path("temp_data/logo.png")


def write_sentence_to_file(filename, sentence):
    try:
        with open(filename, 'a') as file:
            file.write(sentence + '\n')
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def write_sentence_to_file_temp(filename, sentence):
    try:
        with open(filename, 'w') as file:
            file.write(sentence + '\n')
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def read_sentences_from_file(filename):
    try:
        with open(filename, 'r') as file:
            sentences = file.read().splitlines()
        return sentences
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []


def find_unmatched_sentences(data_filename, used_filename):
    data_sentences = read_sentences_from_file(data_filename)
    used_sentences = read_sentences_from_file(used_filename)

    unmatched_sentences = []

    for sentence in data_sentences:
        sentence = sentence.strip()
        if sentence not in used_sentences:
            unmatched_sentences.append(sentence)

    return unmatched_sentences


def move_txt_temp_file(source_file, file_name):
    # Đường dẫn đến tệp cần di chuyển
    source_file = source_file

    # Đường dẫn đến thư mục đích
    destination_directory = resource_path("Sticker Image\\temp_data")

    # Kiểm tra xem tệp nguồn tồn tại
    if os.path.exists(source_file):
        # Kiểm tra xem thư mục đích tồn tại, nếu không tồn tại thì tạo thư mục đích
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # Đường dẫn đầy đủ đến tệp trong thư mục đích
        destination_file = os.path.join(destination_directory, f"{file_name}")

        # Di chuyển tệp từ nguồn sang đích
        shutil.move(source_file, destination_file)


def move_csv_temp_file(file):
    # Đường dẫn đến tệp cần di chuyển
    source_file = resource_path(f"temp_data\\{file}")

    # Đường dẫn đến thư mục đích
    destination_directory = resource_path("Sticker Image\\temp_data")

    # Kiểm tra xem tệp nguồn tồn tại
    if os.path.exists(source_file):
        # Kiểm tra xem thư mục đích tồn tại, nếu không tồn tại thì tạo thư mục đích
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # Đường dẫn đầy đủ đến tệp trong thư mục đích
        destination_file = os.path.join(destination_directory, f"{file}")

        # Di chuyển tệp từ nguồn sang đích
        shutil.move(source_file, destination_file)

def write_lists_to_csv(sku_list, product_name_list, output_file):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Ghi tiêu đề của cột
        writer.writerow(['SKU', 'Product Name'])
        # Ghi dữ liệu từ hai list vào file CSV
        for sku, product_name in zip(sku_list, product_name_list):
            writer.writerow([sku, product_name])


def create_csv_to_photo():

    sku_list = []
    product_name_list = []
    list_text = find_unmatched_sentences(base_data, used_data)
    if list_text:
        #write_sentence_to_file_temp(temp_used_data, "")

        i = 1
        for text in list_text:
            i = i + 1
            if i == 50:
                break
            write_sentence_to_file(used_data, text)
            #write_sentence_to_file(temp_used_data, text)
            list_split, product_name = split_sentence_2_3_and_3_3(text)

            #list_split, product_name = split_sentence_4_2_5_2(text)
            sku = export_file_to_csv(list_split, text)
            time.sleep(1)
            sku_list.append(sku)
            product_name_list.append(product_name)

    write_lists_to_csv(sku_list, product_name_list, upload_shopify)

    if os.path.exists(name_size_2):
        move_csv_temp_file("NameSize_2.csv")
    if os.path.exists(name_size_2_change):
        move_csv_temp_file("NameSize_2_change.csv")


    if os.path.exists(name_size_3):
        move_csv_temp_file("NameSize_3.csv")

    if os.path.exists(upload_shopify):
        move_csv_temp_file("upload_shopify.csv")


    if os.path.exists(name_size_4):
        move_csv_temp_file("NameSize_4.csv")

    if os.path.exists(name_size_4_change):
        move_csv_temp_file("NameSize_4_change.csv")


    if os.path.exists(temp_used_data):
        move_txt_temp_file("temp_sentence_used.txt")


    if os.path.exists(temp_used_data_2):
        move_txt_temp_file(temp_used_data_2, "temp_sentence_used_2.txt")

    if os.path.exists(temp_used_data_2_change):
        move_txt_temp_file(temp_used_data_2_change, "temp_sentence_used_2_change.txt")


    if os.path.exists(temp_used_data_3):
        move_txt_temp_file(temp_used_data_3, "temp_sentence_used_3.txt")

    if os.path.exists(temp_used_data_4):
        move_txt_temp_file(temp_used_data_4,"temp_sentence_used_4.txt")

    if os.path.exists(temp_used_data_4_change):
        move_txt_temp_file(temp_used_data_4_change,"temp_sentence_used_4_change.txt")


    return sku_list, product_name_list


if __name__ == "__main__":
    sku_list, product_name_list = create_csv_to_photo()

    print(sku_list)
    print(product_name_list)
