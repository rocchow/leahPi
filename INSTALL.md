# Installation Guide for Raspberry Pi

## Quick Setup

Run the setup script:
```bash
bash setup-pi.sh
```

This will automatically handle the installation for you.

---

## Manual Installation

### For Raspberry Pi OS (Newer Versions - Externally Managed Python)

Raspberry Pi OS now uses an externally-managed Python environment. Use system packages instead of pip:

```bash
# Update system
sudo apt update

# Install system Python packages
sudo apt install -y python3-pygame python3-numpy python3-full
```

**Verify installation:**
```bash
python3 -c "import pygame; print('Pygame OK')"
python3 -c "import numpy; print('NumPy OK')"
```

---

## Alternative: Virtual Environment

If system packages don't work or you prefer isolation:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install packages
pip install pygame numpy

# Verify
python3 -c "import pygame; print('OK')"
```

**To run the app:**
```bash
source venv/bin/activate
python3 main.py
```

**Or create a wrapper script:**
```bash
#!/bin/bash
cd ~/leahPi
source venv/bin/activate
python3 main.py
```

---

## Troubleshooting

### Error: "externally-managed-environment"

**Solution:** Use system packages instead:
```bash
sudo apt install python3-pygame python3-numpy -y
```

### Error: "python3-pygame not found"

**Solution:** Update package list:
```bash
sudo apt update
sudo apt install python3-pygame python3-numpy -y
```

### Error: "No module named 'pygame'"

**Check if installed:**
```bash
python3 -c "import pygame"
```

**If not installed, try:**
```bash
# System package
sudo apt install python3-pygame -y

# Or virtual environment
python3 -m venv venv
source venv/bin/activate
pip install pygame
```

### Error: "python3-full not found"

**Solution:** This package might not be available on all Pi OS versions. Skip it and install:
```bash
sudo apt install python3-pygame python3-numpy -y
```

---

## Verification

After installation, test:

```bash
# Test imports
python3 -c "from src.display_manager import DisplayManager; print('✅ All OK')"

# Test config
python3 -c "import config; print(f'Screen: {config.SCREEN_WIDTH}x{config.SCREEN_HEIGHT}')"

# Run app
python3 main.py
```

---

## System Requirements

- Raspberry Pi OS (latest recommended)
- Python 3.7+
- 100MB+ free disk space
- Touchscreen LCD display

---

## Next Steps

After installation:
1. Configure `config.py` with your screen resolution
2. Test the app: `python3 main.py`
3. See `TESTING.md` for testing guide
