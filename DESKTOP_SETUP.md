# Desktop Icon and Auto-Start Setup

## Quick Setup

Run the automated setup script:
```bash
cd ~/leahPi
bash setup-desktop.sh
```

This will:
- ✅ Create a desktop icon
- ✅ Set up systemd service for auto-start
- ✅ Optionally enable auto-start on boot

---

## Manual Setup

### 1. Create Desktop Icon

**Step 1: Create icon image (optional)**
```bash
python3 create-icon.py
```

**Step 2: Copy desktop file**
```bash
cp leahpi.desktop ~/Desktop/
chmod +x ~/Desktop/leahpi.desktop
```

**Step 3: Make run script executable**
```bash
chmod +x run-app.sh
```

**Step 4: Update paths in desktop file** (if needed)
Edit `~/Desktop/leahpi.desktop` and update paths:
```ini
Exec=/home/pi/leahPi/run-app.sh
Icon=/home/pi/leahPi/assets/icon.png
```

**Step 5: Double-click the icon on desktop to test**

---

### 2. Set Up Auto-Start Service

**Step 1: Copy service file**
```bash
sudo cp leahpi.service /etc/systemd/system/
sudo chmod 644 /etc/systemd/system/leahpi.service
```

**Step 2: Update paths in service file** (if needed)
```bash
sudo nano /etc/systemd/system/leahpi.service
```

Make sure paths match your installation:
```ini
WorkingDirectory=/home/pi/leahPi
ExecStart=/usr/bin/python3 /home/pi/leahPi/main.py
```

**Step 3: Reload systemd**
```bash
sudo systemctl daemon-reload
```

**Step 4: Enable auto-start**
```bash
sudo systemctl enable leahpi.service
```

**Step 5: Start the service (optional)**
```bash
sudo systemctl start leahpi.service
```

---

## Service Management Commands

### Start/Stop Service
```bash
# Start service
sudo systemctl start leahpi

# Stop service
sudo systemctl stop leahpi

# Restart service
sudo systemctl restart leahpi
```

### Check Status
```bash
# View status
sudo systemctl status leahpi

# View logs (live)
journalctl -u leahpi -f

# View last 50 log entries
journalctl -u leahpi -n 50
```

### Enable/Disable Auto-Start
```bash
# Enable auto-start on boot
sudo systemctl enable leahpi

# Disable auto-start
sudo systemctl disable leahpi
```

---

## Troubleshooting

### Desktop Icon Doesn't Work

**Check file permissions:**
```bash
chmod +x ~/Desktop/leahpi.desktop
chmod +x ~/leahPi/run-app.sh
```

**Check paths in desktop file:**
```bash
cat ~/Desktop/leahpi.desktop
```

**Test run script directly:**
```bash
cd ~/leahPi
./run-app.sh
```

### Service Won't Start

**Check service status:**
```bash
sudo systemctl status leahpi
```

**Check logs:**
```bash
journalctl -u leahpi -n 50
```

**Common issues:**
- Wrong paths in service file
- Python not found at `/usr/bin/python3`
- Working directory doesn't exist
- Display not available (for GUI apps)

**Fix display issue:**
Edit service file and ensure:
```ini
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/pi/.Xauthority
```

### Service Starts But App Doesn't Show

**Check if running:**
```bash
ps aux | grep python3
```

**Check display:**
```bash
echo $DISPLAY
```

**Try running manually:**
```bash
cd ~/leahPi
DISPLAY=:0 python3 main.py
```

### App Crashes on Startup

**View detailed logs:**
```bash
journalctl -u leahpi -f
```

**Common causes:**
- Missing dependencies
- Wrong screen resolution in config.py
- Touchscreen not detected
- Virtual environment not activated (if using venv)

**Fix virtual environment issue:**
Edit `run-app.sh` or service file to activate venv:
```bash
source ~/leahPi/venv/bin/activate
python3 main.py
```

---

## Using Virtual Environment

If you're using a virtual environment, update the service file:

```bash
sudo nano /etc/systemd/system/leahpi.service
```

Change ExecStart to:
```ini
ExecStart=/bin/bash -c 'cd /home/pi/leahPi && source venv/bin/activate && python3 main.py'
```

Or update `run-app.sh` to handle venv (already done).

---

## Customization

### Change Icon

Replace `assets/icon.png` with your own 128x128 PNG image, or:
```bash
python3 create-icon.py
```

### Change Service User

If running as different user, edit service file:
```bash
sudo nano /etc/systemd/system/leahpi.service
```

Change:
```ini
User=yourusername
Group=yourgroup
```

### Delay Service Start

If app needs to wait for display, add delay:
```ini
[Service]
ExecStartPre=/bin/sleep 5
```

---

## Testing

**Test desktop icon:**
1. Double-click icon on desktop
2. App should launch

**Test service:**
```bash
# Start service
sudo systemctl start leahpi

# Check it's running
sudo systemctl status leahpi

# View output
journalctl -u leahpi -f
```

**Test auto-start:**
```bash
# Enable service
sudo systemctl enable leahpi

# Reboot Pi
sudo reboot

# After reboot, check if app started
sudo systemctl status leahpi
```

---

## Uninstall

**Remove desktop icon:**
```bash
rm ~/Desktop/leahpi.desktop
```

**Remove service:**
```bash
sudo systemctl stop leahpi
sudo systemctl disable leahpi
sudo rm /etc/systemd/system/leahpi.service
sudo systemctl daemon-reload
```
