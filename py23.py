import csv
with open("darbi.csv", "w", newline="", encoding="utf-8") as fails:
    rakst=csv.writer(fails)
    rakst.writerow(["darbi"])
    darbs=input("ievadi pirmo darbu")
    rakst.writerow([darbs])
    while True:
        darbs=(input("ievadi uzdevumu: "))
        rakst.writerow([darbs])
        talak=input("vēl? jā/nē")
        x="jā"
        if talak.lower() != x:
            break