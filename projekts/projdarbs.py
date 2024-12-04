import csv
def novskaits(novads):
    with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        count=0
        zemnov=novads.lower()
        for rinda in lasītājs:
                if rinda[9] == zemnov.capitalize():
                    count+=1
    print(zemnov.capitalize(),"- pieturas ir",count)
    y=input("faila nosaukums, formātā y.csv")
    with open(y, "w", newline="", encoding="utf-8") as fails:
     rakst=csv.writer(fails)
     rakst.writerow([zemnov.capitalize(),"- pieturas ir",count])
def pagskaits(pagasts):
     with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        i=0
        zempag=pagasts.lower()
        for rinda in lasītājs:
                if rinda[10] == zempag.capitalize():
                    i+=1
     print(zempag.capitalize(),"- pieturas ir",i)
     y=input("faila nosaukums, formātā y.csv")
     with open(y, "w", newline="", encoding="utf-8") as fails:
      rakst=csv.writer(fails)
      rakst.writerow([zempag.capitalize(),"- pieturas ir",i])
def ciemskaits(ciemats):
     with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        count=0
        zemciem=ciemats.lower()
        for rinda in lasītājs:
                if rinda[11] == zemciem.capitalize():
                    count+=1
        print(zemciem.capitalize(),"- pieturas ir",count)
        y=input("faila nosaukums, formātā y.csv")
        with open(y, "w", newline="", encoding="utf-8") as fails:
          rakst=csv.writer(fails)
          rakst.writerow([zemciem.capitalize(),"- pieturas ir",count])
def novnos(novads):
     with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        zemnov=novads.lower()
        i=0
        aa=[]
        y=input("faila nosaukums, formātā y.csv")
        for rinda in lasītājs:
             if rinda[9] == zemnov.capitalize():
                  i+=1
                  print("pietura nr.",i,rinda[1])
                  aa.append(["pietura nr.",i,rinda[1]])
     with open(y, "w", newline="", encoding="utf-8") as fails:
                    rakst=csv.writer(fails)
                    rakst.writerow(aa)
def novpag(pagasts):
     with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        zempag=pagasts.lower()
        i=0
        y=input("faila nosaukums, formātā y.csv")
        aa=[]
        for rinda in lasītājs:
             if rinda[10] == zempag.capitalize():
                  i+=1
                  if rinda[8]=="":
                    print("pietura nr.",i,rinda[1])
                    aa.append(["pietura nr.",i,rinda[1]])
                  else:
                    print("pietura nr.",i,rinda[1],", iela -",rinda[8])
                    aa.append(["pietura nr.",i,rinda[1],", iela -",rinda[8]])
     with open(y, "w", newline="", encoding="utf-8") as fails:
                    rakst=csv.writer(fails)
                    rakst.writerow(aa)
def novciem(ciemats):
     with open("busstops.csv", "r", newline="", encoding="utf-8") as fails:
        lasītājs=csv.reader(fails, delimiter=",")
        zemciem=ciemats.lower()
        i=0
        y=input("faila nosaukums, formātā y.csv")
        aa=[]
        for rinda in lasītājs:
             if rinda[11] == zemciem.capitalize():
                  i+=1
                  if rinda[8]=="":
                    print("pietura nr.",i,"-",rinda[1])
                    aa.append(["pietura nr.",i,"-",rinda[1]])
                  else:
                    print("pietura nr.",i,"-",rinda[1],", iela -",rinda[8])
                    aa.append(["pietura nr.",i,"-",rinda[1],", iela -",rinda[8]])
     with open(y, "w", newline="", encoding="utf-8") as fails:
               rakst=csv.writer(fails)
               rakst.writerow(aa)
izvēlne=int(input("ievadi skaitli 1-7 1=skaits novadā, 2=skaits pagastā 3=skaits ciemā/pilsētā 4=novada pieturu nosaukumi 5=pagasta pieturu nosaukumi 6=ciema/pilsēta 7= ceļa numurs pieturai"))
if izvēlne==1:
          x=input("ievadi novadu")
          (novskaits(x))
elif izvēlne==2:
          x=input("ievadi pagastu")
          (pagskaits(x))
elif izvēlne==3:
          x=input("ievadi ciemu/pilsētu")
          (ciemskaits(x))
elif izvēlne==4:
          x=input("ievadi novadu")
          (novnos(x))
elif izvēlne==5:
          x=input("ievadi pagastu")
          (novpag(x))
elif izvēlne==6:
          x=input("ievadi ciems/pilsēta")
          (novciem(x))
else:
     print("ievadi pareizu skaitli")