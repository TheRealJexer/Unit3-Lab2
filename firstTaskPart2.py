# opens and reads the July9.csv file and gives it a TAB delimiter
with open("July9.csv") as f:
    for line in f:
        read = f.readline()
        data = read.split(",")
        days = int[data[8]]
        print(data)





    