import uuid
import time
import threading
import os
from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)

# Generate a random UUID once when the application starts
random_string = str(uuid.uuid4())


# Function responsible for generating logs
def generate_logs():
    while True:
        timestamp = datetime.now(timezone.utc).isoformat(
            timespec="milliseconds"
        ).replace("+00:00", "Z")

        print(f"{timestamp}: {random_string}", flush=True)

        time.sleep(5)


# HTTP endpoint to return application status
@app.route("/")
def get_status():
    timestamp = datetime.now(timezone.utc).isoformat(
        timespec="milliseconds"
    ).replace("+00:00", "Z")

    return jsonify({
        "timestamp": timestamp,
        "randomString": random_string
    })


if __name__ == "__main__":

    # Start logging in a background thread
    logging_thread = threading.Thread(target=generate_logs)
    logging_thread.daemon = True
    logging_thread.start()

    # Start Flask web server
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
