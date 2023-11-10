# opens and reads the July9.csv file and gives it a TAB delimiter
f_obj = open("July9.csv", mode = "r")
data = f_obj.readline()
items = data.split(",")
weatherStation = str(items[3])
year = (items[6])
month = (items[7])
for items in data:
    print(weatherStation, year, month)



    