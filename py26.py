import json
data={
  "name": "John Doe",
  "age": 35,
  "email": "john.doe@example.com",
  "hobbies":["reading","hiking","photography"]
}
with open("outputs.json", "w") as fails:
    json.dump(data, fails, indent=2)