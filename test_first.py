import pytest
import requests
def test_login():
    print("Login Successful")
    
def test_logout():
    print("Logout Successful")

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
    status = requests.get(f'https://10.125.236.31:30622/AsmManager/lcm/status',
                                          headers=getRestAPIHeaders(ingress_ip, username, password),
                                          verify=False)
    print(status)
