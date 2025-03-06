from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Define real commands for each AI function
CORE_TEAM_FUNCTIONS = {
    "Tony Stark": "top -b -n1 | grep 'Cpu(s)'",
    "Rick Sanchez": "python3 ai_auto_debugger.py",
    "Sherlock Holmes": "sudo cat /var/log/auth.log | tail -n 10",
    "Rocket Raccoon": "sudo nmap -sV localhost",
    "Yoda": "ps aux --sort=-%cpu | head -10",
    "Harley Quinn": "stress-ng --cpu 2 --timeout 10s",
    "Power": "rsync -a --delete ~/omnitide_swarmai/backups/ ~/omnitide_swarmai/",
    "Makima": "python3 ai_task_coordinator.py",
    "Denji": "cpufreq-info",
    "Deku": "systemctl restart omnitide_swarmai",
    "All Might": "uptime"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/execute", methods=["POST"])
def execute():
    data = request.json
    command = CORE_TEAM_FUNCTIONS.get(data["function"], "echo 'Invalid function'")
    result = subprocess.getoutput(command)
    return jsonify({"output": result})

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "")
    response = f"Core Team AI Response: '{message}' received!"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
