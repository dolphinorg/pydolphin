# dolphin

a convenient solution to heroku web apps / APIs.


# installation.

```text
pip3 install dolphin

or 

pip3 install --no-cache git+https://github.com/dolphinorg/dolphin.git
```

# basic example.
```py

import os
from flask import Flask
from dolphin import dolphin

PORT = int(os.environ.get("PORT", 6969))

app = Flask(__name__)

@app.before_first_request
def dolphin_start():
    dolphin.swim()

@app.route('/')
def index():
    return 'hello'

app.run(host='0.0.0.0', port=PORT)
```

# note.

=> i am currently learning js and node-js but 
   if you want to contribute to make an packages 
you can contact me t.me/midnightmadwalk.
=> use it in any python web framework and
   report bug or contribute. 
