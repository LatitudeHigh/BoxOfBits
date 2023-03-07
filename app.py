from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Box of Bits</p>"

@app.route('/json', methods=['POST'])
def post_data():
    if not request.is_json:
        return "bad request :(", 403
    content = request.get_json()
    return f"{content}", 201


@app.route('/test/<word>/')
def capitalize(word):
    return f'<h1>{word}</h1>', 200