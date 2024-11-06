import csv
with open("skoleni2.csv", "w", newline="", encoding="utf-8") as fails:
    rakst=csv.writer(fails)
    rakst.writerow(["vārds","uzvārds","klase"])
    for i in range(5):
        vards=input("ievadi vārdu")
        uzvards=input("ievadi uzvārdu")
        klase=input("ievadi klasi")
        rakst.writerow([vards,uzvards,klase])