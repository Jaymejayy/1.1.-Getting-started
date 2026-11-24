import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_logs():
    with open("/app/files/log.txt", "r") as file:
        return file.read(), 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
