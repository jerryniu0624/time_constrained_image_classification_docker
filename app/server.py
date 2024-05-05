from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/addCalc', methods=['POST'])
def addCalc():
   print(request.values)
   num1=request.values.get('num1')
   num2 = request.values.get('num2')
   return num1+num2

if __name__ == '__main__':
   app.run(port = 9000)