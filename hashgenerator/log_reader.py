
import os
import urllib.request
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_logs():
    with open("/app/files/log.txt", "r") as file:
        logs = file.read()

    with urllib.request.urlopen("http://ping-pong-svc:2345/pongs") as response:
        counter = response.read().decode("utf-8")

    response = logs + f"\nPing / Pongs: {counter}\n"

    return response, 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

