#!/bin/bash

echo "🚀 Starting OmniTide SwarmAI Full Setup..."

# Ensure script runs as root
if [[ $EUID -ne 0 ]]; then
   echo "⚠️  Please run as root (use sudo)."
   exit 1
fi

# Set base directory
BASE_DIR="$HOME/omnitide_swarmai"

# Update & upgrade system
echo "🔍 Updating system..."
apt update && apt upgrade -y

# Install required dependencies
echo "📦 Installing system dependencies..."
apt install -y git python3 python3-pip sqlite3 ffmpeg libssl-dev tk cron nginx curl ufw unzip jq systemd docker.io chromium-chromedriver

# Install Python dependencies
echo "🐍 Installing Python libraries..."
pip3 install --upgrade pip
pip3 install fastapi uvicorn requests loguru flask flask_cors watchdog psutil openai jsonschema torch transformers beautifulsoup4 selenium weaviate pinecone-client

# Set up directories
echo "📂 Creating necessary directories..."
mkdir -p $BASE_DIR/{config,logs,scripts,services,core_team,ai_clones,models,backups,knowledge}

# Clone latest system files
echo "📦 Cloning OmniTide SwarmAI repository..."
git clone https://github.com/mrpongalfer/omnitide_swarmai.git $BASE_DIR

# Configure firewall
echo "🛡 Configuring firewall..."
ufw allow 22/tcp
ufw allow 5000/tcp
ufw enable

# Create AI system services
echo "⚙️  Configuring AI Services..."
cat <<EOF > /etc/systemd/system/omnitide_swarmai.service
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
systemctl daemon-reload
systemctl enable omnitide_swarmai
systemctl start omnitide_swarmai

# Start the system
echo "🚀 Launching OmniTide SwarmAI..."
bash $BASE_DIR/start.sh

echo "✅ Setup complete! 🚀 System is now running."
echo "📌 Access Web UI at: http://localhost:5000"
