# calculator.py
# HTML and CSS for the front-end interface and Flask to handle the back-end logic.

from flask import Flask, request, render_template_string
import re

calculator = Flask(__name__)

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
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            max-width: 300px;
            width: 100%;
            text-align: center;
        }
        .calculator button {
            width: 50px;
            height: 50px;
            padding: 10px;
            margin: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        .calculator button:hover {
            background-color: #f0f0f0;
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
        <form method="post">
            <br>
            <input type="text" name="expression" id="expression" value="{{ expression }}" readonly>
            <br>
            <br>
            <button type="submit" name="digit" value="1">1</button>
            <button type="submit" name="digit" value="2">2</button>
            <button type="submit" name="digit" value="3">3</button>
            <button type="submit" name="operator" value="+">+</button>
            <br>
            <button type="submit" name="digit" value="4">4</button>
            <button type="submit" name="digit" value="5">5</button>
            <button type="submit" name="digit" value="6">6</button>
            <button type="submit" name="operator" value="-">-</button>
            <br>
            <button type="submit" name="digit" value="7">7</button>
            <button type="submit" name="digit" value="8">8</button>
            <button type="submit" name="digit" value="9">9</button>
            <button type="submit" name="operator" value="*">*</button>
            <br>
            <button type="submit" name="digit" value="0">0</button>
            <button type="submit" name="operator" value="/">/</button>
            <button type="submit" name="clear" value="clear">Del</button>
            <button type="submit" name="calculate" value="calculate">=</button>
        </form>
        {% if result is defined %}
        <h3>Outcome: {{ result }}</h3>
        {% endif %}
    </div>
</body>
</html>
"""

@calculator.route('/', methods=['GET', 'POST'])
def handle_calculator():
    expression = ''
    result = None

    if request.method == 'POST':
        expression = request.form.get('expression', '')

        if 'digit' in request.form:
            expression += request.form['digit']
        elif 'operator' in request.form:
            expression += ' ' + request.form['operator'] + ' '
        elif 'clear' in request.form:
            expression = ''
        elif 'calculate' in request.form:
            try:
                expression = re.sub(r'[^0-9+\-*/.\s]', '', expression)
                result = eval(expression)
            except Exception as e:
                result = 'Error: ' + str(e)

    return render_template_string(HTML_PAGE, expression=expression, result=result)

if __name__ == '__main__':
    calculator.run(debug=True)
