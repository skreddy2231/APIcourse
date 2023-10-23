import requests
import json

FAKEURL = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'


testinput = "C:/TestQA/Twilight/rf-2023/APICourse/reqres_api/usersdata.json"

with open(testinput, 'r') as testdata_get:
    data = testdata_get.read()
    print(type(data))
    jsondata = json.loads(data)
    print(jsondata["single_user"])

print(data)
testdata_get.close()