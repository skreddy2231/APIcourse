import json

def simpleJosn():
    # JSON string
    students = '{"id":"9607", "name": "Sunny", "department":"Computer"}'
    print(type(students))
    print("initial data:", students)
    # print(students["department"])
    # convert string to Python dict
    student_dict = json.loads(students)
    print("Loads() function reurned:", type(student_dict))
    print("loads the data:", student_dict)
    print(student_dict["department"])
    print(student_dict['name'])
    print('Deserialization Completed.')

def use_dumps():
    # Creating a dictionary
    dictionary = { 1: 'Welcome', 2: 'to',
                  3: 'Geeks', 4: 'for',
                  5: 'Geeks'}
    print("Step1: Initial dict type1: ", type(dictionary))  # dict
    print("Key returns value:", dictionary[3], " or way2:", dictionary.get(3))
    # list(my_dict.keys())[list(my_dict.values()).index(100)])
    # one-liner way..
    str_from_dict = list(dictionary.keys())
    print("convert to list to fetch values", type(list(dictionary)), " its and keys:", list(dictionary.keys()))
    print("===:", list(dictionary.values()).index("for"))  # returned value of index
    print("Value returns key:", list(dictionary.keys())[list(dictionary.values()).index("for")],"\n otherwise another way iterate all values and get key")

    # Step2: Converts input dictionary into string and stores it in json_string
    json_string = json.dumps(dictionary)
    print("Step2: convert dict to json str: " , type(json_string))  #str

use_dumps()