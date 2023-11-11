mydict1 = {"fruits": "apple", "name": "student", "gadgets": "phones"}
print(mydict1)

# fetch value from key
print("Get dict value of key:", mydict1["name"], "other way:", mydict1.get("name"))


# insert a new record to dict
mydict1["year"] = "2023"
print(mydict1)

# length of dict
print("length of dict:", len(mydict1))

# use the dict() constructor to make a dictionary
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)


# get only keys form dictionary:
print("Get only Keys:", mydict1.keys())

# get values from keys in dictionary:
print("Get values of Keys:", mydict1.values())
mydict1["fruits"] = "Mango"
print("Ftech dict after update a value:", mydict1)

# Get a list of the key:value pairs as tuples in a list.
print("Get a list of the key:value pairs:", mydict1.items())

# check specified key is present in a dictionary use the in keyword
if "name" in mydict1:
    mydict1["name"] = "Students"
    print("yes, key: name is present in dict", mydict1, "\n")


# change the key value from dict, if key is not there, it adds as new entry
mydict1["year1"] = 2019
print("---value change:", mydict1, "\n")
# update the value, if key is not there, it wont update and no error
mydict1.update({"year2": "2023"})
print("-----Update value:", mydict1, "\n")

# copy dict into other dict
mydict2 = mydict1.copy()  # way1
mydict3 = dict(mydict1)  # way2 for copy


# pop() method removes the item with the specified key name
mydict1.pop("name")
print("remove the item form dict using pop:", mydict1, "\n")

# popitem() method removes the last inserted item
mydict1.popitem()
print("remove the item form dict use popitem:", mydict1, "\n")

# delete(del) keyword deletes the specific key: [pop()]
del mydict1["year1"]
print("Delete the key using del:", mydict1, "\n")

# del keyword can also delete the dictionary
del mydict1
# print(bool(mydict1))  # throws error
print(mydict2)  # clone of mydict1

# clear() method empties the dictionary:
thisdict.clear()
print(thisdict)

# ------------- Nested Dict  ---------------APIs
myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}

print("Fetach nested:", myfamily["child2"]["year"])


def crud_dict():
    mydict1 = {}
    mydict1["name"] = "triveni"
    mydict1["alphabet"] = 1, 2, 3, 4, 5
    print(mydict1)
    mydict1["roles"] = {"nested": {"adres": "IND", "num": 114}}
    print("Added new valu:", mydict1)
    mydict2 = {"name1": "stud1"}
    print("name2::", mydict2.get("name2"))
    print("name3::", mydict2.get("name3", "John"))

    test_dict = {"Manjeet": 11, "Akash": 2, "Akshat": 3, "Nikhil": 1}
    print("The original dictionary : ", test_dict)
    empty_dict = dict()
    flag = False
    print("my hash-val:", empty_dict)
    for keys in test_dict:
        if test_dict[keys] in empty_dict:
            flag = True
            break
        else:
            empty_dict[test_dict[keys]] = 1
    print("Does dictionary contain repetition : ", str(flag))
    print("Does dictionary contain repetition : ", flag)


crud_dict()
