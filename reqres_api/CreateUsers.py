import requests
import json

APIURL = 'https://reqres.in'
create_user = '/api/users'

req_hearders = {
    'Content-Type': 'application/json'
}

singleuser_body = {
    "name": "morpheus",
    "job": "leader"
}


def post_createUser():
    response = requests.post(APIURL+create_user, json=singleuser_body, headers=req_hearders)
    assert response.status_code == 201

    req_response = response.json()
    req_jsondata = json.dumps(req_response)
    jsondata = json.loads(req_jsondata)

    assert "morpheus" == jsondata["name"]


post_createUser()