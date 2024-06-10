import requests
from requests.auth import HTTPBasicAuth


def test_with_authentication():
    response = requests.get(
        "https://api.github.com/user",
        auth=HTTPBasicAuth("triveni.bika@gmail.com", "Sri@2920"),
    )
    print(response.text)
    
