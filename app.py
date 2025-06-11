from flask import Flask
import subprocess
import time
from flask import request

app = Flask(__name__)

# Helper function to flash the light for a given duration (in seconds)
def flash_light(duration):
    try:
        subprocess.run(
            ["timeout", str(duration), "cat", "/dev/video0"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
    except subprocess.CalledProcessError:
        pass

# Morse code pattern for SOS: ... --- ...
# Dot: 0.2s, Dash: 0.6s, Intra-symbol gap: 0.2s, Letter gap: 0.6s
@app.route("/sos", methods=["GET"])
def sos():
    pattern = [0.2, 0.2, 0.2, 0.6, 0.6, 0.6, 0.2, 0.2, 0.2]  # durations for flashes
    gaps =   [0.2, 0.2, 0.6, 0.2, 0.2, 0.6, 0.2, 0.2]        # gaps between flashes
    try:
        for i, duration in enumerate(pattern):
            flash_light(duration)
            if i < len(gaps):
                time.sleep(gaps[i])
        return "Flashed SOS pattern.", 200
    except Exception as e:
        return f"Failed to flash SOS: {e}", 500

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
