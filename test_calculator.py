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

    # Define expected HTML content
    expected_content = [
        b'<h3>Hello, how are you?</h3>',
        b'<h2>Simple Calculator..</h2>',
        b'<form method="post">',
        b'<input type="number" name="a" placeholder="Enter first number" required>',
        b'<input type="number" name="b" placeholder="Enter second number" required>',
        b'<select name="operation">',
        b'<option value="add">Addition</option>',
        b'<option value="subtract">Subtraction</option>',
        b'<option value="multiply">Multiplication</option>',
        b'<option value="divide">Division</option>',
        b'<button type="submit">Calculate</button>'
    ]

    # Check if each expected HTML content is present in the response data
    for content in expected_content:
        assert content in response.data





