import csv
import pandas as pd
from csv import reader, writer
new = []
def read_csv_file(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        for row in file:
            new.append(row)
        return csv.reader(file)



df = read_csv_file('/Users/lofangyu/Documents/data_analytics/new-1.csv')
for i in range (len(new)):
    new[i] = new[i].split(',')
for i in range(7):
    print(new[i])
print(new[2][10][3:-1])

for j in range (len(new)-2):
    if new[j+2][10] == 'NO' or new[j+2][9] == 'NO':
        new[j+2].append(0)
        new[j+2].append(0)
        new[j+2].append(0)
        new[j+2].append(0)
    else:
        for k in range(4):
            distance = (int(new[j+2][10][3:-1]) - int(new[j+2][9][3:-1]) )/10
            quant_normal = int(new[j+2][11+k])/ distance
            new[j+2].append(quant_normal)

with open('normal_data_sum.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(new)