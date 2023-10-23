import json

def localtest():
    # JSON string
    students = '{"id":"9607", "name": "Sunny", "department":"Computer"}'

    # convert string to Python dict
    student_dict = json.loads(students)
    print(student_dict)

    print(student_dict['name'])
    print('Deserialization Completed.')

sampleJson = """{
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

jsondata = json.loads(sampleJson)
#print(type(jsondata))

# print("Employee data:", jsondata["company"]["employee"]["payble"]["salary"], "\n", jsondata["company"]["employee"]["payble"]["bonus"])

samplejson2 = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""
# o/p: ["name1", "name2"]
print(type(samplejson2))
convertdict = json.loads(samplejson2)
print(type(convertdict))
for n in range(len(convertdict)):
    for k, v in convertdict[n].items():
        if k == "name":
            print("val of key:", convertdict[n][k])

sampleJson = {"key1": "value1"
                , "key2": "value2"}
print(type(sampleJson))
prettyPrintedJson  = json.dumps(sampleJson, indent=3, separators=(",", " = "))
print(prettyPrintedJson)

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

dict1 = {}
dict1 = dict1.fromkeys(employees, defaults)
print(dict1)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# {'name': 'Kelly', 'salary': 8000}
resKeys = ["name", "salary"]
print(sample_dict[resKeys[0]] , " and \n", sample_dict[resKeys[1]])

dict2 = {}
for k in resKeys:
    dict2 =  {k:sample_dict[k]}

print(dict2)

