import os
import socket
import random
from flask import Flask
from flask import render_template


app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR') or random.choice(["red","green","blue","blue2","darkblue",])
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

@app.route("/")
def main():
    return render_template('index.html', name=hostname, local_ip=local_ip, color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('index.html',name=hostname, local_ip=local_ip, color=color_codes[new_color])    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

