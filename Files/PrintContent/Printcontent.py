import csv
with open('dep.csv')as files:
    data=csv.reader(files)
    for row in data:
        print(row[0],row[1],row[2])
