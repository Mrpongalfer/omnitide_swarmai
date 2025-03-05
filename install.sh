#!/bin/bash

echo "🚀 Starting OmniTide SwarmAI Full Setup..."

# Ensure script is NOT running as root
if [[ $EUID -eq 0 ]]; then
   echo "⚠️  Do NOT run this script as root! Run it as a regular user."
   exit 1
fi

# Set base directory
BASE_DIR="$HOME/omnitide_swarmai"

# Update & upgrade system
sudo apt update && sudo apt upgrade -y

# Install required dependencies
sudo apt install -y git python3 python3-pip sqlite3 ffmpeg libssl-dev tk cron nginx curl ufw unzip jq systemd docker.io chromium-chromedriver

# Install Python dependencies
pip3 install --upgrade pip
pip3 install fastapi uvicorn requests loguru flask flask_cors watchdog psutil openai jsonschema torch transformers beautifulsoup4 selenium weaviate pinecone-client

# Set up directories
mkdir -p $BASE_DIR/{config,logs,scripts,services,core_team,ai_clones,models,backups,knowledge}

# Clone latest system files
if [ ! -d "$BASE_DIR/.git" ]; then
    git clone https://github.com/mrpongalfer/omnitide_swarmai.git $BASE_DIR
else
    cd $BASE_DIR && git pull origin main
fi

# Configure firewall
sudo ufw allow 22/tcp
sudo ufw allow 5000/tcp
sudo ufw enable

# Enable AI system service
sudo systemctl daemon-reload
sudo systemctl enable omnitide_swarmai
sudo systemctl start omnitide_swarmai

# Start the UI and AI monitoring system
nohup python3 $BASE_DIR/ui.py &

echo "✅ Setup complete! 🚀 System is now running."
echo "📌 Access Web UI at: http://localhost:5000"
echo "📌 Use the interactive AI menu at: http://localhost:5000/menu"
