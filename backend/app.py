from flask import Flask
import os

app = Flask(__name__)

log_path = os.getenv("LOG_PATH", "/logs")
name = "<your name>"

@app.route('/')
def home():
    return f"Hello from Flask backend of {name}!"

@app.route('/log')
def write_log():
    with open(f"{log_path}/{name}_access.log", "a") as f:
        f.write("Flask route /log was accessed\n")
    return "Log entry added."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)