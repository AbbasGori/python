
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():

    return "Hello World!run"

if __name__ == '__main__':
    app.run(host='ec2-34-229-181-0.compute-1.amazonaws.com',port=80)
