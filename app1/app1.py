from flask import request, Flask
import json

app1 = Flask(__name__)

@app1.route('/')

def hello_world():
    return "Hello, this is app1 of flask-nginx-loadbalancer-sample:)"
    
if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')
