from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/trigger", methods=["GET"])
def trigger_camera():
    try:
        subprocess.run(
            ["timeout", "1", "cat", "/dev/video0"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        return "Camera triggered (red light should be on briefly).", 200
    except subprocess.CalledProcessError:
        return "Failed to access camera device.", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5021)
