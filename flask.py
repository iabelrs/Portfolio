from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!!! 7u7"

app.run(port='8000')

