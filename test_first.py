import pytest

def test_login():
    print("Login Successful")
    
@pytest.mark.sanity
def test_logout():
    print("Logout Successful")

def test_calculation():
    assert 2+2 ==4



