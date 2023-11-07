# this code will read and output the July9.csv file as a dictionary
import csv
data = csv.DictReader(open("July9.csv"))
print("CSV file as a dictionary:\n")
for row in data:
    print(row)