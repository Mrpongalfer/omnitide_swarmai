from fastapi import FastAPI
import uvicorn
import subprocess
import os

app = FastAPI()

# Define Core Team Functions
CORE_TEAM_FUNCTIONS = {
    "Tony Stark": ["Monitor Performance", "Optimize AI Execution"],
    "Rick Sanchez": ["Run Recursive Debugging", "AI Self-Repair"],
    "Sherlock Holmes": ["Security Threat Analysis", "AI Forensic Investigation"],
    "Rocket Raccoon": ["Penetration Testing", "Monitor Firewall"],
    "Yoda": ["Task Prioritization", "Resource Load Balancing"],
    "Harley Quinn": ["Run Chaos Testing", "Simulate AI Stress"],
    "Power": ["Backup AI System", "Restore AI Failover"],
    "Makima": ["AI Task Coordination", "Workflow Optimization"],
    "Denji": ["Optimize Power Usage", "Scale AI Processing"],
    "Deku": ["Ensure Task Persistence", "Monitor Long-Term AI Execution"],
    "All Might": ["Track AI Stability", "Enhance AI Uptime"],
}

# Define Real Submenus with Functional Commands
SUBMENUS = {
    "System Monitoring": [
        {"name": "CPU Usage", "command": "top -b -n1 | grep 'Cpu(s)'"},
        {"name": "Memory Usage", "command": "free -m"},
        {"name": "AI Task Execution Log", "command": "tail -n 10 $HOME/omnitide_swarmai/logs/system.log"}
    ],
    "Security & Firewall": [
        {"name": "Run Security Scan", "command": "sudo ufw status"},
        {"name": "Monitor Firewall Logs", "command": "sudo journalctl -u ufw --no-pager | tail -n 10"},
        {"name": "Detect Intrusions", "command": "cat /var/log/auth.log | tail -n 10"}
    ],
    "AI Task Management": [
        {"name": "View AI Workload", "command": "ps aux --sort=-%cpu | head -10"},
        {"name": "Adjust AI Task Priority", "command": "renice -n 10 -p $(pgrep python3)"},
        {"name": "Enable/Disable AI Modules", "command": "systemctl list-units --type=service --all"}
    ],
    "AI Research & Intelligence": [
        {"name": "Web Scraper", "command": "python3 $HOME/omnitide_swarmai/knowledge_scraper.py"},
        {"name": "AI Trend Analysis", "command": "python3 $HOME/omnitide_swarmai/trend_analysis.py"},
        {"name": "Machine Learning Insights", "command": "python3 $HOME/omnitide_swarmai/ml_insights.py"}
    ],
}

@app.get("/")
def home():
    return {
        "message": "OmniTide SwarmAI is running!",
        "status": "Online",
        "menu": "/menu",
        "monitoring": "/monitor",
        "security": "/security",
        "ai_tasks": "/ai-tasks"
    }

@app.get("/menu")
def menu():
    return {
        "Core Team AI Functions": CORE_TEAM_FUNCTIONS,
        "System Menus": SUBMENUS
    }

@app.get("/monitor")
def monitor():
    return {
        key["name"]: subprocess.getoutput(key["command"])
        for key in SUBMENUS["System Monitoring"]
    }

@app.get("/security")
def security():
    return {
        key["name"]: subprocess.getoutput(key["command"])
        for key in SUBMENUS["Security & Firewall"]
    }

@app.get("/ai-tasks")
def ai_tasks():
    return {
        "Available AI Tasks": [key["name"] for key in SUBMENUS["AI Task Management"]],
        "Execute a task": "/run-task?task=Optimize Performance"
    }

@app.get("/run-task")
def run_task(task: str):
    task_command = next((item["command"] for item in SUBMENUS["AI Task Management"] if item["name"] == task), None)
    if task_command:
        result = subprocess.getoutput(task_command)
        return {"Executing Task": task, "Output": result}
    return {"Error": "Task not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
