
import os
import time
import urllib.request
from flask import Flask, send_file

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 3000))

CACHE_DIR = "/app/cache"
IMAGE_FILE = os.path.join(CACHE_DIR, "image.jpg")
CACHE_DURATION = 600

todos = [
    "Learn Kubernetes",
    "Complete the DevOps course",
    "Build a Todo application"
]


@app.route("/")
def home():
    todo_list = ""

    for todo in todos:
        todo_list += f"<li>{todo}</li>"

    return f"""
        <h1>Todo App</h1>

        <form>
            <input
                type="text"
                name="todo"
                maxlength="140"
                placeholder="Enter a todo..."
            >
            <button type="button">Send</button>
        </form>

        <h2>Todo list</h2>
        <ul>
            {todo_list}
        </ul>

        <h2>Random picture</h2>
        <img src="/image" alt="Random picture" width="600">
    """


@app.route("/image")
def get_image():
    os.makedirs(CACHE_DIR, exist_ok=True)

    if os.path.exists(IMAGE_FILE):
        image_age = time.time() - os.path.getmtime(IMAGE_FILE)
    else:
        image_age = CACHE_DURATION + 1

    if image_age >= CACHE_DURATION:
        try:
            with urllib.request.urlopen("https://picsum.photos/1200") as response:
                with open(IMAGE_FILE + ".tmp", "wb") as file:
                    file.write(response.read())

            os.replace(IMAGE_FILE + ".tmp", IMAGE_FILE)

        except Exception:
            if not os.path.exists(IMAGE_FILE):
                raise

    return send_file(IMAGE_FILE, mimetype="image/jpeg")


if __name__ == "__main__":
    print(f"Server started in port {PORT}", flush=True)
    app.run(host="0.0.0.0", port=PORT)

