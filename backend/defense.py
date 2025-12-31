import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(BASE_DIR, "logs", "traffic.log")

def block_ip(ip):
    print(f"🚫 Autonomous Defense Activated")
    print(f"🚫 Blocking IP: {ip}")

    with open(log_file, "a") as f:
        f.write(f"DEFENSE BLOCKED IP={ip}\n")
