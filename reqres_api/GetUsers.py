import requests
import json

APIURL = 'https://reqres.in'
id = '2'
notfound_id = '200'

get_users = '/api/users?page=2'
single_user = '/api/users/' + id
single_user_notfound = '/api/users/' + notfound_id
list_resource = '/api/unknown'
list_single_resource = '/api/unknown/6'
list_single_resource_notfound = '/api/unknown/61'
req_hearders = {
    'Content-Type': 'application/json'
}


# GET ALL users
def get_AllUsers():
    response = requests.get(APIURL + get_users, headers=req_hearders)
    # verify status code
    assert response.status_code == 200
    req_response = response.json()

    # <pretty response JSON format>
    res_jsondata = json.dumps(req_response, indent=4)
    jsondata = json.loads(res_jsondata)
    usersDict = {}
    usersList = []
    for data in jsondata["data"]:
        if "Lindsay" in data["first_name"]:
            print(f'user "{"Lindsay"}" present in json data')
            # Ques ask1: how to assert user in non-print stmt?

        usersDict[data["id"]] = data["first_name"]
        usersList.append(data["first_name"])

    print(f'Store subset of users in dict:{usersDict} ,\n subset of users in list:{usersList}')
    # Ques ask2: how to return more than one value?


# GET Request
def get_SingleUser():
    response = requests.get(APIURL + single_user, headers=req_hearders)
    # verify status code
    assert response.status_code == 200
    req_response = response.json()
    res_jsondata = json.dumps(req_response, indent=4)
    jsondata = json.loads(res_jsondata)
    print(jsondata["data"]["id"])

    # validate runtime id with actual id
    assert jsondata["data"]["id"] == int(id)


def get_SingleUserNotFound():
    response = requests.get(APIURL + single_user_notfound, headers=req_hearders)
    req_response = response.json()
    # print("req_response", req_response)
    # verify status code
    assert response.status_code == 404
    assert len(req_response) == 0


def get_ListResources():
    response = requests.get(APIURL + list_resource, headers=req_hearders)
    # verify status code
    assert response.status_code == 200
    req_response = response.json()
    res_jsondata = json.dumps(req_response, indent=4)
    jsondata = json.loads(res_jsondata)

    expected_keys = ['pantone_value', 'id', 'color', 'name']
    keyval = {}
    for eachItem in jsondata["data"]:
        print("eachItem", eachItem)
        for key, value in eachItem.items():
            if key in expected_keys:
                keyval[key] = value

    print("results gestored in json dict:", keyval)


def get_ListSingleResource():
    response = requests.get(APIURL + list_single_resource, headers=req_hearders)
    # verify status code
    assert response.status_code == 200
    req_response = response.json()
    res_jsondata = json.dumps(req_response, indent=4)
    jsondata = json.loads(res_jsondata)

    # validate runtime resource_id with actual_id
    assert jsondata["data"]["id"] == 6


def get_SingleUserNotFound():
    response = requests.get(APIURL + list_single_resource_notfound, headers=req_hearders)
    req_response = response.json()

    # verify status code when resource not found
    assert response.status_code == 404
    assert len(req_response) == 0



# get_AllUsers()
# get_SingleUser()
# get_SingleUserNotFound()
# get_ListResources()
# get_ListSingleResource()
# get_SingleUserNotFound()

# Ques ask3: how to generate report in TA.
 # how to handle and validate type of authorizations
 # how to validate headers
 # how to create test cases / test suites ?
 # can we group test cases based on tags ?
 # run tests / test suites in parallel ?
 # run tests in sequential ?
 # re-run failure tests ?
 # trigger batch script / schedule cronjob.

 # [gmail / outlook]
 # Notify results in email ( start of suite and completion of suite) - test results
 # Notify email, email results in attachment.

 # How to setup framework in virtual env? (use in python and RF)
 # create GIT repo
 # configure tests in Jenkins and gitLab
 # setip different type of suites in pipeline




