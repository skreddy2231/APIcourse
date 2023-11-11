list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
templist = []
# ['My', 'name', 'is', 'Kelly']


def listconcatinate(list1, list2):
    for index1 in range(0, len(list1)):
        templist.append(list1[index1] + list2[index1])
    print(templist)


# listconcatinate(list1, list2)

print("==================================1\n")

input1 = "triveni"
# o/p: accepted  / aeiou

vowelList = {"a", "e", "i", "o", "u"}
mainlist = set(input1.lower())
print(type(mainlist))
# res = mainlist.symmetric_difference(vowelList)
res = mainlist.issubset(vowelList)
if res == True:
    print("Accepted")
else:
    print("Declined")

print("==================================2\n")


def char_occurance():
    test_list1 = "geeksforgeeks is best for geeks"
    test_list1 = test_list1.replace(" ", "")
    splitlist = list(test_list1)
    # o/p: {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 2}
    temp = {}
    isPresent = False
    for ichar in splitlist:
        print("read:", ichar)
        if ichar in temp:
            temp[ichar] += 1
        else:
            temp[ichar] = 1

    print(temp)


# char_occurance()


def iterate_list_str():
    tlist = []
    newlist = ["allx", "lovex", "gfg", "xit", "is", "lovex", "bestx"]
    # o/p: ['gfg', 'xit', 'is']
    # string ends with 'x' should be removed
    for char in newlist:
        if char.endswith("x") == True:
            print("present")
            tlist.append(char)
            # newlist.remove(char)
        else:
            print("Not present")

    print("tlist::", tlist)
    for rItem in tlist:
        if rItem in newlist:
            newlist.remove(rItem)
            print("latest list:", newlist)

    print(newlist, "\n")


# iterate_list_str()
print("---------iterate_list_str--------------\n")


# two list strings match and outcome: [True, False, False]
def match_listStrings():
    test_list1 = ["Gfg", "is", "best"]
    test_list2 = ["I love Gfg", "Its Best for Geeks", "Gfg means CS"]
    for i in range(len(test_list1)):
        isContains = bool(test_list1[i] in test_list2[i])
        if isContains == True:
            print(
                "Actual contains with:",
                test_list1[i],
                " =contains= ",
                test_list2[i],
                "is:",
                isContains,
            )
        else:
            print(
                "Actual NOT contains with:",
                test_list1[i],
                " =contains= ",
                test_list2[i],
                "is:",
                isContains,
            )
        # break


# match_listStrings()
print("------- match_listStrings--------------------\n")


def reverse_str():
    mystr4 = "hellow world"
    strlist1 = list(mystr4)
    restr = ""
    # strlist1= strlist1[::-1]
    for i in range(len(strlist1)):
        restr = strlist1[i] + restr

    print("---", restr)

    mystr5 = "hellow world"
    strlist5 = list(mystr5)
    print("strlist5", strlist5[::-1])


# reverse_str()
print("---------reverse_str--------------\n")


# convert list to str
def convert_list_str():
    elist = ["the", "united", "america"]
    estr = " ".join(elist)
    print("Convert list to string using join::", estr, type(estr))

    estr = estr + " pY is FUN"
    estr = estr.capitalize()
    print("Upper case the first letter in this str:", estr)

    txt = "Hello, And Welcome To My World!"
    # Searches the string for a specified value and returns the position of where it was found
    x = txt.find("To")
    print("find x:", x)
    txt = txt.casefold()
    print("convert str into lower case:", txt)

    price = 10.05
    txt2 = "this is for watch {rangedata:} in euros"
    print(txt2.format(rangedata=price))


# convert_list_str()
print("---------convert_list_str--------------\n")


def convert_list_str_iterate():
    list1 = ["hello", "welcome", "python"]
    str1 = ""
    str2 = ""
    for i in range(len(list1)):
        str1 = str1 + list1[i]
        str2 = list1[i] + str2

    print("final convert list to str through iterateion:", str1)
    print("final convert list to str and then high index to low index strings:", str2)
    str3_reverse1 = ""
    str3 = list(str1)
    for y in range(len(str3)):
        str3_reverse1 = str3[y] + str3_reverse1
        print("rever chars:", str3_reverse1)


convert_list_str_iterate()


def numbers_check():
    # Check if all the characters in a string are decimals (0-9)
    txt = "1234"
    x = txt.isdecimal()
    print("x is decimal:", x)
    st = "  Hello  World   From Digita    lOcean   tes   t   "
    st = " ".join(st.split())
    print("remove all unwanted spaces with join +split:'", st, "'")
    st1 = "  Hello  World   From Digita    lOcean   tes   t   "
    # st1 = st1.translate()
    print("Translate fn space remove:'", st1, "'")


numbers_check()
