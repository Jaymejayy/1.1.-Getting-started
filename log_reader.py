import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_logs():
    with open("/app/files/log.txt", "r") as file:
        logs = file.read()

    counter_file = "/app/files/pingpong.txt"

    if os.path.exists(counter_file):
        with open(counter_file, "r") as file:
            counter = file.read()
    else:
        counter = "0"

    response = logs + f"\nPing / Pongs: {counter}\n"

    return response, 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
