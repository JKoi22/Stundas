import csv
with open("dati.csv","r") as fails:
    lasītājs=csv.reader(fails, delimiter=";")
    for rinda in lasītājs:
#        print(rinda)
        print(rinda[0])