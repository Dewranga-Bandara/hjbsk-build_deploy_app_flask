from flask import Flask, render_template, request
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")

def perform_operation(route_function):
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = route_function(num1, num2)
        return str(result)
    except ValueError:
        return "Error: Please enter valid numerical values."

@app.route("/sum")
def sum_route():
    return perform_operation(summation)

@app.route("/sub")
def sub_route():
    return perform_operation(subtraction)

@app.route("/mul")
def mul_route():
    return perform_operation(multiplication)

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
