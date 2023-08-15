from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Helo'

@app.route("/calculator/add", methods=['POST'])
def add():
    num1=request.json.get('first')
    num2=request.json.get('second')
    result=num1+num2
    response={"result:",result}
    return jsonify(response)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    num1=request.json.get('first')
    num2=request.json.get('second')
    result=num1-num2
    response={"result:",result}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
