masina={
"Audi":1909,
"Volkswagen":2024,
"Fiat":1903,
"Renault":1898,
"Skoda":1905
}
for x,y in masina.items():
    print(x,":",y)
if "Audi" in masina:
    print("ir, jā")
else:
    print("nē, nav")
for x,y in masina.items():
    if y<2010:
        print(x)