import csv
with open("atskaite-liepja.csv","r",encoding= "utf-8") as fails:
    lasītājs=csv.reader(fails, delimiter=";")
    count=0
    for rinda in lasītājs:
            if rinda[3]=="Van":
                count+=1
print(count)