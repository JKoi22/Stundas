fails="menesi2.txt"
with open(fails, "r") as f:
    saturs=fails.read()
    print(saturs.lower().count("a"))
file.close()