# https://www.geeksforgeeks.org/python-remove-double-quotes-from-dictionary-keys/
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict.get("brand"))
print(thisdict["brand"])

print(thisdict.keys())
print(thisdict.values())
x = thisdict.items()
print(type(x))

if "brand1" in thisdict:
    print("Key exisst")
else:
    print("Key NOT exisst")


def getKey(thisdict, value):
    # print((thisdict.values()).index[0])
    for x, keyVal in thisdict.items():
        if value == keyVal:
            print("My key:", x)
            break


# getKey(thisdict, 1964)


test_dict = {
    "Gfg": {"a": [1, 3], "b": [3, 6], "c": [6, 7, 8]},
    "Best": {"a": [7, 9], "b": [5, 3, 2], "d": [0, 1, 0]},
}
# Output : {‘c’: {‘Gfg’: [0, 7]}, ‘b’: {‘Gfg’: [4, 9]}, ‘a’: {‘Gfg’: [1, 3, 7, 8]}}


# def nesteddict():
#     for dict in test_dict.items():
#         print("Get main dict:", dict)
#         for key1, val1 in dict[val1].items():
#             print("Get key and val of dict:", key1, val1)  # Gfg": {"a": [1, 3] }
#             # ‘a’: {‘Gfg’: [1, 3, 7, 8]}
#             print(dict[val1])


listdict = {"month": [1, 2, 3], "name": ["Jan", "Feb", "March"]}

# {1: 'Jan', 2: 'Feb', 3: 'March'}

# emptyDict = {}


# def nestedDict(listdict):
#     for lisVal in listdict.values():  # [1, 2, 3]  ["Jan", "Feb", "March"]
#         print("get length:", len(lisVal))
#         for valIndix in range(0, len(lisVal)):  # [1, 2, 3]
#             print("level list:", lisVal[valIndix])
#             for valIndix in range(0, len(lisVal)):  # [1, 2, 3]
#                 print("level list:", lisVal[valIndix])
#                 emptyDict[[lisVal][0][valIndix]] = lisVal[1][valIndix]

#     print("outcome:", emptyDict)


# nestedDict(listdict)


# list1 = [1, 2, 3, 4]
# list2 = ["a", "b", "c", "d"]


listdict1 = {"month": [1, 2, 3], "name": ["Jan", "Feb", "March"]}
a = list(listdict1.values())  # [[1, 2, 3], ['Jan', 'Feb', 'March']]
print("== ", a)
list1 = a[0]
list2 = a[1]
# for i in a:
#     print("i val:", i[0])
print("list1", a[0])
print("list2", a[1])
temp2 = {}
for idict in range(len(list1)):
    temp2[list1[idict]] = list2[idict]
print("output:", temp2)


str = "gfg_is_best_for_geeks"
# {'gfg': {'is': {'best': {'for': 'geeks'}}}}
splitstr = str.split("_")
templist = []
tempdict = {}
print("list length:", len(str, splitstr))


def convert_str_nesteddict(str, splitstr):
    # for index in range(0, len(splitstr)):
    if str in splitstr:
        LookupError
    else:
        convert_str_nesteddict(splitstr[index])

    print("Final o/p:", tempdict)


convert_str_nesteddict(str, splitstr)

# list1 = ["a", "b", "c", "d"]
# for i in range(list1):
#     print(i)


# for i in range(0, len(list1):
#     print(i)
