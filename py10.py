aa=["janvāris","februāris","marts","aprīlis","maijs","jūnijs","jūlijs","augusts","septembris","oktobris","novembris","decembris"]
wr=open("menesi2.txt","w")
for i in aa:
    wr.write(i +"\n")
wr.close()