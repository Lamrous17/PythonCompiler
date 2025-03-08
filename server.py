from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_code():
    data = request.json
    code = data.get("code", "")

    try:
        output = subprocess.run(["python3", "-c", code], capture_output=True, text=True, timeout=5)
        return jsonify({"output": output.stdout + output.stderr})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Render использует порты выше 10000
