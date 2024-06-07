# test_calculator.py

import pytest
from calculator import calculator

@pytest.fixture
def client():
    calculator.config['TESTING'] = True
    with calculator.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h3>IP Calculator</h3>' in response.data
    
    # Test addition: 10 + 5
    client.post('/', data={'display': '10+5='})
    response = client.get('/')
    assert b'15.0' in response.data
    print("Test addition: 10 + 5 = 15")

    # Test addition: -1 + 1
    client.post('/', data={'display': '-1+1='})
    response = client.get('/')
    assert b'0.0' in response.data
    print("Test addition: -1 + 1 = 0")

    # Test addition: -1 + -1
    client.post('/', data={'display': '-1+-1='})
    response = client.get('/')
    assert b'-2.0' in response.data
    print("Test addition: -1 + -1 = -2")

if __name__ == '__calculator__':
    pytest.main(['-v', __file__])

