import csv
from datetime import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import time

import numpy as np
import pandas as pd
import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


reddit_raw_link = resource_path("temp_data/reddit_raw_link.txt")
raw_view_file = resource_path("temp_data/raw_view_file.txt")


def write_list_to_csv(list1, list2):
    try:
        with open("base_data.csv", mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            for item1, item2 in zip(list1, list2):
                writer.writerow([item1, item2])

        print(f"Đã ghi dữ liệu vào file CSV: ")
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")


def write_lines_to_text_file(lines, file_path):
    try:
        with open(file_path, 'a') as file:  # Mở tệp ở chế độ ghi thêm ('a')
            file.writelines([line + '\n' for line in lines])  # Ghi danh sách các lít và thêm dấu xuống dòng
    except Exception as e:
        print("Có lỗi khi ghi các lít vào tệp:", str(e))


def get_memes_links():
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/search?q=memes&src=typed_query")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']")))
    upload_button.click()
    pyautogui.sleep(1)
    pyautogui.write("utester.9001@gmail.com")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                               "//div[@role='button']//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")))
    upload_button.click()
    pyautogui.sleep(1)
    pyautogui.write("@Smith53017960")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Next')]")))
    upload_button.click()
    pyautogui.sleep(1)
    pyautogui.write("Chung.241089")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                               "//div[@role='button']//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")))
    upload_button.click()

    pyautogui.sleep(180)

    for i in range(1000):
        pyautogui.press('down')

    pyautogui.sleep(5)

    # Lấy mã nguồn HTML của trang
    html_source = driver.page_source

    # Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(html_source, 'html.parser')

    # Tìm tất cả các phần tử <div> có class="css-1dbjc4n"
    div_elements = soup.find_all('div', class_='css-1dbjc4n')

    # Lặp qua từng phần tử div có class='css-1dbjc4n'
    all_link = []
    for div_element in div_elements:
        # Tìm tất cả các phần tử con div trong div_element
        inner_div_elements = div_element.find_all('div', class_='css-1dbjc4n r-16y2uox r-1pi2tsx r-13qz1uu')

        # Lặp qua từng phần tử div con để lấy các liên kết
        for inner_div_element in inner_div_elements:
            # Tìm tất cả các liên kết (thẻ <a>) bên trong phần tử div con
            link_elements = inner_div_element.find_all('a')

            # Lấy các liên kết và in ra màn hình
            for link_element in link_elements:
                link_url = link_element.get('href')
                if link_url:
                    link = "https://twitter.com" + link_url
                    all_link.append(link)

    driver.quit()

    return all_link


def get_memes_links_test():
    # driver = webdriver.Chrome()
    # driver.get("https://twitter.com/search?q=memes&src=typed_query")

    # pyautogui.sleep(5)

    # html_source = driver.page_source

    with open("ten_tep.html", "r", encoding="utf-8") as html_file:
        html_content = html_file.read()
    html_source = html_content
    soup = BeautifulSoup(html_source, 'html.parser')
    div_elements = soup.find_all('div', class_='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')

    all_link = []
    all_view = []
    for div_element in div_elements:
        inner_div_elements = div_element.find_all('div', class_='css-1dbjc4n r-13awgt0 r-18u37iz r-1h0z5md')
        for inner_div_element in inner_div_elements:
            link_elements = inner_div_element.find_all('a')
            i = 0
            for link_element in link_elements:
                text_content = link_element.get_text()
                href = link_element.get('href')
                all_view.append(text_content)
                all_link.append("https://twitter.com" + href)

    return all_link, all_view

def create_sku_code():
    now = datetime.now()
    day = now.day
    formatted_day = f"{day:02}"
    month = now.month
    formatted_month = f"{month:02}"
    year = now.year
    hour = now.hour
    formatted_hour = f"{hour:02}"
    minute = now.minute
    formatted_minute = f"{minute:02}"
    second = now.second
    formatted_second = f"{second:02}"

    sku = "ST" + str(
        year) + formatted_month + formatted_day + "_" + formatted_hour + formatted_minute + formatted_second
    return sku

def move_base_data():
    csv_path = 'base_data.csv'
    df = pd.read_csv(csv_path, header=None, names=['Link', 'Views'])
    df['Timestamp'] = datetime.now()
    total_file_path = 'total_data_twitter.csv'
    df.to_csv(total_file_path, mode='a', header=False, index=False)

def get_memes_links_view():

    def get_link_view(html_source):
        soup = BeautifulSoup(html_source, 'html.parser')
        div_elements = soup.find_all('div', class_='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')
        all_link = []
        all_view = []
        for div_element in div_elements:
            inner_div_elements = div_element.find_all('div', class_='css-1dbjc4n r-13awgt0 r-18u37iz r-1h0z5md')
            for inner_div_element in inner_div_elements:
                link_elements = inner_div_element.find_all('a')
                for link_element in link_elements:
                    text_content = link_element.get_text()
                    href = link_element.get('href')
                    base_link = href.split("/analytics")[0]
                    all_view.append(text_content)
                    all_link.append("https://twitter.com" + base_link)

        write_list_to_csv(all_link, all_view)

    def get_for_loop():
        for i in range(100):
            pyautogui.press('down')
        html_source = driver.page_source
        get_link_view(html_source)

    driver = webdriver.Chrome()
    driver.get("https://twitter.com")

    cookie_files = ["twitter_cookies.json", "twitter_cookies_1699676266.json"]  # Thêm các tệp đã lưu vào đây

    # Thêm tất cả cookie từ các tệp đã lưu
    for file_name in cookie_files:
        with open(file_name, "r") as cookie_file:
            saved_cookies = json.load(cookie_file)
            for cookie in saved_cookies:
                driver.add_cookie(cookie)

    time.sleep(2)
    driver.get("https://twitter.com/search?q=memes&src=typed_query")
    time.sleep(80)
    j = 0
    for i in range(100000):
        if j == 15:
            driver.get("https://twitter.com/search?q=memes&src=typed_query")
            time.sleep(5)
            j = 0
        get_for_loop()
        j = j + 1
    driver.quit()


def convert_views(view_str):
    if pd.notna(view_str):
        view_str = str(view_str)
        matches = re.findall(r'(\d+)([KM])', view_str)
        total_views = 0
        for match in matches:
            value, unit = match
            if unit == 'K':
                total_views += int(value) * 1000
            elif unit == 'M':
                total_views += int(value) * 1000000
        return total_views
    else:
        return np.nan

def sorted_by_view():
    input_file = 'base_data.csv'
    output_file = 'output_sorted_by_view.csv'

    df = pd.read_csv(input_file, header=None)

    # Chuyển đổi lượt xem sang số nguyên
    df[1] = df[1].apply(convert_views)

    # Loại bỏ các giá trị không hợp lệ
    df = df.dropna(subset=[1])

    # Sắp xếp theo số lượt xem giảm dần
    df_sorted = df.sort_values(by=1, ascending=False)

    # Ghi vào tệp CSV mới
    df_sorted.to_csv(output_file, header=False, index=False)


def sort_by_repeat():

    input_file = 'output_sorted_by_view.csv'
    output_file = 'output_sorted_by_repeat.csv'

    # Đọc tệp CSV đã sắp xếp, sử dụng trị số cột 0 và 1
    df = pd.read_csv(input_file, header=None)

    # Tạo một Series chứa số lần xuất hiện của từng phần tử trong cột 0 (Link)
    link_counts = df[0].value_counts()

    # Thêm một cột mới là số lần duplicate (dup)
    df['Dup'] = df[0].map(link_counts) - 1  # Trừ 1 để loại bỏ một lần xuất hiện ban đầu

    # Sắp xếp theo thứ tự giảm dần của số lần duplicate
    df_sorted = df.sort_values(by='Dup', ascending=False)

    # Lấy danh sách các phần tử đã sắp xếp
    sorted_links = df_sorted[0]

    # Ghi danh sách đã sắp xếp và số lần duplicate vào tệp
    df_sorted.to_csv(output_file, index=False)

# Gọi hàm và truyền tên tệp input và output

def remove_duplicate():

    df = pd.read_csv('output_sorted_by_repeat.csv', header=None, names=['Link', 'Value1', 'Value2'])
    df_deduplicated = df.drop_duplicates(subset=['Link', 'Value2'])
    df_deduplicated.to_csv('output_deduplicated.csv', index=False)


def get_top_list():

    df_deduplicated = pd.read_csv('output_deduplicated.csv')
    df_deduplicated = df_deduplicated.iloc[2:]
    first_10_deduplicated = df_deduplicated.head(10)
    df_sorted = pd.read_csv('output_sorted_by_view.csv')
    first_10_sorted = df_sorted.head(10)
    with open('top_list_twitter.csv', 'a') as outfile:
        first_10_deduplicated.to_csv(outfile, index=False, header=False, mode='a')
        first_10_sorted.to_csv(outfile, index=False, header=False, mode='a')

    files_to_delete = ['output_deduplicated.csv', 'output_sorted_by_repeat.csv', 'output_sorted_by_view.csv', 'base_data.csv']
    for file_name in files_to_delete:
        if os.path.exists(file_name):
            os.remove(file_name)



#get_memes_links_view()
time.sleep(1)
move_base_data()
#time.sleep(1)
#sorted_by_view()
#time.sleep(1)
#sort_by_repeat()
#time.sleep(1)
#remove_duplicate()
#time.sleep(1)
#get_top_list()
#time.sleep(1)
