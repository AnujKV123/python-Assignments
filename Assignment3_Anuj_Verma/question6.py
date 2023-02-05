
# 6. Create a list by picking an odd-index items from the first list and even index items from the second return third list.

def meargeOddEven(lst1, lst2):
    i=0
    j=0
    lst3 = []
    for x in range(len(lst1)+len(lst2)):
        if(x%2==0):
            lst3.append(lst1[i])
            i += 1
        else:
            lst3.append(lst2[j])
            j += 1
    return lst3


lst1 = [1, 3, 5, 7, "Hi", "Anuj"]
lst2 = [2, 4, 6, 8, "Hello", "Verma"]
print(meargeOddEven(lst1, lst2))