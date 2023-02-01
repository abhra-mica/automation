import pytest
import requests
def test_login():
    print("Login Successful")
    
def test_logout():
    print("Logout Successful")

def test_calculation():
    base_url = 'https://api.publicapis.org/entries'
    print("Hello")
    response = requests.get(base_url)
    print(response)

def getRestAPIHeaders(applianceIP, username, password):
    data = {"username": username, "password": password}
    url = "https://" + applianceIP + "/rest/auth/login"
    access_token = requests.post(url, json=data, headers={'Content-Type': 'application/json'}, verify=False).json()[
        'access_token']
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        'Accept': 'application/json',
        "Authorization": "Bearer " + access_token
    }
    return headers

def test_header():
    resp = getRestAPIHeaders("10.125.236.31","admin","Dell@12345")
    print("REsponse-- ")
    print(resp)

