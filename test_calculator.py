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
    assert b'Simple Calculator' in response.data
    print("Test passed: Simple Calculator title is present in the HTML.")
    
    assert b'Outcome: None' in response.data
    print("Test passed: Outcome is present in the HTML.")
    
    # Test addition: 10 + 5
    client.post('/', data={'display': '10+5='})
    response = client.get('/')
    assert b'15' in response.data
    print("Test passed: Addition operation result is present in the HTML.")

if __name__ == '__main__':
    pytest.main(['-v', __file__])





