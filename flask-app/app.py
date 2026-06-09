from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Cyber Lab Dashboard</h1>

    <h2>Server Information</h2>

    <ul>
        <li>Hostname: {socket.gethostname()}</li>
        <li>Time: {datetime.datetime.now()}</li>
        <li>Status: Running</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)