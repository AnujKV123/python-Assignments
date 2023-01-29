# Q3. create a list with duplicate elements and remove the duplicate elements ************************************** 

# method 1 ***********************

def duplicateM1(lis):
    lis = set(lis)

    lis = list(lis)

    print(lis)

# method 2 ***********************

def duplicateM2(lis):
    ans = []

    for i in range(len(lis)):
        if lis[i] not in ans:
            ans.append(lis[i])

    print(ans)

lis = [1, 2, 3, 2, 3, 3, 5, "hi", "hello", "hi"]
duplicateM1(lis)
duplicateM2(lis)
