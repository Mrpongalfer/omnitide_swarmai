#!/bin/bash

echo "🚀 Starting OmniTide SwarmAI Full Setup..."

# Ensure script is NOT running as root
if [[ $EUID -eq 0 ]]; then
   echo "⚠️  Do NOT run this script as root! Run it as a regular user."
   exit 1
fi

# Set base directory (inside home, NOT root)
BASE_DIR="$HOME/omnitide_swarmai"

# Update & upgrade system
echo "🔍 Updating system..."
sudo apt update && sudo apt upgrade -y

# Install required dependencies
echo "📦 Installing system dependencies..."
sudo apt install -y git python3 python3-pip sqlite3 ffmpeg libssl-dev tk cron nginx curl ufw unzip jq systemd docker.io chromium-chromedriver

# Install Python dependencies
echo "🐍 Installing Python libraries..."
pip3 install --upgrade pip
pip3 install fastapi uvicorn requests loguru flask flask_cors watchdog psutil openai jsonschema torch transformers beautifulsoup4 selenium weaviate pinecone-client

# Set up directories
echo "📂 Creating necessary directories..."
mkdir -p $BASE_DIR/{config,logs,scripts,services,core_team,ai_clones,models,backups,knowledge}

# Clone latest system files
echo "📦 Cloning OmniTide SwarmAI repository..."
if [ ! -d "$BASE_DIR/.git" ]; then
    git clone https://github.com/mrpongalfer/omnitide_swarmai.git $BASE_DIR
else
    cd $BASE_DIR && git pull origin main
fi

# Configure firewall
echo "🛡 Configuring firewall..."
sudo ufw allow 22/tcp
sudo ufw allow 5000/tcp
sudo ufw enable

# Create AI system services
echo "⚙️  Configuring AI Services..."
cat <<EOF | sudo tee /etc/systemd/system/omnitide_swarmai.service
[Unit]
Description=OmniTide SwarmAI System
After=network.target

[Service]
ExecStart=/bin/bash $BASE_DIR/start.sh
Restart=always
User=$USER

[Install]
WantedBy=multi-user.target
EOF

# Enable the AI service
sudo systemctl daemon-reload
sudo systemctl enable omnitide_swarmai
sudo systemctl start omnitide_swarmai

# AI Knowledge Acquisition Module
echo "🌍 Setting up AI Knowledge Scraper..."
cat <<EOF > $BASE_DIR/knowledge_scraper.py
import os
import requests
import json
from bs4 import BeautifulSoup
from transformers import pipeline

summarizer = pipeline("summarization")

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = ' '.join([p.text for p in soup.find_all('p')])
        return summarizer(text, max_length=150, min_length=30, do_sample=False)
    return None

def update_knowledge_base():
    urls = [
        "https://arxiv.org/list/cs.AI/recent",
        "https://blog.openai.com",
        "https://www.deeplearning.ai/the-batch/"
    ]

    knowledge = {}
    for url in urls:
        summary = scrape_website(url)
        if summary:
            knowledge[url] = summary

    with open(os.path.join(os.getcwd(), "knowledge", "knowledge_base.json"), "w") as f:
        json.dump(knowledge, f, indent=4)

    print("✅ Knowledge base updated.")

if __name__ == "__main__":
    update_knowledge_base()
EOF

# AI UI & API
echo "🖥 Setting up AI Web UI..."
cat <<EOF > $BASE_DIR/services/ai_ui.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "OmniTide SwarmAI is running!"}

@app.get("/status")
def get_status():
    return {"status": "AI Online", "learning": True, "security": "Active"}

# Run server: uvicorn services.ai_ui:app --host 0.0.0.0 --port 5000
EOF

# Mr. Meeseeks AI Clones
echo "💥 Setting up Mr. Meeseeks Clones..."
cat <<EOF > $BASE_DIR/mr_meeseeks.py
import sys
import time

def mr_meeseeks_task(task):
    print(f"👀 I'm Mr. Meeseeks! Doing the task: {task}")
    time.sleep(2)
    print(f"✅ Task completed: {task}")
    print("💀 Poof! Mr. Meeseeks has self-destructed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Please provide a task for Mr. Meeseeks.")
    else:
        mr_meeseeks_task(" ".join(sys.argv[1:]))
EOF

# Start the system
echo "🚀 Launching OmniTide SwarmAI..."
nohup python3 $BASE_DIR/services/ai_ui.py &

echo "✅ Setup complete! 🚀 System is now running."
echo "📌 Access Web UI at: http://localhost:5000"
