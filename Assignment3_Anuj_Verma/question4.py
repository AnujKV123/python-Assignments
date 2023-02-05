
# 4.Reverse the list by using negative index and apply logic also.

# by using negative indexing
def revList(lst):
    return(lst)[::-1]

# by using logic
def revListLogic(lst):
    lst.reverse()
    return lst

# third logic
def thirdLogic(lst):
    lstx = []
    for i in range(len(lst), 0, -1):
        lstx.append(i)
    return lstx


lst = [1, 2, 3, 4, 5]
print(revList(lst))
print(revListLogic(lst))
print(thirdLogic(lst))

