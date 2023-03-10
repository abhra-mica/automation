import pytest
import requests
from pytest import fixture
import webbrowser

@fixture(scope="module")
def open_close_cluster():
    print("Function called to check all nodes are up")
    yield 
    show_report()
    print("Tearing down cluster as test passed")
    
def show_report():
    print("SHOWREPPORT--")
    #url = 'file:\\C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\GitTest\\report\\report.html'
    url = "file://C://ABHRA//report.html"
    webbrowser.open_new_tab(url)
    print("REPORT SHOWN")
    
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

@pytest.mark.sanity
def test_lcmstatus(open_close_cluster):
    resp = getRestAPIHeaders("10.125.236.31","admin","Dell@12345")
    print("REsponse-- ")
    print(resp)
    lcmStatus = requests.get(f'https://10.125.236.31:30622/AsmManager/lcm/status',
                                          headers=getRestAPIHeaders("10.125.236.31","admin","Dell@12345"),
                                          verify=False).json()['lcmStatus']
    print(lcmStatus)
    assert lcmStatus == 'READY','LCMSTATUS should be Ready'
      
def test_lcmhealth(open_close_cluster):
    resp = getRestAPIHeaders("10.125.236.31","admin","Dell@12345")
    print("Health-- ")
    print(resp)
    lcmHealth = requests.get(f'https://10.125.236.31:30622/AsmManager/lcm/healthz',
                                          headers=getRestAPIHeaders("10.125.236.31","admin","Dell@12345"),
                                          verify=False)
    print(lcmHealth)
    #assert lcmHealth == 'READY','LCMSTATUS should be Ready'
