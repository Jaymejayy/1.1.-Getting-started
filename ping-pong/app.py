from flask import Flask

app = Flask(__name__)

# Counter stored in application memory
counter = 0


@app.route("/pingpong", methods=["GET"])
def pingpong():
    global counter

    response = f"pong {counter}"
    counter += 1

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
