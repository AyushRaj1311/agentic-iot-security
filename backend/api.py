from flask import Flask, jsonify, render_template
import os
from collections import defaultdict
import time

# ------------------ PATH SETUP ------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "frontend", "templates"),
    static_folder=os.path.join(BASE_DIR, "frontend", "static"),
    static_url_path="/static"
)

LOG_FILE = os.path.join(BASE_DIR, "logs", "traffic.log")

# ------------------ ROUTES ------------------

@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/status")
def status():
    traffic = 0
    attacks = 0
    blocked = set()

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            for line in f:
                if line.startswith("DEVICE"):
                    traffic += 1
                elif line.startswith("ATTACK"):
                    attacks += 1
                elif line.startswith("DEFENSE"):
                    blocked.add(line.split("IP=")[1].strip())

    return jsonify({
        "traffic": traffic,
        "attacks": attacks,
        "blocked_ips": list(blocked)
    })


@app.route("/api/attack-timeline")
def attack_timeline():
    timeline = defaultdict(int)

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            for line in f:
                if line.startswith("ATTACK"):
                    minute = time.strftime("%H:%M")
                    timeline[minute] += 1

    return jsonify(timeline)


@app.route("/logs")
def logs():
    entries = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            entries = f.readlines()[-100:]
    return render_template("logs.html", logs=entries)


@app.route("/devices")
def devices():
    return render_template(
        "devices.html",
        devices=[
            {"name": "Smart Camera", "status": "Active"},
            {"name": "Smart Bulb", "status": "Active"}
        ]
    )

# ------------------ START SERVER ------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
