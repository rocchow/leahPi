#!/bin/bash
# Direct deployment via rsync (fastest, no GitHub needed)
# Usage: ./deploy-direct.sh [pi-ip-address] [pi-username]

PI_IP=${1:-"raspberrypi.local"}  # Default to raspberrypi.local or provide IP
PI_USER=${2:-"pi"}                # Default username is 'pi'
PROJECT_DIR="~/leahPi"            # Adjust if different on Pi

echo "🚀 Direct deployment to Raspberry Pi..."
echo "📡 Target: ${PI_USER}@${PI_IP}"
echo "📁 Project: ${PROJECT_DIR}"

# Exclude unnecessary files
rsync -avz --progress \
  --exclude '.git' \
  --exclude '__pycache__' \
  --exclude '*.pyc' \
  --exclude '.DS_Store' \
  --exclude '*.log' \
  --exclude 'venv/' \
  --exclude '.venv/' \
  ./ ${PI_USER}@${PI_IP}:${PROJECT_DIR}/

echo "✅ Direct deployment complete!"
