# https://www.geeksforgeeks.org/python-convert-dictionary-value-list-to-dictionary-list/

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = []


def lists_concatinate(a, b):
    for x in a:
        for y in b:
            result.append(x + y)
        print(result)


'''Ex1: o/p =['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
lists_concatinate(list1, list2)'''


# Iterate both lists simultaneously–
list3 = [10, 20, 30, 40]
list4 = [100, 200, 300, 400]
'''print(list4[::-1])  # reverse list
list4.reverse()  # reverse list'''


def lists_iterate_parallel(eList3, eList4):
    index = 0
    eList4.reverse()
    for x in eList3:
        for y in range(index, len(eList4)):
            print(x, eList4[y])
            index = index + 1
            break


# Ex2:
# lists_iterate_parallel(list3, list4)


# Remove empty strings from the list of strings
# o/p—----["Mike", "Emma", "Kelly", "Brad"]
def remove_emptyList():
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    for element in list1:
        if element == "":
            list1.remove(element)
    print(list1)


# remove_emptyList()


def isChildElemetsNested(iList, temp1):
    appendlist = []
    isreturn = any(isinstance(i, list) for i in iList)
    if isreturn == True:
        for childlist in iList:
            if (
                len(childlist) >= 1
                and type(childlist) == list
                and any(isinstance(i, list) for i in childlist) == False
            ):
                childlist.extend(sub_list)
                print("*** Final appended list....", childlist)
                temp1 = childlist.copy()
                appendlist.append(temp1)
            else:
                appendlist.append(childlist)
                print("--- simple elements:", appendlist)

            isChildElemetsNested(childlist, temp1)
    return appendlist


# Ex3: Extend the nested list by adding the sublist
def extensmainlist():
    mainlist = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]
    mylist = []
    temp1 = []
    for ele in range(len(mainlist)):
        isNested = True
        print("Iterate element before:", mainlist[ele])
        resultList = isChildElemetsNested(mainlist[ele], temp1)
        if len(resultList) > 0 and resultList != "":
            mylist.append(resultList)
            temp1 = []
        else:
            mylist.append(mainlist[ele])
        print("Iteration element after append:", mylist, "\n")

    print("Updated mainlist details:", mylist)


# extensmainlist()

# ASK: https://www.interviewbit.com/problems/nested-list/#:~:text=To%20add%20new%20values%20to,by%20using%20extend()%20method.&text=If%20you%20know%20the%20index,can%20use%20pop()%20method.
# elist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
# print(elist[1:4])
# print(elist[::])
# print(elist[3:15:3])
# print(elist[::-1])
# print(elist[::-3])
# print(elist[:1:-2])
# print(elist[1:1:1])
# print(elist[-1:-1:-1])
# print(elist[:0:])


def lamdatest():
    x = lambda a: a + 10
    print(x(5))

    # Multiply argument a with argument b and return the result:
    y = lambda i, j: i * j
    print(y(5, 6))


# lamdatest()


def reverse(s):
    if len(s) == 0:
        print("Now s:", s)
        return s
    else:
        tt = reverse(s[1:]) + s[0]
        print(tt)
        return reverse(s[1:]) + s[0]


s = "Geeksforgeeks"
# print(reverse(s))
print("recursive slice:", s[1:])
print("recursive slice2:", s[1:6])
print("recursive reverse slice3:", s[1:7:2])
print("recursive reverse slice4:", s[-4:])
