# test_calculator.py

import pytest
from calculator import calculator

@pytest.fixture
def client():
    calculator.config['TESTING'] = True
    with calculator.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/?a=10&b=5&operation=add')  # Updated route here
    assert response.status_code == 200
    
    # Check if the response contains valid JSON data
    json_data = response.get_json()
    if json_data is None:
        print("Response does not contain valid JSON data:")
        print(response.data.decode('utf-8'))  # Print the response content
        assert False  # Fail the test

    # Perform assertions on the JSON data
    assert json_data['result'] == 15
    print(f"Test addition: 10 + 5 = {json_data['result']}")

    # Add similar checks for other test cases...

if __name__ == '__main__':
    pytest.main(['-v', __file__])




