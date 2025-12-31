import time
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(BASE_DIR, "logs", "traffic.log")

for i in range(8):
    with open(log_file, "a") as f:
        f.write("ATTACK login_failed IP=192.168.1.50\n")
    time.sleep(1)
