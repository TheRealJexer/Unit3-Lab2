# opens and reads the July9.csv file and gives it a TAB delimiter
import csv
with open("July9.csv", newline='') as csvfile:
    data = csv.reader(csvfile, delimiter= '\t')
    for row in data:
        print(', '.join(row))