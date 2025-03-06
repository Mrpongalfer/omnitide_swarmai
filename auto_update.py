import os
import subprocess
import time

BASE_DIR = os.path.expanduser("~/omnitide_swarmai")

def update_system():
    """Pull latest updates, apply patches, restart services."""
    print("🚀 Updating OmniTide SwarmAI...")
    subprocess.run(["git", "-C", BASE_DIR, "pull", "origin", "main"])
    subprocess.run(["bash", os.path.join(BASE_DIR, "install.sh")])
    print("✅ Update complete!")

while True:
    update_system()
    time.sleep(3600)  # Check for updates every hour
