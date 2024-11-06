import csv
temp=[]
with open("nedela.csv", "w", newline="", encoding="utf-8") as fails:
    rakst=csv.writer(fails)
    for i in range(7):
        diena=float(input("ievadi dienas temperatūru"))
        temp.append(diena)
        rakst.writerow([diena])
temp.sort()
print(temp[0],temp[-1])