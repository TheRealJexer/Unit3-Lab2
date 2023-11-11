# reads and displays the July9.csv file as a list
import csv
with open("July9.csv", newline= '') as f:
    reader = csv.reader(f)
    data_list = list(reader)
print(data_list)