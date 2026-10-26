from flask import Flask
import os
import socket

app = Flask(__name__)


@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "v1")
    return (
        "<h1>Hello from EKS - deployed by GitHub Actions</h1>"
        f"<p>Version: {version}</p>"
        f"<p>Served by pod: {socket.gethostname()}</p>"
    )


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
