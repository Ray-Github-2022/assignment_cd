# test_calculator.py

import pytest
from calculator import calculator as app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'IP Calculator' in response.data
    # assert b'Outcome: None' in response.data

    # Simulate inputting "10+5=" and checking the result
    response = client.post('/', data={'expression': '10', 'operator': '+'})
    response = client.post('/', data={'expression': '10+', 'digit': '5'})
    response = client.post('/', data={'expression': '10+5', 'calculate': 'calculate'})

    # Verify the result by fetching it in JSON format
    response = client.post('/?format=json', data={'expression': response.data.decode().split('value="')[1].split('"')[0], 'calculate': 'calculate'})
    json_data = response.get_json()
    assert json_data['result'] == 15.0

if __name__ == '__main__':
    pytest.main(['-v', __file__])
