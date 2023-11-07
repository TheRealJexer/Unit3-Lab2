# reads each row form July9.csv and prints a list of strings
import csv
with open("July9.csv", newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ')
    for row in data:
        print(', '.join(row))