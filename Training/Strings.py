import random
str1 = "Hello"
str2 = "hello"
str3 = "Welcome to Python programing!"

num1, num2 = 100, 60
p = q = r = "I am a fruit"


def general_str_examples(num2):
    print("--------------------")
    print(f"declared same value to multiple variables \n p: '{p}', q:'{q}', r:'{r}'")
    print("*** before convert 'num2' data-type:", type(num2))
    num2 = str(num2)
    print("convert string <-> int: ", num2)
    print("*** After convert 'num2' data-type:", type(num2))
    print("-------------------- \n")


def isequal_strings(a, b):
    if str1 == str2:
        print(f"Both strings are equal")
    elif str1 != str2:
        print("Concatinate strings:", str1, ",", str3)
    else:
        print(f"Both strings are NOT equal")


def reverse_data(str):
    print("Current value:", str)
    str = str[::-1]  # ::-1 slice the string into chars and reverse -1 to 0 position
    print("Reverse value:", str)


def reverse_wordbackword(str):
    result = ""
    split_str = str.split(" ")
    for st in split_str:
        res = st[::-1]
        print("---- slice and reverse:", res)
        result = result + " " + res

    return result


# explicitly specify the data type of a variable [casting]
def datatype_casting(dstr, dinteger, dfloat):
    dstr = str(5)
    dinteger = int(3)
    dfloat = float(3)
    print(
        f" 1. declared string: '{dstr}' \n 2. declared Integer: '{dinteger}' \n 3. declared float: '{dfloat}'"
    )


def str_joins_test():
    # using a dictionary as an iterable, the returned values are the keys, not the values.
    myDict = {"name": "John", "country": "Norway"}
    myseperator = "#"
    res = myseperator.join(myDict)
    print("Dict  values joined with seperator:", res)

    # Join all items in a tuple into a STRING, using a hash character as separator:
    myTuple = ("John", "Peter", "Vicky")
    resTuple = myseperator.join(myTuple)
    print("Join tuple items:", resTuple)

    myList = ["test1", "user1", "124"]
    resList = myseperator.join(myList)
    print("Join list items:", resList)


# general_str_examples(num2)

# # compare strings are equal
# isequal_strings(str1, str2)
# print("\n")

# # reverse full string:
# reverse_data(str3)
# print("\n")

# # reverse string (word by word) backwards
# reverse = reverse_wordbackword(str3)
# print("Reverse string word by word backwarding:", reverse)
# print("\n")

# datatype_casting("administartor", 200, 54.1881)
# print("\n")

# string.join(iterable)
# str_joins_test()


# Test random val generation
def get_random_values():
    print("Generate random number from range:", random.randrange(3, 9))


# get_random_values()

my_list = ["a", ["bb", "cc"], "d"]
my_list[1].append("xx")
print("After append:", my_list)
my_list[1].insert(0, "dd")
print("After insertion:", my_list)
