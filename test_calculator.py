# test_calculator.py

# import pytest
# from calculator import calculator

# @pytest.fixture
# def client():
#     calculator.config['TESTING'] = True
#     with calculator.test_client() as client:
#         yield client

# def test_add(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert b'<h3>IP Calculator</h3>' in response.data
    
#     # Test addition: 10 + 5
#     client.post('/', data={'display': '10+5='})
#     response = client.get('/')
#     assert b'15.0' in response.data
#     print("Test addition: 10 + 5 = 15")

#     # Test addition: -1 + 1
#     client.post('/', data={'display': '-1+1='})
#     response = client.get('/')
#     assert b'0.0' in response.data
#     print("Test addition: -1 + 1 = 0")

#     # Test addition: -1 + -1
#     client.post('/', data={'display': '-1+-1='})
#     response = client.get('/')
#     assert b'-2.0' in response.data
#     print("Test addition: -1 + -1 = -2")

# if __name__ == '__main__':
#     pytest.main(['-v', __file__])

import pytest
from calculator import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Simple Calculator' in response.data
    print("Test passed: Simple Calculator title is present in the HTML.")

    assert b'Outcome: None' in response.data
    print("Test passed: Outcome is present in the HTML.")

    response = client.post('/', data={'expression': '10+5', 'calculate': 'calculate'})
    assert response.status_code == 200
    assert b'15.0' in response.data
    print("Test passed: Addition result is correct.")

if __name__ == '__main__':
    pytest.main(['-v', __file__])

