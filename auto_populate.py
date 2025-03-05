import os
import json
import subprocess
import time

BASE_DIR = os.path.expanduser("~/omnitide_swarmai")

FOLDER_STRUCTURE = {
    "config": "Default AI system configuration",
    "logs": "System logs for AI execution tracking",
    "scripts": "AI automation scripts",
    "services": "Running AI services",
    "core_team": "AI agent scripts and models",
    "ai_clones": "Temporary AI instances for tasks",
    "models": "Machine learning and AI models",
    "backups": "Automated backups of AI knowledge and settings",
    "knowledge": "Data scraped and learned by AI over time"
}

def populate_folders():
    """Ensure all required folders exist and populate them with initial data."""
    for folder, description in FOLDER_STRUCTURE.items():
        folder_path = os.path.join(BASE_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)
        
        # Auto-populate files
        if folder == "config":
            config_file = os.path.join(folder_path, "settings.json")
            if not os.path.exists(config_file):
                with open(config_file, "w") as f:
                    json.dump({"AI_Status": "Online", "Learning_Mode": True}, f, indent=4)
        
        elif folder == "logs":
            log_file = os.path.join(folder_path, "system.log")
            open(log_file, "a").close()  # Create empty log file if not present
        
        elif folder == "scripts":
            script_file = os.path.join(folder_path, "monitor.py")
            if not os.path.exists(script_file):
                with open(script_file, "w") as f:
                    f.write("# AI System Monitoring Script\n")
        
        elif folder == "knowledge":
            knowledge_file = os.path.join(folder_path, "knowledge_base.json")
            if not os.path.exists(knowledge_file):
                with open(knowledge_file, "w") as f:
                    json.dump({}, f, indent=4)

    print("✅ All folders populated with required data.")

if __name__ == "__main__":
    populate_folders()
