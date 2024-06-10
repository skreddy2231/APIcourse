z# List [] - List is an ordered , allows duplicates(allows to change the existing behavior) - MUTABLE
# Tuple () - Tuple does not allows change of the existing behavior. - IMMUTABLE (i.e, constant list varible)
# Set {} - It is an unordered.

list1 = [
    1,
    2,
    3,
    4,
    "kartik",
    "hello",
    True,
    [
        "kartik",
        "hello",
        False,
        "true",
        [
            "apple",
            "ball",
            "my name is kartik of kartik",
            ["user1", "this is new kartik"],
            "alltests",
        ],
    ],
]

str_name = "kartik"
occurance = 0


def handle_stroccurance(str_ele, list1, occurance):
    for ele in list1:
        if ele == str_ele and type(ele) == str:
            print(
                "Expected: '",
                str_name,
                "' matched from Actual string: '",
                ele,
                "' occurance:",
                occurance,
            )
            occurance += 1
        elif type(ele) == list:
            handle_stroccurance(str_name, ele, occurance)
            print(
                "Expected: '",
                str_name,
                "' matched from Actual sub-string: '",
                ele,
                "' occurance:",
                occurance,
            )
            occurance += 1
        elif type(ele) == str and str_name in ele:
            handle_stroccurance(str_name, ele, occurance)
            print(
                "Expected name: '",
                str_name,
                "' matched from Actual sub-string:'",
                ele,
                "' occurance:",
                occurance,
            )
            occurance += 1
        else:
            if occurance == len(list1):
                print("i m breaking..")
                break
    return occurance

    # print("Name:", str_name, "' , total no.of occurances:", occurance)


# practice string methods:
def string_examples():
    txt = "I love apples, apples are my favorite fruit"
    mylist = ["apple", "fruits", "cars", 123, "fruits with apples"]
    str = "hellow 123"
    str2 = ["EN", "NL", "All"]

    print("length of string:", len(str))
    print("length of list:", len(mylist))
    print("Fetch value form list", mylist[-2])
    mylist.append("animals")
    print("Append value to list:", mylist)

    mylist.insert(1, "mango")
    print("Insert value to list:", mylist)

    mylist.remove(123)
    print("Delete value from list:", mylist)

    mylist.pop(-1)
    print("Remove list element from the specified index", mylist)

    print("\n GET list data", mylist)
    mylist.reverse()
    print("Reverse the list", mylist)

    str2.extend(mylist)
    print("Extend list:", mylist)

    msg = "    python       is   FU     N!   "
    msg = msg.strip()
    print("Trim a string:'", msg + "'")

    # replace a string value:
    message = "python is a programing lang"
    msg1_result = message.replace("programing", "scripting")
    print(f"Replace string content: '{msg1_result}'")


# practice python built-in data types:
def py_datatypes():
    lang_list1 = ["Java", "C++", "Python"]

    # Tuple::
    lang_list2 = ("Telugu", "Hindi", "Telugu", "English", "konkani" "telugu")
    lang_list2_val = lang_list2.index("Telugu")
    print(
        f"Search the first occurence of value:",
        lang_list2_val,
    )
    lang2_res = lang_list2.count("Telugu")
    print("Specify no.of time value occurence:", lang2_res)

    lang_list1.extend(lang_list2)
    print("extend list from tuple:", lang_list1)

    lang_list1.sort()
    print("Sort the list values:", lang_list1)

    list3 = lang_list1.copy()
    list3.append("Curl")
    print("Clone new list:", list3)

    lang_list1.clear()
    print("clear values in list:", lang_list1)


# check repeat string occurance:
# result = handle_stroccurance(str_name, list1, occurance)
# print("Name:'", str_name, "' exists, no.of occurences:", result)

# General str examples
# string_examples()
# print("---------\n")

# list & tuple methods
# py_datatypes()
# print("---------\n")


def general_str_ex():
    mydict = {"emp1": "Engineer", "emp2": "HR", "emp3": "Sales", "emp4": "Director"}
    print("return only keys:", mydict.keys())
    print("Dict key has a value:", mydict["emp2"])
    print("Get dict value of the key:", mydict.get("emp3"))
    mydict["emp5"] = "Organiser"
    print("Dictionary contain:", mydict)
    print("---------\n")


def symmetric_diff():
    # returns all items to result variable except the items on intersection
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    xresult = x.symmetric_difference(y)
    yresult = y.symmetric_difference(x)
    print("Set x & y symmetric_difference in x is:", xresult)
    print("Set x & y symmetric_difference in y is:", yresult)


# symmetric_diff()


def set_subset_ex():
    A = {1, 2, 3}
    B = {1, 2, 3, 4, 5}
    C = {8, 3, 4, 1, 5, 2, 7, 9}
    D = {2, 3, 1}
    # all items of A are present in B
    print(A.issubset(B))
    print("B is subset of C: ?", B.issubset(C))
    print(A.issubset(D))


set_subset_ex()
