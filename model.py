import csv



def csv_data_open():      # открытие файла csv и переформатирование в list
    with open("Contacts.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        file_csv = list(file_csv)
    return file_csv



def add_info(list): 
    with open("Contacts.csv", "a", encoding="utf8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(list)


def del_info(index):  
    list_csv = csv_data_open()
    del list_csv[index]
    with open("Contacts.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)


def update_info(index, tel): 
    list_csv = csv_data_open()
    list_csv[index][3] = tel
    with open("Contacts.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)


def export_csv_csv(): 
    with open('Contacts.csv', encoding="utf8") as csvfile, open('Contacts.csv', 'w', encoding="utf8", newline='') as f:
        reader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(f, delimiter=';')
        for row in reader:
            writer.writerow(row)


def add_info_new(list):  
    export_csv_csv()
    with open("Contacts.csv", "a", encoding="utf8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(list)


def del_info_new(index):
    export_csv_csv()
    list_csv = csv_data_open()
    del list_csv[index]
    with open("Contacts.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)



def update_info_new(index, tel):  
    export_csv_csv()
    list_csv = csv_data_open()
    list_csv[index][3] = tel
    with open("Contacts.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)