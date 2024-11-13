import csv
with open("preces.csv","r",encoding= "utf-8") as fails:
    lasītājs=csv.reader(fails, delimiter=";")
    for rinda in lasītājs:
         if rinda[2]==20:
            print(rinda[0])

#
with open("rezultati.csv","w",encoding= "utf-8") as spor:
    ieraks=csv.writer(spor)
    ieraks.writerow(["sportists","metiens","metiens2","metiens3","videjais"])
    for i in range(2):
            sportists=input("vārds")
            sprez=int(input("rezultāts"))
            sprez2=int(input("rezultāts"))
            sprez3=int(input("rezultāts"))
            vid= sprez+sprez2+sprez3
            x=vid/3
            ieraks.writerow([sportists,sprez,sprez2,sprez3,x])

            


