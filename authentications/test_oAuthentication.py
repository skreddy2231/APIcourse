import json
import requests
import jsonpath


def test_oauth_api():
    # generate token url:
    token_url = "https://thetestingworldapi.com/Token"
    response = requests.get("http://thetestingworldapi.com/api/stDe")
