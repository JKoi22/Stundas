import csv
dati= [
["vārds","vecums","pilsēta"],
["Jānis","30","Rīga"],
["Anna","25","Liepāja"]
]
with open('jauns_fails.csv', 'w', newline='') as fails:
    rakstītājs = csv.writer(fails)
    rakstītājs.writerows(dati)