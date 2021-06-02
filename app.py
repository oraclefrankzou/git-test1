import socket
from flask import Flask
import json
import datetime


app=Flask(__name__)

@app.route('/')
def hello():
     return json.dumps({'date14': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'host':socket.gethostname()})


if __name__ == '__main__':
   app.run(host='0.0.0.0')
