file=open("menesi2.txt","r", encoding="utf-8")
count=0
for line in file:
    if line[0] not in "T":
        count+=1
file.close()
print(count,"rindas nesākas ar t")