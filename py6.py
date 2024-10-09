#fails=open("teksts.txt","r")
#saturs=fails.read()
#print(saturs)
#fails.close()
fails=open("teksts.txt","r")
rindas_nr=1
for rinda in fails:
    print(f"{rindas_nr}.{rinda.strip()}")
    rindas_nr+=1
fails.close()