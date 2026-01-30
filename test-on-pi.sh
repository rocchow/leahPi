#!/bin/bash
# Quick test script to run on Raspberry Pi
# Usage: Copy this to Pi and run: bash test-on-pi.sh

echo "🧪 Testing Raspberry Pi Learning App"
echo "===================================="

# Check Python version
echo "📋 Checking Python version..."
python3 --version

# Check if dependencies are installed
echo ""
echo "📦 Checking dependencies..."
python3 -c "import pygame; print('✅ Pygame:', pygame.version.ver)" 2>/dev/null || echo "❌ Pygame not installed"
python3 -c "import numpy; print('✅ NumPy:', numpy.__version__)" 2>/dev/null || echo "❌ NumPy not installed"

# Check if config exists
echo ""
echo "⚙️  Checking configuration..."
if [ -f "config.py" ]; then
    echo "✅ config.py found"
    # Show current screen settings
    python3 -c "import config; print(f'   Screen: {config.SCREEN_WIDTH}x{config.SCREEN_HEIGHT}')"
    python3 -c "import config; print(f'   Fullscreen: {config.FULLSCREEN}')"
else
    echo "❌ config.py not found"
fi

# Check if main.py exists
echo ""
if [ -f "main.py" ]; then
    echo "✅ main.py found"
else
    echo "❌ main.py not found"
    exit 1
fi

# Test import
echo ""
echo "🔍 Testing imports..."
python3 -c "
import sys
sys.path.insert(0, '.')
try:
    from src.display_manager import DisplayManager
    from src.touch_handler import TouchHandler
    from src.ui.menu_screen import MenuScreen
    print('✅ All imports successful')
except Exception as e:
    print(f'❌ Import error: {e}')
    sys.exit(1)
"

# Ask if ready to run
echo ""
echo "🚀 Ready to test!"
echo ""
echo "Options:"
echo "1. Test in windowed mode (safe, can see errors)"
echo "2. Test in fullscreen mode (for actual LCD)"
echo "3. Exit"
echo ""
read -p "Choose option (1-3): " choice

case $choice in
    1)
        echo ""
        echo "🪟 Running in windowed mode..."
        # Temporarily set fullscreen to False
        python3 -c "
import config
config.FULLSCREEN = False
" 2>/dev/null || echo "# Set FULLSCREEN = False in config.py manually"
        python3 main.py
        ;;
    2)
        echo ""
        echo "🖥️  Running in fullscreen mode..."
        echo "⚠️  Press Ctrl+C to exit"
        python3 main.py
        ;;
    3)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac
