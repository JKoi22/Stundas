import csv
with open("atskaite-liepja.csv","r",encoding= "utf-8") as fails:
    lasītājs=csv.reader(fails, delimiter=";")
    next(lasītājs)
    next(lasītājs)
    count=0
    y=5
    z=3
    for i in lasītājs:
        count+=1
print(count)

