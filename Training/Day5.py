def duplicat_char():
    test_str = "hewelloo"
    test_str = list(test_str)
    test_dict = {}
    empty_str = ""

    kVal = 1
    for x in test_str:
        if x not in test_dict.keys():
            test_dict[x] = kVal
        else:
            print("Duplicate char", x)

    print(empty_str)


str1 = "geekforgeeks best for geeks"
str2 = str1.split(" ")
empty_list1 = []
repl_dict = {"geeks": "all CS aspirants"}
# o/p: geekforgeeks best for all CS aspirants

for item in str2:
    empty_list1.append(repl_dict.get(item, item))
    # if item == "geeks":
    # print("Gte:", empty_list1)

empty_list1 = " ".join(empty_list1)
print("updated str:", empty_list1, "\n")


new_str = "gfg is best for geeks"
split_str = new_str.split(" ")
# str = gfg is  for
test_dict2 = {"geeks": 1, "best": 6}
empty_list2 = []
for word in test_dict2.keys():
    print("Keys :", word)
    if word in split_str:
        # empty_list2.append(test_dict2.get(word, " "))
        new_str = new_str.replace(word, "")

# empty_list2 = " ".join(empty_list2)
print(new_str)


str3 = "Geeks for Geeks"
str4 = str3.split(" ")
list1 = []
str5 = ""
for item in str4:
    if item not in list1:
        list1.append(item)

str5 = " ".join(list1)
print("Final:", str5)


dict1 = {"Manjeet": [1], "Akash": [1, 8, 9]}
# o/p: {‘Manjeet’: [], ‘Akash’: [8, 9]}

y = []
res = {}
# res = dict()
for values in dict1.values():
    y = values
    print(y)

for i in dict1.keys():
    a = []
    for j in dict1[i]:
        if j in y:  # [1] in [1,8,9]
            # res_dict.append(dkeys, "")
            res.get(i, " ")
            # a.append(dVal)
        # res_dict[dkeys] = a
print(y)


def intersections():
    x = []


for i in test_dict.keys():
    x.extend(test_dict[i])
y = []
for i in x:
    if x.count(i) == 1:
        y.append(i)
res = dict()

for i in test_dict.keys():
    a = []
    for j in test_dict[i]:
        if j in y:
            a.append(j)
        res[i] = a
