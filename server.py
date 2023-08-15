from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Helo'

@app.route("/calculator/add", methods=['POST'])
def add():
    num1=request.json.get('first')
    num2=request.json.get('second')
    return jsonify(num1+num2)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    num1=request.json.get('first')
    num2=request.json.get('second')
    print(num1-num2)
    return jsonify(num1-num2)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
