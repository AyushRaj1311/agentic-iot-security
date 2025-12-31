import time
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(BASE_DIR, "logs", "traffic.log")

while True:
    with open(log_file, "a") as f:
        f.write("DEVICE camera NORMAL_TRAFFIC\n")
    time.sleep(3)
