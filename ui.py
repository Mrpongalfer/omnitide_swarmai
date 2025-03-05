from fastapi import FastAPI
import uvicorn
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OmniTide SwarmAI is running!", "status": "Online"}

@app.get("/menu")
def menu():
    return {
        "Monitor System": "/monitor",
        "Run AI Task": "/run-task?task=example",
        "Scan Network": "/scan-network"
    }

@app.get("/monitor")
def monitor():
    cpu_usage = subprocess.getoutput("top -b -n1 | grep 'Cpu(s)'")
    return {"CPU Usage": cpu_usage}

@app.get("/run-task")
def run_task(task: str):
    result = subprocess.getoutput(f"python3 ai_tasks/{task}.py")
    return {"Task Executed": task, "Output": result}

@app.get("/scan-network")
def scan_network():
    result = subprocess.getoutput("arp -a")
    return {"Network Scan Results": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
