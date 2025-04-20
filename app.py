###
# TWOJ KOD API 
###

from flask import Flask
from flask import request
from flask import jsonify


# Create a flask
app = Flask(__name__)

# Create an API end point
@app.route('/hello', methods=['GET'])
def say_hello():
    name = request.args.get("name", "")
    title = request.args.get("title", "")
    if name:
        resp = f"Hello {title} {name}" if title else f"Hello {name}!"
    else:
        resp = f"Hello {title}" if title else "Hello"
    return jsonify(output=resp)


@app.route('/api/v1.0/predict', methods = ['GET'])
def predict():
    num1 = request.args.get("num1", "")
    num2 = request.args.get("num2", "")
    if num1 and num2:
        try:
            num1 = float(num1)
            num2 = float(num2)
            resp = 1 if (num1 + num2) > 5.8 else 0
            return jsonify(
                prediction=resp,
                features={"num1": num1, "num2": num2}
            )
        except ValueError:
            return jsonify(output="Proszę podać poprawne liczby."), 400
    else:
        return jsonify(output="Proszę podać 2 liczby."), 400

if __name__ == '__main__':
    app.run(port=5000)
