# calculate.py
# HTML and CSS for the front-end interface and Flask to handle the back-end logic.

# app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f9;
            margin: 0;
        }
        .calculator {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .calculator input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .calculator button {
            width: 100%;
            padding: 10px;
            border: none;
            background-color: #28a745;
            color: #fff;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        .calculator button:hover {
            background-color: #218838;
        }
        .result {
            margin-top: 10px;
            font-size: 18px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h2>Simple Calculator</h2>
        <form method="post">
            <input type="number" name="a" placeholder="Enter first number" required>
            <input type="number" name="b" placeholder="Enter second number" required>
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}
        <div class="result">
            <p>Result: {{ result }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        a = request.form.get('a', type=float)
        b = request.form.get('b', type=float)
        result = a + b
    return render_template_string(HTML_PAGE, result=result)

if __name__ == '__main__':
    app.run(debug=True)

