import csv
with open("dati.csv","r") as fails:
    lasītājs=csv.reader(fails)
    for x in lasītājs:
        print(x)