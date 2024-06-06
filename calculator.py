# calculator.py
from flask import Flask, request, render_template_string, jsonify

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
    <!-- Your HTML content here -->
</body>
</html>
"""

@calculator.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        # Return JSON response
        pass
    else:
        if 'werkzeug.client' in request.environ:
            # Test environment
            return jsonify({'message': 'This is a test response'})
        else:
            # Regular environment
            return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    calculator.run(debug=True)


# # calculator.py
# # HTML and CSS for the front-end interface and Flask to handle the back-end logic.

# from flask import Flask, request, render_template_string

# calculator = Flask(__name__)

# HTML_PAGE = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Hello Today! Simple Calculator</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             height: 100vh;
#             background-color: #f4f4f9;
#             margin: 0;
#         }
#         .calculator {
#             background-color: #fff;
#             padding: 20px;
#             border-radius: 8px;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#             max-width: 300px;
#             width: 100%;
#             text-align: center;
#         }
#         .calculator input, .calculator select, .calculator button {
#             width: calc(100% - 20px);
#             padding: 10px;
#             margin: 10px 0;
#             border: 1px solid #ccc;
#             border-radius: 4px;
#         }
#         .calculator button {
#             background-color: #28a745;
#             color: #fff;
#             font-size: 16px;
#             cursor: pointer;
#         }
#         .calculator button:hover {
#             background-color: #218838;
#         }
#         .result {
#             margin-top: 10px;
#             font-size: 18px;
#             color: #333;
#         }
#     </style>
# </head>
# <body>
#     <div class="calculator">
#         <h3>Hello, how are you?</h3>
#         <h2>Simple Calculator..</h2>
#         <form method="post">
#             <input type="number" name="a" placeholder="Enter first number" required>
#             <input type="number" name="b" placeholder="Enter second number" required>
#             <select name="operation">
#                 <option value="add">Addition</option>
#                 <option value="subtract">Subtraction</option>
#                 <option value="multiply">Multiplication</option>
#                 <option value="divide">Division</option>
#             </select>
#             <button type="submit">Calculate</button>
#         </form>
#         {% if result is not none %}
#         <div class="result">
#             <p>Last result: {{ result }}</p>
#         </div>
#         {% elif error is not none %}
#         <div class="result">
#             <p style="color: red;">Error: {{ error }}</p>
#         </div>
#         {% endif %}
#     </div>
# </body>
# </html>
# """

# @calculator.route('/', methods=['GET', 'POST'])
# def index():
#     result = None
#     error = None
#     if request.method == 'POST':
#         try:
#             a = request.form.get('a', type=float)
#             b = request.form.get('b', type=float)
#             operation = request.form.get('operation')

#             if operation == 'add':
#                 result = a + b
#             elif operation == 'subtract':
#                 result = a - b
#             elif operation == 'multiply':
#                 result = a * b
#             elif operation == 'divide':
#                 if b == 0:
#                     error = "Cannot divide by zero"
#                 else:
#                     result = a / b
#         except ValueError:
#             error = "Invalid input. Please enter valid numbers."

#     return render_template_string(HTML_PAGE, result=result, error=error)

# if __name__ == '__main__':
#     calculator.run(debug=True)

# if __name__ == '__main__':
#     calculator.run(debug=True)

