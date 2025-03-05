from fastapi import FastAPI, Request
import uvicorn
import json
import os
import subprocess
from openai import OpenAI  # For NLP-based interactions

app = FastAPI()

# Load settings
SETTINGS_FILE = os.path.expanduser("~/omnitide_swarmai/config/settings.json")
if os.path.exists(SETTINGS_FILE):
    with open(SETTINGS_FILE, "r") as f:
        settings = json.load(f)
else:
    settings = {"openai_api_key": "", "ai_status": "Online"}

OPENAI_API_KEY = settings["openai_api_key"]

CORE_TEAM_FUNCTIONS = {
    "Tony Stark": ["Monitor System", "Optimize Performance"],
    "Rick Sanchez": ["Debug AI", "Recursive Error Fixing"],
    "Sherlock Holmes": ["Security Analysis", "Forensic Investigation"],
    "Rocket Raccoon": ["Firewall Management", "Threat Scanning"],
    "Yoda": ["Balance Workload", "Prioritize Tasks"],
    "Harley Quinn": ["Chaos Testing", "System Stress Tests"],
    "Power": ["Backup AI", "Failover Execution"],
    "Makima": ["Coordinate AI Agents", "Enhance Task Execution"],
    "Denji": ["Optimize Power Use", "Scale AI Processing"],
    "Deku": ["AI Task Persistence", "Monitor AI Sessions"],
    "All Might": ["Ensure Stability", "Boost AI Resilience"],
}

@app.get("/")
def home():
    return {
        "message": "OmniTide SwarmAI is running!",
        "status": settings.get("ai_status", "Unknown"),
        "dashboard": "/dashboard",
        "menu": "/menu",
        "chat": "/chat",
        "security": "/security",
        "ai-tasks": "/ai-tasks"
    }

@app.get("/dashboard")
def dashboard():
    return {
        "System Status": subprocess.getoutput("uptime"),
        "AI Running Processes": subprocess.getoutput("ps aux | grep python3"),
        "Recent Logs": subprocess.getoutput("tail -n 10 ~/omnitide_swarmai/logs/system.log")
    }

@app.get("/menu")
def menu():
    return {
        "Core Team Functions": CORE_TEAM_FUNCTIONS,
        "Available System Controls": [
            "Monitor CPU Usage",
            "Run AI Task",
            "Check Firewall",
            "Analyze AI Logs",
            "Enable AI Auto-Scaling"
        ]
    }

@app.get("/chat")
async def chat_with_ai(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    if not OPENAI_API_KEY:
        return {"error": "Missing OpenAI API Key. Update settings.json"}

    response = OpenAI(api_key=OPENAI_API_KEY).chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    return {"AI Response": response.choices[0].message["content"]}

@app.get("/security")
def security():
    return {
        "Firewall Status": subprocess.getoutput("sudo ufw status"),
        "Recent Security Logs": subprocess.getoutput("sudo journalctl -u ufw --no-pager | tail -n 10"),
        "Detected Threats": subprocess.getoutput("cat /var/log/auth.log | tail -n 10")
    }

@app.get("/ai-tasks")
def ai_tasks():
    return {
        "Available AI Tasks": [
            "Optimize Performance",
            "Run Debugging",
            "Monitor Security",
            "Balance AI Workload",
            "Run AI Stress Test"
        ]
    }

@app.get("/run-task")
def run_task(task: str):
    task_command = next((item for item in CORE_TEAM_FUNCTIONS if item in task), None)
    if task_command:
        result = subprocess.getoutput(f"python3 ~/omnitide_swarmai/scripts/{task_command.replace(' ', '_')}.py")
        return {"Executing Task": task, "Output": result}
    return {"Error": "Task not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
