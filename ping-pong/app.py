
from flask import Flask

app = Flask(__name__)

pongs = 0


@app.route("/pingpong", methods=["GET"])
def pingpong():
    global pongs

    response = f"pong {pongs}"
    pongs += 1

    return response


@app.route("/pongs", methods=["GET"])
def get_pongs():
    return str(pongs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

