dict1={"name":"Anuj",
    "id":12, 
    "addr":"mohali", 
    "ls":[1,2,3,4],
    "tup": (5,6,7,8), 
    "d1":{"key":"value","k2":"v2", "key3":3}}

print(dict1)

print(type(dict1))

dict1["nickname"] = "Abhishek"

print(dict1)

del(dict1["id"])


for key,value in dict1.items():
    print(key,value)

print(dict1.items())

for key in dict1:
    print(key)
    print(dict1[key])

print(dict1["tup"][2])