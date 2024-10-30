import csv
with open("darbinieki.csv","r",encoding= "utf-8") as fails:
    lasītājs=csv.reader(fails, delimiter=",")
    next(lasītājs)
    for ierak in lasītājs:
        vards=ierak[0]
        nodarb=ierak[3]
        print(f"{vards}-{nodarb}")
fails.close()   