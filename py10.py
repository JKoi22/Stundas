aa=["janvāris","februāris","marts","aprīlis","maijs","jūnijs","jūlijs","augusts","septembris","oktobris","novembris","decembris"]
wr=open("menesi2.txt","w", encoding= "utf-8")
for i in aa:
    wr.write(i +"\n")
wr1=open("menesi2.txt","w")
print(wr1)
wr.close()
wr1.close()