# test_calculator.py

# Import necessary modules
import pytest
from calculator import calculator

# Define fixture to set up the test client
@pytest.fixture
def client():
    calculator.config['TESTING'] = True
    with calculator.test_client() as client:
        yield client

# Define test case
def test_add(client):
    # Send a GET request to the calculator route
    response = client.get('/')

    # Assert that the response status code is 200
    assert response.status_code == 200

    # Check if the response contains valid HTML content
    assert b'<title>Hello Today! Simple Calculator</title>' in response.data
    assert b'<h2>Simple Calculator..</h2>' in response.data
    assert b'<form method="post">' in response.data
    assert b'<input type="number" name="a" placeholder="Enter first number" required>' in response.data
    assert b'<input type="number" name="b" placeholder="Enter second number" required>' in response.data
    assert b'<select name="operation">' in response.data
    assert b'<option value="add">Addition</option>' in response.data
    assert b'<option value="subtract">Subtraction</option>' in response.data
    assert b'<option value="multiply">Multiplication</option>' in response.data
    assert b'<option value="divide">Division</option>' in response.data
    assert b'<button type="submit">Calculate</button>' in response.data



