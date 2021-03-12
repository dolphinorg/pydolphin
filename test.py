import os
from flask import Flask
from pydolphin import dolphin


app = Flask(__name__)

@app.before_first_request
def dolphin_start():
    dolphin.swim()

@app.route('/')
def index():
    return 'hello'

port = int(os.environ.get("PORT", 6969))
app.run(host='0.0.0.0', port=port)
