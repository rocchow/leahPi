#!/bin/bash
# Setup script for Raspberry Pi
# Handles externally-managed Python environment

echo "🔧 Setting up Raspberry Pi Learning App"
echo "========================================"

# Update system
echo "📦 Updating system packages..."
sudo apt update

# Install system Python packages
echo ""
echo "📥 Installing system packages..."
sudo apt install -y python3-pygame python3-numpy python3-full

# Check if packages are installed
echo ""
echo "✅ Checking installed packages..."
python3 -c "import pygame; print('Pygame:', pygame.version.ver)" 2>/dev/null && echo "✅ Pygame installed" || echo "❌ Pygame missing"
python3 -c "import numpy; print('NumPy:', numpy.__version__)" 2>/dev/null && echo "✅ NumPy installed" || echo "❌ NumPy missing"

# Alternative: Create virtual environment if system packages don't work
if ! python3 -c "import pygame" 2>/dev/null; then
    echo ""
    echo "⚠️  System packages not available, creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install pygame numpy
    echo ""
    echo "✅ Virtual environment created!"
    echo "📝 To run the app, use: source venv/bin/activate && python3 main.py"
else
    echo ""
    echo "✅ All packages installed successfully!"
    echo "🚀 Ready to run: python3 main.py"
fi

echo ""
echo "✨ Setup complete!"
