import csv
with open("skoleni.csv", "w", newline="", encoding="utf-8") as fails:
    rakst=csv.writer(fails)
    rakst.writerow(["vārds","uzvārds","klase"])
    vards=input("ievadi vārdu")
    uzvards=input("ievadi uzvārdu")
    klase=input("ievadi klasi")
    rakst.writerow([vards,uzvards,klase])