import csv
import random
import pandas as pd


with open('test.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for i in range(10):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        csv_writer.writerow([x, y, 7])

    csv_file.close()

read_file = pd.read_csv('test.csv')
print(read_file)
writer = pd.ExcelWriter('test.xlsx')
read_file.to_excel(writer, index=False, header=True)
writer.save()