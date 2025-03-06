import os
import json
import time
import threading
import subprocess
import psutil
import requests
from datetime import datetime

# Core AI Functions
def monitor_performance():
    """Tracks CPU & memory usage and adjusts AI load dynamically."""
    while True:
        usage = psutil.cpu_percent(interval=2)
        memory = psutil.virtual_memory().percent
        print(f"Tony Stark AI: CPU {usage}%, Memory {memory}%")
        if usage > 80 or memory > 85:
            print("⚠️ High usage detected—optimizing AI load.")
            subprocess.run(["renice", "-n", "10", "-p", str(os.getpid())])
        time.sleep(5)

def security_scan():
    """Runs AI-driven security scans and adjusts firewall rules."""
    while True:
        threats = subprocess.getoutput("cat /var/log/auth.log | tail -n 5")
        if "failed password" in threats:
            print("🚨 Security Alert: Unauthorized access attempt detected!")
            subprocess.run(["sudo", "ufw", "deny", "22"])
        time.sleep(10)

def recursive_debugging():
    """Self-fixes AI scripts by detecting and repairing errors automatically."""
    while True:
        errors = subprocess.getoutput("grep 'error' $HOME/omnitide_swarmai/logs/system.log")
        if errors:
            print(f"Rick Sanchez AI: Fixing Errors -> {errors}")
            subprocess.run(["python3", "$HOME/omnitide_swarmai/self_fix.py"])
        time.sleep(15)

def backup_ai_system():
    """Automatically backs up AI data using rsync."""
    while True:
        print("Power AI: Running AI backup process.")
        subprocess.run(["rsync", "-a", "$HOME/omnitide_swarmai", "/backups/"])
        time.sleep(3600)

# Running AI Functions in Parallel
ai_threads = [
    threading.Thread(target=monitor_performance),
    threading.Thread(target=security_scan),
    threading.Thread(target=recursive_debugging),
    threading.Thread(target=backup_ai_system)
]

# Start AI processes
for thread in ai_threads:
    thread.daemon = True
    thread.start()

print("✅ Core AI Agents are now active & running in the background.")

while True:
    time.sleep(60)
