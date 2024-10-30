import csv
with open("atskaite-liepja.csv","r",encoding= "utf-8") as fails:
    lasītājs=csv.reader(fails, delimiter=";")
    for rinda in lasītājs:
            if rinda[3]=="Car":
                print(rinda)
