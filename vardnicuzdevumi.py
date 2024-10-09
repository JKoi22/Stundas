#1. uzd
valgalv={
"Latvija": "Rīga",
"Igaunija":"Tallina",
"Polija": "Varšava"
}
for x,y in valgalv.items():
    print(x,",",y)
#2. uzd
masinas={
"Audi":1997,
"BMW":2012,
"Opel":1997
}
masinas["BMW"]=2021
print(masinas)
#3. uzd
auglis={
"banāns":"1,50 EUR",
"ābols":"2 EUR",
"bumbieris":"3 EUR"
}
auglis["aplelsīns"]="1,50 EUR"
print(auglis)
#4 uzd
skolniki={
"Renards":7,
"Viktors":5,
"Alfrēds":9,
"Regnārs":7
}
if "Jānis" in skolniki:
    print(skolniki.values("Jānis"))
else:
    print("Jāņa te nav")
#5 uzd
dzivnieki={
"suns":20,
"kaķis":10,
"kaza":40,
"alpaka":80,
"govs":190
}
for x,y in dzivnieki.items():
    print(x,y,"kg")
#6. uzd
gramatas={
"Dž. Orvels":"Dzīvnieku ferma",
"Imants Ziedonis":"epifānijas",
"Rainis":"Dzejoļu krājums"
}
gramatas.pop("Rainis")
print(gramatas)
#7 uzd
pilsetas={
    "Rīga":{
        "iedzīvotāju skaits":"627 487",
        "Valsts" :"Latvija",
    },
    "Viļņa":{
        "iedzīvotāju skaits":"544 386",
        "Valsts":"Lietuva"
    }
}
print(pilsetas["Rīga"]["iedzīvotāju skaits"])
print(pilsetas["Rīga"]["Valsts"])
print(pilsetas["Viļņa"]["iedzīvotāju skaits"])
print(pilsetas["Viļņa"]["Valsts"])