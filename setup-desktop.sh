#!/bin/bash
# Setup desktop icon and auto-start service for Leah Learning App

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DESKTOP_FILE="$SCRIPT_DIR/leahpi.desktop"
SERVICE_FILE="$SCRIPT_DIR/leahpi.service"
RUN_SCRIPT="$SCRIPT_DIR/run-app.sh"
DESKTOP_DEST="$HOME/Desktop/leahpi.desktop"
SERVICE_DEST="/etc/systemd/system/leahpi.service"

echo "🖥️  Setting up Desktop Icon and Auto-Start Service"
echo "=================================================="

# Make run script executable
chmod +x "$RUN_SCRIPT"
echo "✅ Made run-app.sh executable"

# Update paths in desktop file
sed -i "s|/home/pi/leahPi|$SCRIPT_DIR|g" "$DESKTOP_FILE"
echo "✅ Updated paths in desktop file"

# Copy desktop file to Desktop
cp "$DESKTOP_FILE" "$DESKTOP_DEST"
chmod +x "$DESKTOP_DEST"
echo "✅ Created desktop icon: $DESKTOP_DEST"

# Update paths in service file
sed -i "s|/home/pi/leahPi|$SCRIPT_DIR|g" "$SERVICE_FILE"
sed -i "s|User=pi|User=$USER|g" "$SERVICE_FILE"
sed -i "s|Group=pi|Group=$(id -gn)|g" "$SERVICE_FILE"

# Copy service file (requires sudo)
echo ""
echo "📦 Setting up systemd service (requires sudo)..."
sudo cp "$SERVICE_FILE" "$SERVICE_DEST"
sudo chmod 644 "$SERVICE_DEST"
echo "✅ Service file installed: $SERVICE_DEST"

# Reload systemd
sudo systemctl daemon-reload
echo "✅ Systemd daemon reloaded"

# Ask if user wants to enable service
echo ""
read -p "Enable auto-start on boot? (y/n): " enable_service
if [ "$enable_service" = "y" ] || [ "$enable_service" = "Y" ]; then
    sudo systemctl enable leahpi.service
    echo "✅ Auto-start enabled"
    echo ""
    read -p "Start the service now? (y/n): " start_now
    if [ "$start_now" = "y" ] || [ "$start_now" = "Y" ]; then
        sudo systemctl start leahpi.service
        echo "✅ Service started"
        echo ""
        echo "Check status with: sudo systemctl status leahpi"
    fi
else
    echo "ℹ️  Service installed but not enabled. Enable later with:"
    echo "   sudo systemctl enable leahpi.service"
fi

echo ""
echo "✨ Setup complete!"
echo ""
echo "📋 Summary:"
echo "   Desktop icon: $DESKTOP_DEST"
echo "   Service file: $SERVICE_DEST"
echo ""
echo "🔧 Useful commands:"
echo "   Start service:    sudo systemctl start leahpi"
echo "   Stop service:    sudo systemctl stop leahpi"
echo "   Status:           sudo systemctl status leahpi"
echo "   View logs:        journalctl -u leahpi -f"
echo "   Enable auto-start: sudo systemctl enable leahpi"
echo "   Disable auto-start: sudo systemctl disable leahpi"
