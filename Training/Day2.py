st1 = "malayalam"
str = st1[::-1]

elist = []


def str_reverse():
    for i in reversed(range(len(st1))):
        print(st1[i])
        elist.append(st1[i])

    result = "".join(elist)
    print(result == st1)


# listItem = list(st1)
# print(listItem)
# list1 = []
# size = len(listItem)
# print(size)
# for i in range(size, 0, -1):
#     print(listItem[-1])
#     list1.append(listItem[-i])
# print("reverse result:", list1)

# list2 = [7, 3, 1, 3, 45, 2, 1, 4, 51, 4, 1]
# for i in range(len(list2), 1, -1):
#     print(list2[i])


swaplist = [200, 300, 400, 500]
# swaplist.replace(swaplist[1], swaplist[3])
res = swaplist[1]
swaplist[1] = swaplist[3]
swaplist[3] = res
print(swaplist)

# identify -ve numbers and get list
test_list = [5, 6, -3, -8, 9, 11, -12, 2]
emp_list = []
for x in test_list:
    if x > 0:
        emp_list.append(x)
        # test_list.remove(x)
print(emp_list)

names = "   hello       wor     ld  !  1  "
res11 = names.rstrip()
print("'", res11, "'")


test_list = [[1, 3], [3, 4], [6, 5], [4, 5], [7, 6], [7, 9]]
# [[1, 3, 3, 4, 6, 5], [4, 5, 7, 6, 7, 9]]
res = []
count11 = len(test_list)
k = count11 / 2  # 6/2 = 3
for j in range(0, len(test_list), k):
    temp = []
    for sub in test_list[j : j + k]:
        for i in sub:
            temp.append(i)
    res.append(temp)
print("*** ", res, " ***")


str1 = "This is a python language"
strlist = str1.split(" ")
newlist1 = []
for x in strlist:
    if len(x) % 2 == 0:
        print(x)
        newlist1.append(x)
print(newlist1)


str2 = "apples"
st_len = len(str2)
k = st_len // 2  # 7/2 = 3.5 (// 3)
res = ""
for x in range(st_len):
    if x >= k:
        res = res + str2[x].upper()
    else:
        res = res + str2[x]
print(res)
