import time
import os
from defense import block_ip

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(BASE_DIR, "logs", "traffic.log")

def analyze():
    attack_count = 0
    ip = ""

    with open(log_file, "r") as f:
        for line in f:
            if "login_failed" in line:
                attack_count += 1
                ip = line.split("IP=")[1].strip()

    if attack_count >= 5:
        print("⚠️ Attack Detected by Agentic AI")
        block_ip(ip)

while True:
    analyze()
    time.sleep(5)
