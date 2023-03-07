from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/json', methods=['POST'])
def post_data():
    print("hello")
    if not request.is_json:
        return "bad request :(", 403
    content = request.get_json()
    return f"{content}", 201