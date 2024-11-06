import csv
temp=[]
with open("temp.csv", "w", newline="", encoding="utf-8") as fails:
    rakst=csv.writer(fails)
    while True:
        diena=float(input("ievadi dienas temperatūru"))
        temp.append(diena)
        rakst.writerow([diena])
        turp=input("turpināt? j/n")
        if turp.lower() !="j":
            break
vid_temp=sum(temp)/len(temp)
print("vidējā temperatūra ir", vid_temp,"C")

        