from io import open
import os
import requests
import json
import pytest   # unit test framework
# @pytest.mark.skip  - decorator for skip any test


absolute_path = os.path.dirname(__file__)
relative_path = "usersdata.json"
testinput = os.path.join(absolute_path, relative_path)
with open(testinput, 'r') as getinput:
    testdata = getinput.read()
    fetch_data = json.loads(testdata)  # loads method converts dict which is in string format, to json format


# GET ALL users
@pytest.mark.Sanity
def test_tc_001_get_AllUsers():
    response = requests.get(fetch_data["APIURL"] + fetch_data["get_users"], headers=fetch_data["req_hearders"])
    # verify status code
    assert response.status_code == 200
    req_response = response.json()

    #fetch heards and validate::
    print(response.headers)
    print(response.headers.get('Date'))
    print(response.headers.get('Server'))
    print(response.cookies)
    print(response.encoding)
    print(response.elapsed)     # elapsed time is b/w sending request to get response duration

    # Get complete content ->
    print(response.content)

    # <pretty response JSON format>
    # response is in the form of object. before call keys in json format, parse response object.
    res_jsondata = json.dumps(req_response, indent=4)
    jsondata = json.loads(res_jsondata)
    usersDict = {}
    usersList = []
    for data in jsondata["data"]:
        if "Lindsay" in data["first_name"]:
            print(f'user "{"Lindsay"}" present in json data')
            assert "Lindsay" == data["first_name"]
        usersDict[data["id"]] = data["first_name"]
        usersList.append(data["first_name"])
    # return usersList, usersDict


# GET Request
@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_002_get_SingleUser():
    response = requests.get(fetch_data["APIURL"] + fetch_data["single_user"], headers=fetch_data["req_hearders"])
    # verify status code
    assert response.status_code == 200, "Status code failed in Get method"
    req_response = response.json()
    res_jsondata = json.dumps(req_response, indent=4)
    jsondata = json.loads(res_jsondata)
    print(jsondata["data"]["id"])

    # validate runtime id with actual id
    assert jsondata["data"]["id"] == 2

@pytest.mark.Sanity
def test_tc_003_get_SingleUserNotFound():
    response = requests.get(fetch_data["APIURL"] + fetch_data["single_user_notfound"],
                            headers=fetch_data["req_hearders"])
    req_response = response.json()
    # print("req_response", req_response)
    # verify status code
    assert response.status_code == 404
    assert len(req_response) == 0

@pytest.mark.Smoke
# @pytest.mark.skip("Skipping test as it is depends on other test")
def test_tc_004_get_ListResources():
    response = requests.get(fetch_data["APIURL"] + fetch_data["list_resource"],
                            headers=fetch_data["req_hearders"])
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

@pytest.mark.Smoke
def test_tc_005_get_ListSingleResource():
    response = requests.get(fetch_data["APIURL"] + fetch_data["list_single_resource"],
                            headers=fetch_data["req_hearders"])
    # verify status code
    assert response.status_code == 200
    req_response = response.json()
    res_jsondata = json.dumps(req_response, indent=4)
    jsondata = json.loads(res_jsondata)

    # validate runtime resource_id with actual_id
    assert jsondata["data"]["id"] == 6

@pytest.mark.Sanity
def test_tc_006_get_SingleResourceNotFound():
    response = requests.get(fetch_data["APIURL"] + fetch_data["list_single_resource_notfound"],
                            headers=fetch_data["req_hearders"])
    req_response = response.json()
    # verify status code when resource not found
    assert response.status_code == 404
    assert len(req_response) == 0


# a, b = get_AllUsers()
# print("\n ****** GET ALL USERS outcome ***** \n")
# print(a)
# print(b)

# get_SingleUser()
# get_SingleUserNotFound()
# get_ListResources()
# get_ListSingleResource()
# get_SingleResourceNotFound()

# close input urls defined json file
getinput.close()
