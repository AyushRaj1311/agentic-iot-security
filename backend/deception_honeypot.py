from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def fake_camera():
    if request.method == "POST":
        print("🎭 Attacker trapped!")
        print("Credentials:", request.form)
    return """
    <h2>Smart Camera Login</h2>
    <form method="post">
        Username: <input name="user"><br>
        Password: <input name="pass" type="password"><br>
        <input type="submit">
    </form>
    """

app.run(port=8080)
