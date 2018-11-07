from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='ec2-18-234-201-254.compute-1.amazonaws.com', port=22)

