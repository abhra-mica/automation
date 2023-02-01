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



