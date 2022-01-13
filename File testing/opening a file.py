import csv

with open('files to test/data.csv') as a:
    dic = csv.DictReader(a)
    for row in dic:
        print(row['name'])