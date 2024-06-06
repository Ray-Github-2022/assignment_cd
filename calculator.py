# calculator.py
# HTML and CSS for the front-end interface and Flask to handle the back-end logic.

# app.py
from flask import Flask, request, jsonify, render_template_string

calculator = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Today! Simple Calculator</title>
    <style>
        /* Your CSS styles here */
    </style>
</head>
<body>
    <div class="calculator">
        <h3>Hello, how are you?</h3>
        <h2>Simple Calculator..</h2>
        <form method="post">
            <input type="number" name="a" placeholder="Enter first number" required>
            <input type="number" name="b" placeholder="Enter second number" required>
            <select name="operation">
                <option value="add">Addition</option>
                <option value="subtract">Subtraction</option>
                <option value="multiply">Multiplication</option>
                <option value="divide">Division</option>
            </select>
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}
        <div class="result">
            <p>Last result: {{ result }}</p>
        </div>
        {% elif error is not none %}
        <div class="result">
            <p style="color: red;">Error: {{ error }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@calculator.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            a = float(request.form.get('a'))
            b = float(request.form.get('b'))
            operation = request.form.get('operation')

            if operation == 'add':
                result = a + b
            elif operation == 'subtract':
                result = a - b
            elif operation == 'multiply':
                result = a * b
            elif operation == 'divide':
                if b == 0:
                    error = "Cannot divide by zero"
                    return render_template_string(HTML_PAGE, error=error)
                else:
                    result = a / b
        except ValueError:
            error = "Invalid input. Please enter valid numbers."
            return render_template_string(HTML_PAGE, error=error)
        
        return jsonify({'result': result})

    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    calculator.run(debug=True)

if __name__ == '__main__':
    calculator.run(debug=True)

