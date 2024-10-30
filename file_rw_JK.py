f= open("texts.txt", "r",encoding="utf-8")
print(f.readline())
#
fails= open("fruits.txt","w",encoding="utf-8")
i=0
while i<3:
    x=input("augļi")
    fails.write(x+ "\n")
    i+=1
##
y=open("texts.txt", "r",encoding= "utf-8")
count=0
for line in y: #nezinu kapēc neiet
    if "teikums" in line[0]:
        lm=(y.readline())
        print(lm)
        count+=1
    else:
        count+=1
##
l=input("auglis4")
fails.write(l)
f.close()
fails.close()
y.close()
