import csv

with open("Book1.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        old_number = row[0] # int(row[0]) + 1
        print(old_number) # old_number + '1'
