# Testing Guide for Raspberry Pi

## Quick Start Testing

### Step 1: SSH into Your Pi

```bash
ssh pi@raspberrypi.local
# Or use IP: ssh pi@192.168.1.100
```

### Step 2: Navigate to Project Directory

```bash
cd ~/leahPi
# Or wherever you cloned/deployed the project
```

### Step 3: Install Dependencies (First Time Only)

**Quick Setup:**
```bash
bash setup-pi.sh
```

**Manual Setup:**

For newer Raspberry Pi OS (externally-managed environment):

```bash
# Update system
sudo apt update

# Install system packages (recommended)
sudo apt install -y python3-pygame python3-numpy python3-full
```

**Alternative: Virtual Environment**

If system packages aren't available:
```bash
python3 -m venv venv
source venv/bin/activate
pip install pygame numpy
# Remember to activate venv before running: source venv/bin/activate
```

### Step 4: Configure for Testing

**For safe testing (windowed mode):**

Edit `config.py`:
```bash
nano config.py
```

Change:
```python
FULLSCREEN = False  # Set to False for testing
SCREEN_WIDTH = 800   # Match your display
SCREEN_HEIGHT = 480  # Match your display
```

**Or use the test script:**
```bash
bash test-on-pi.sh
```

### Step 5: Run the Application

**Option A: Windowed Mode (Safe for Testing)**
```bash
python3 main.py
```

**Option B: Fullscreen Mode (For LCD Display)**
```bash
# Make sure FULLSCREEN = True in config.py
python3 main.py
```

**Option C: Run in Background**
```bash
# Run in background
nohup python3 main.py > app.log 2>&1 &

# View logs
tail -f app.log

# Stop the app
pkill -f "python3 main.py"
```

---

## Testing Checklist

### ✅ Basic Functionality

1. **App Starts**
   ```bash
   python3 main.py
   ```
   - Should see menu screen
   - No error messages

2. **Language Selection**
   - Tap "English" button
   - Should show alphabet grid
   - Repeat for Numbers, Korean, Chinese

3. **Character Selection**
   - Tap any character (e.g., "A")
   - Should show tracing screen

4. **Touch Input**
   - Draw on screen with finger
   - Should see drawing appear
   - Guide lines should be visible

5. **Tracing Feedback**
   - Draw close to guide lines → green
   - Draw away from guide → red
   - Progress bar should update

6. **Navigation**
   - Tap "Back" → returns to menu
   - Tap "Clear" → erases drawing
   - Complete tracing → shows "Great Job!"

---

## Troubleshooting

### Problem: "No module named 'pygame'"

**Solution:**
```bash
sudo apt install python3-pygame -y
# Or
pip3 install pygame
```

### Problem: "No module named 'numpy'"

**Solution:**
```bash
sudo apt install python3-numpy -y
# Or
pip3 install numpy
```

### Problem: Touchscreen Not Working

**Check touchscreen:**
```bash
# List input devices
ls /dev/input/

# Test touchscreen
cat /dev/input/event0  # Replace event0 with your touchscreen device
# Move finger on screen, should see output
```

**Calibrate if needed:**
```bash
sudo apt install xinput-calibrator
xinput_calibrator
```

**Check display config:**
```bash
# Check if display is detected
tvservice -s

# Check resolution
fbset
```

### Problem: Screen Resolution Wrong

**Edit config.py:**
```python
# Common resolutions:
SCREEN_WIDTH = 800   # 7" displays
SCREEN_HEIGHT = 480

# Or
SCREEN_WIDTH = 1024   # 10" displays
SCREEN_HEIGHT = 600

# Or
SCREEN_WIDTH = 1280   # Larger displays
SCREEN_HEIGHT = 800
```

**Find your resolution:**
```bash
# On Pi
fbset -s

# Or check /boot/config.txt
cat /boot/config.txt | grep hdmi
```

### Problem: App Crashes on Start

**Run with error output:**
```bash
python3 main.py 2>&1 | tee error.log
```

**Check common issues:**
- Wrong screen resolution in config.py
- Touchscreen not detected
- Missing dependencies

### Problem: Performance Issues

**Check Pi resources:**
```bash
# CPU temperature
vcgencmd measure_temp

# Memory usage
free -h

# CPU usage
top
```

**Optimize:**
- Close other applications
- Reduce CHARACTER_DISPLAY_SIZE in config.py
- Check if running in fullscreen (better performance)

---

## Testing Different Scenarios

### Test 1: English Alphabet
1. Select "English"
2. Tap "A"
3. Trace the letter
4. Verify completion animation

### Test 2: Numbers
1. Select "Numbers"
2. Tap "5"
3. Trace the number
4. Check accuracy feedback

### Test 3: Korean
1. Select "Korean"
2. Tap "가"
3. Trace the character
4. Verify stroke order

### Test 4: Chinese
1. Select "Chinese"
2. Tap "一"
3. Trace the character
4. Check visual feedback

---

## Performance Testing

### Frame Rate Check

Add this to main.py temporarily:
```python
import pygame
clock = pygame.time.Clock()
while running:
    # ... your code ...
    fps = clock.get_fps()
    print(f"FPS: {fps}")
    clock.tick(60)
```

Target: 30+ FPS for smooth experience

### Memory Usage

```bash
# Monitor memory while app runs
watch -n 1 free -h
```

### CPU Temperature

```bash
# Check temperature
vcgencmd measure_temp

# If too hot (>80°C), add cooling or reduce load
```

---

## Quick Test Commands

```bash
# Test imports only
python3 -c "from src.display_manager import DisplayManager; print('OK')"

# Test config
python3 -c "import config; print(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)"

# Run with verbose output
python3 -u main.py 2>&1 | tee test.log

# Check if app is running
ps aux | grep python3

# Kill app if stuck
pkill -f "python3 main.py"
```

---

## Running on Boot (After Testing)

Once everything works, you can set it to run automatically:

**Create systemd service:**
```bash
sudo nano /etc/systemd/system/leahpi.service
```

Add:
```ini
[Unit]
Description=Leah Learning App
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/leahPi
ExecStart=/usr/bin/python3 /home/pi/leahPi/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Enable and start:**
```bash
sudo systemctl enable leahpi
sudo systemctl start leahpi

# Check status
sudo systemctl status leahpi

# View logs
journalctl -u leahpi -f
```

---

## Need Help?

Check logs:
```bash
# Application errors
cat error.log

# System logs
journalctl -u leahpi -n 50
```

Test individual components:
```bash
# Test display
python3 -c "from src.display_manager import DisplayManager; dm = DisplayManager(); dm.initialize(); print('Display OK')"

# Test touch
python3 -c "from src.touch_handler import TouchHandler; print('Touch handler OK')"
```
