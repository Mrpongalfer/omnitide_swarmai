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

# Define Submenus
SUBMENUS = {
    "System Monitoring": ["CPU Usage", "Memory Usage", "AI Task Execution Log"],
    "Security & Firewall": ["Run Security Scan", "Monitor Firewall Logs", "Detect Intrusions"],
    "AI Task Management": ["View AI Workload", "Adjust AI Task Priority", "Enable/Disable AI Modules"],
    "AI Research & Intelligence": ["Web Scraper", "AI Trend Analysis", "Machine Learning Insights"],
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
    cpu_usage = subprocess.getoutput("top -b -n1 | grep 'Cpu(s)'")
    memory_usage = subprocess.getoutput("free -m")
    return {
        "CPU Usage": cpu_usage,
        "Memory Usage": memory_usage,
        "AI Logs": subprocess.getoutput("tail -n 10 $HOME/omnitide_swarmai/logs/system.log")
    }

@app.get("/security")
def security():
    return {
        "Security Scan": subprocess.getoutput("sudo ufw status"),
        "Firewall Logs": subprocess.getoutput("sudo journalctl -u ufw --no-pager | tail -n 10"),
        "Intrusion Detection": subprocess.getoutput("cat /var/log/auth.log | tail -n 10")
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
        ],
        "Execute a task": "/run-task?task=Optimize Performance"
    }

@app.get("/run-task")
def run_task(task: str):
    return {"Executing Task": task, "Status": "Task is running in background"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
