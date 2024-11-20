import csv
#novadiem
def novskaits(novads):
    with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        count=0
        zemnov=novads.lower()
        for rinda in lasītājs:
                if rinda[9] == zemnov.capitalize():
                    count+=1
    print(zemnov.capitalize(),"- pieturas ir",count)
#pagastiem
def pagskaits(pagasts):
     with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        i=0
        zempag=pagasts.lower()
        for rinda in lasītājs:
                if rinda[10] == zempag.capitalize():
                    i+=1
     print(zempag.capitalize(),"- pieturas ir",i)
#ciemiem pilsētām utt
def ciemskaits(ciemats):
     with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        count=0
        zemciem=ciemats.lower()
        for rinda in lasītājs:
                if rinda[11] == zemciem.capitalize():
                    count+=1
        print(zemciem.capitalize(),"- pieturas ir",count)
def novnos(novads):
     with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        zemnov=novads.lower()
        i=0
        for rinda in lasītājs:
             if rinda[9] == zemnov.capitalize():
                  i+=1
                  if rinda[8]=="":
                    print("pietura nr.",i,rinda[1])
                  else:
                       print("pietura nr.",i,rinda[1],",",rinda[8])
def novpag(pagasts):
     with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        zempag=pagasts.lower()
        i=0
        for rinda in lasītājs:
             if rinda[10] == zempag.capitalize():
                  i+=1
                  if rinda[8]=="":
                    print("pietura nr.",i,rinda[1])
                  else:
                    print("pietura nr.",i,rinda[1],", iela -",rinda[8])
def novciem(ciemats):
     with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        zemciem=ciemats.lower()
        i=0
        for rinda in lasītājs:
             if rinda[11] == zemciem.capitalize():
                  i+=1
                  if rinda[8]=="":
                    print("pietura nr.",i,"-",rinda[1])
                  else:
                    print("pietura nr.",i,"-",rinda[1],", iela -",rinda[8])
def celanr(pietura):
    with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        zempiet=pietura.lower()
        for rinda in lasītājs:
               if zempiet.capitalize()==rinda[2] and rinda[7]!=0:
                    print(rinda[2], rinda)
celanr("Dāvji")