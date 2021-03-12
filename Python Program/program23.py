#dictionaries

key = {
    "name" : "Farabi",
    "Email" : "nihadfarabi@gmail.com",
    "phone" : "01770020401",
       1 : "my id",
}

print(key["name"])
print(key.get("Email"))
print(key.get("id","not a valid key"))
print(key.get(1))