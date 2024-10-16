try:
    fails=open("tekstis.txt", "r")
    fails.close()
except FileNotFoundError:
    print("fails netika atrasts!")