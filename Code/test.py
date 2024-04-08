import csv


def read_csv_file():
    file_name = "NameSize_4.csv"
    csv_file = f"C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\temp_data\\{file_name}"
    list_1 = []

    with open(csv_file, newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        for row_number, row in enumerate(csv_reader, start=1):
            try:
                if row and len(row) > 0:  # Check if the row is not empty and has at least one element
                    list_1.append(row[0])
            except IndexError as e:
                print(f"Error in row {row_number}: {e}")

    return list_1[1:] if list_1 else []

print(len(read_csv_file()))
print(read_csv_file())