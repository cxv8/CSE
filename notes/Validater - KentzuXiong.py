import csv


def validate(num: str):
    if len(num) == 16:
        list_num = list(num)
        list_num.pop(15)
        print(''.join(list_num))
        return False


def reverse(num: str):
    print(num)
    return num[::-1]


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]  # String
            if validate(old_number):
                writer.writerow(row)
        print("OK")
