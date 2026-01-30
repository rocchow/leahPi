#!/bin/bash
# Launcher script for Leah Learning App
# This script handles both virtual environment and system Python

cd "$(dirname "$0")"

# Check if virtual environment exists and use it
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the app
python3 main.py

# If app exits, keep terminal open to see errors (optional)
# read -p "Press Enter to close..."
