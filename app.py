from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your Flask App!"

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return jsonify(result=a * b)

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        return jsonify(error="Division by zero is not allowed"), 400
    return jsonify(result=a / b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
