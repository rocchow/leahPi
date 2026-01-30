# Quick Deployment Guide

## Fastest Methods to Deploy Updates to Raspberry Pi

### Method 1: Direct rsync (Fastest - No GitHub needed) ⚡

**One command:**
```bash
./deploy-direct.sh
```

**Or with custom IP/username:**
```bash
./deploy-direct.sh 192.168.1.100 pi
```

**Manual rsync:**
```bash
rsync -avz --progress \
  --exclude '.git' \
  --exclude '__pycache__' \
  --exclude '*.pyc' \
  ./ pi@raspberrypi.local:~/leahPi/
```

**Pros:**
- ⚡ Fastest method
- No internet required
- Direct file transfer
- Only syncs changed files

**Cons:**
- Requires SSH access
- No version control on Pi

---

### Method 2: Git Pull (Recommended for version control) 📦

**Using the deployment script:**
```bash
./deploy.sh
```

**Or manually:**
```bash
# On your Mac (push to GitHub)
git add .
git commit -m "Update"
git push

# On Raspberry Pi (SSH in and pull)
ssh pi@raspberrypi.local
cd ~/leahPi
git pull
```

**Pros:**
- Version control
- Can rollback changes
- Works from anywhere

**Cons:**
- Requires internet connection
- Slightly slower

---

### Method 3: Quick SSH + Git Pull (One-liner) 🎯

**From your Mac:**
```bash
ssh pi@raspberrypi.local "cd ~/leahPi && git pull"
```

**After pushing to GitHub:**
```bash
git push && ssh pi@raspberrypi.local "cd ~/leahPi && git pull"
```

---

### Method 4: SCP (Simple file copy) 📋

**Copy entire project:**
```bash
scp -r ./ pi@raspberrypi.local:~/leahPi/
```

**Copy specific file:**
```bash
scp src/tracing_engine.py pi@raspberrypi.local:~/leahPi/src/
```

---

## Setup SSH Keys (Skip password prompts)

**On your Mac:**
```bash
# Generate SSH key if you don't have one
ssh-keygen -t ed25519

# Copy key to Pi
ssh-copy-id pi@raspberrypi.local
```

Now you can SSH without entering password every time!

---

## Find Your Pi's IP Address

**On Raspberry Pi:**
```bash
hostname -I
```

**Or scan your network:**
```bash
# On Mac
arp -a | grep raspberrypi
```

**Or use mDNS (if enabled):**
```bash
ping raspberrypi.local
```

---

## Quick Commands Reference

```bash
# Deploy via rsync (fastest)
./deploy-direct.sh

# Deploy via git (with version control)
./deploy.sh

# SSH into Pi
ssh pi@raspberrypi.local

# Restart app on Pi (if running as service)
ssh pi@raspberrypi.local "sudo systemctl restart leahpi"

# View app logs
ssh pi@raspberrypi.local "journalctl -u leahpi -f"
```

---

## Recommended Workflow

1. **Development**: Make changes locally
2. **Test**: Run locally with `FULLSCREEN = False` in config.py
3. **Deploy**: Use `./deploy-direct.sh` for quick updates
4. **Commit**: When stable, commit and push to GitHub
5. **Pi Update**: SSH and git pull for version-controlled updates

---

## Troubleshooting

**Can't connect via SSH:**
```bash
# Enable SSH on Pi (if not enabled)
sudo systemctl enable ssh
sudo systemctl start ssh
```

**Permission denied:**
```bash
# Check SSH key is copied
ssh-copy-id pi@raspberrypi.local
```

**Can't find Pi:**
```bash
# Use IP address instead of hostname
./deploy-direct.sh 192.168.1.100
```
