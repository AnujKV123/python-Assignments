
# 7. Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list by
# using list comprehension 

# dict ={"key1":1234, "k2":"ram"}

# list= [1234,"ram"]

def checkList(dictX, listX):
    ans = [item  for item in listX if item in dictX.values()]
    return ans

dictX ={"key1":1234, "k2":"ram"}
listX= [1234,"ram", "xyz", "Rahul", "Anuj", 123, 212, 22]
print(checkList(dictX, listX))