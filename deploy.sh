#!/bin/bash
# Quick deployment script for Raspberry Pi
# Usage: ./deploy.sh [pi-ip-address] [pi-username]

PI_IP=${1:-"raspberrypi.local"}  # Default to raspberrypi.local or provide IP
PI_USER=${2:-"pi"}                # Default username is 'pi'
PROJECT_DIR="~/leahPi"            # Adjust if different on Pi

echo "🚀 Deploying to Raspberry Pi..."
echo "📡 Target: ${PI_USER}@${PI_IP}"
echo "📁 Project: ${PROJECT_DIR}"

# Push to GitHub first
echo "📤 Pushing to GitHub..."
git add .
git commit -m "Update: $(date +%Y-%m-%d\ %H:%M:%S)" || echo "No changes to commit"
git push

# SSH into Pi and pull
echo "⬇️  Pulling on Raspberry Pi..."
ssh ${PI_USER}@${PI_IP} "cd ${PROJECT_DIR} && git pull"

echo "✅ Deployment complete!"
