import json
mani_dati={
  "name": "John Doe",
  "age": 35,
  "email": "john.doe@example.com"
}
with open("output.json", "w") as fails:
    json.dump(mani_dati, fails, indent=2)
