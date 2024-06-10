import requests
import json
import os
import pytest
import jsonpath

absolute_path = os.path.dirname(__file__)
relative_path = "usersdata.json"
testinput = os.path.join(absolute_path, relative_path)

with open(testinput, "r") as getinput:
    testdata = getinput.read()
    fetch_data = json.loads(testdata)

post_createuserid = ""
@pytest.mark.Regression
@pytest.mark.TopPriority
def test_tc_101_post_createUser():
    response = requests.post(
        fetch_data["APIURL"] + fetch_data["create_user"],
        json=fetch_data["singleuser_body"],
        headers=fetch_data["req_hearders"],
    )
    assert response.status_code == 201
    req_response = response.json()
    req_jsondata = json.dumps(req_response)
    jsondata = json.loads(req_jsondata)
    print(jsondata)
    print("created user id:", jsondata["id"])
    post_createuserid = jsondata["id"]
    print("post_createuserid--", type(post_createuserid))
    assert "morpheus1" == jsondata["name"]

def test_tc_102_get_CreatedNewUserById():

    #response = requests.get(fetch_data["APIURL"] + fetch_data["single_user"], headers=fetch_data["req_hearders"])
    response = requests.get(fetch_data["APIURL"] + "/api/users/"+post_createuserid, headers=fetch_data["req_hearders"])

    # verify status code
    assert response.status_code == 200, "Status code failed in Get method"
    req_response = response.json()
    res_jsondata = json.dumps(req_response, indent=4)
    jsondata = json.loads(res_jsondata)
    print("Get id before asser3:", type(jsondata))
    print("Get id before asserr:", jsondata["id"])

    # validate runtime id with actual id
    assert jsondata["id"] == post_createuserid

# post_createUser()
test_tc_101_post_createUser()
test_tc_102_get_CreatedNewUserById()
# close external json file
getinput.close()
