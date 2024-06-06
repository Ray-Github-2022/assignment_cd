# test_calculate.py
import pytest
from calculate import calculate

@pytest.fixture
def client():
    calculate.config['TESTING'] = True
    with calculate.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/add?a=10&b=5')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 15
    print(f"Test addition: 10 + 5 = {json_data['result']}")

    response = client.get('/add?a=-1&b=1')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 0
    print(f"Test addition: -1 + 1 = {json_data['result']}")

    response = client.get('/add?a=-1&b=-1')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == -2
    print(f"Test addition: -1 + -1 = {json_data['result']}")

if __name__ == '__main__':
    pytest.main(['-v', __file__])
