from flask import Flask, request, jsonify
from sympy import symbols, Eq, solve

app = Flask(__name__)


@app.route('/solve', methods=['POST'])
def solve_equation():
    data = request.json
    equation = data.get('equation')

    x = symbols('x')

    # Split the equation at the equals sign
    if "=" in equation:
        lhs, rhs = equation.split("=")
    else:
        lhs, rhs = equation, "0"

    # Create the equation using SymPy's Eq
    eq = Eq(eval(lhs), eval(rhs))
    solution = solve(eq, x)

    return jsonify({'solution': str(solution)})


if __name__ == '__main__':
    app.run(debug=True)

