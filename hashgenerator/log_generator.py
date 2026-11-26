import uuid
import time
from datetime import datetime, timezone

random_string = str(uuid.uuid4())

while True:
    timestamp = datetime.now(timezone.utc).isoformat(
        timespec="milliseconds"
    ).replace("+00:00", "Z")

    log_line = f"{timestamp}: {random_string}\n"

    with open("/app/files/log.txt", "a") as file:
        file.write(log_line)

    print(log_line, end="", flush=True)

    time.sleep(5)
