import requests
import json
import os
import pytest

absolute_path = os.path.dirname(__file__)
relative_path = "usersdata.json"
testinput = os.path.join(absolute_path, relative_path)

with open(testinput, "r") as getinput:
    testdata = getinput.read()
    fetch_data = json.loads(testdata)


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
    assert "morpheus" == jsondata["name"]


# post_createUser()

# close external json file
getinput.close()
