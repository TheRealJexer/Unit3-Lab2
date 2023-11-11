# this code will read July9.csv with initial spaces after a delimiter and remove those 
# initial spaces
import csv
print("\nWith initial spaces after a delmiter:\n")
with open("July9.csv", "r") as csvfile:
    data = csv.reader(csvfile, skipinitialspace = False)
    for row in data:
        print(', '.join(row))
print("\nWithout initial spaces after a delimiter:\n")
with open("July9.csv", "r") as csvfile:
    data = csv.reader(csvfile, skipinitialspace = True)
    for row in data:
        print(', '.join(row))