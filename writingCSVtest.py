import csv
import random


with open('test.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for i in range(10):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        csv_writer.writerow([x, y, 7])

    csv_file.close()