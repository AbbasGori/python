from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World! I am Abbas Gori"

if __name__ == '__main__':
    app.run(host='ec2-35-175-238-145.compute-1.amazonaws.com', port=80)

