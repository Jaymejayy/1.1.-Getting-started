import uuid
import time
from datetime import datetime, timezone

# Generate a random UUID when the application starts
random_string = str(uuid.uuid4())

print("Application started!")
print(f"Generated string: {random_string}")

# Keep running forever
while True:

    # Get the current UTC timestamp
    timestamp = datetime.now(timezone.utc).isoformat(
        timespec="milliseconds"
    ).replace("+00:00", "Z")

    # Print timestamp and the same random string
    print(f"{timestamp}: {random_string}", flush=True)

    # Wait 5 seconds
    time.sleep(5)
