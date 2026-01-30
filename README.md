# Raspberry Pi Interactive Learning App

An interactive learning application for Raspberry Pi touchscreen that teaches kids to write through tracing exercises. Supports English alphabet, numbers, Korean (Hangul), and Chinese characters.

## Features

- **Interactive Tracing**: Touch-based tracing with real-time visual feedback
- **Multiple Languages**: 
  - English alphabet (A-Z)
  - Numbers (0-9)
  - Korean Hangul characters
  - Chinese characters
- **Visual Feedback**: Color-coded feedback (green for correct, red for deviation)
- **Progress Tracking**: Completion percentage and success animations
- **Kid-Friendly UI**: Large buttons and colorful interface designed for children

## Requirements

### Hardware
- Raspberry Pi (any model with GPIO)
- Touchscreen LCD display (tested with common 800x480 and 1024x600 displays)
- MicroSD card (8GB+ recommended)

### Software
- Raspberry Pi OS (latest version recommended)
- Python 3.7 or higher
- Pygame 2.5.0 or higher
- NumPy 1.24.0 or higher

## Installation

### 1. Install Dependencies

**Option A: Quick Setup (Recommended)**
```bash
# Run the setup script
bash setup-pi.sh
```

**Option B: Manual Installation**

For newer Raspberry Pi OS (externally-managed Python environment):

```bash
# Update system packages
sudo apt update

# Install system Python packages (recommended)
sudo apt install -y python3-pygame python3-numpy python3-full
```

**Option C: Virtual Environment (if system packages don't work)**

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install packages
pip install pygame numpy

# To run the app later, activate venv first:
# source venv/bin/activate && python3 main.py
```

**Option D: Override (Not Recommended)**

If you must use pip directly:
```bash
pip3 install --break-system-packages -r requirements.txt
```

### 2. Configure Touchscreen

The app should work with most touchscreen displays. If your touchscreen isn't working:

1. Check if your display is detected:
   ```bash
   ls /dev/input/
   ```

2. For some displays, you may need to calibrate the touchscreen:
   ```bash
   sudo apt install xinput-calibrator
   xinput_calibrator
   ```

3. If using a specific touchscreen driver, you may need to configure it in `/boot/config.txt` (consult your display's documentation)

### 3. Configure Display Resolution

Edit `config.py` to match your LCD screen resolution:

```python
SCREEN_WIDTH = 800   # Change to your screen width
SCREEN_HEIGHT = 480  # Change to your screen height
FULLSCREEN = True    # Set to False for windowed mode (useful for testing)
```

Common resolutions:
- 800x480 (common for 7" displays)
- 1024x600 (common for 10" displays)
- 1280x800 (larger displays)

### 4. Test the Application

Before running on the Raspberry Pi, you can test in windowed mode on your development machine:

1. Edit `config.py` and set `FULLSCREEN = False`
2. Run the application:
   ```bash
   python3 main.py
   ```

## Usage

### Running on Raspberry Pi

1. Navigate to the project directory:
   ```bash
   cd LeahLearning
   ```

2. Run the application:
   ```bash
   python3 main.py
   ```

3. To run automatically on boot, add to `/etc/rc.local`:
   ```bash
   sudo nano /etc/rc.local
   ```
   
   Add before `exit 0`:
   ```bash
   cd /path/to/LeahLearning && python3 main.py &
   ```

### Using the Application

1. **Language Selection**: Tap on a language button (English, Numbers, Korean, or Chinese)
2. **Character Selection**: Tap on a character from the grid
3. **Tracing**: 
   - Follow the dotted guide lines with your finger
   - Green lines indicate you're on track
   - Red lines indicate you're deviating from the guide
   - Complete the tracing to see a success animation
4. **Navigation**:
   - **Back**: Return to menu
   - **Clear**: Erase your current drawing
   - **Next**: Move to next character (currently returns to menu)

## Configuration

Edit `config.py` to customize:

- **Display Settings**: Screen resolution, fullscreen mode
- **Colors**: Theme colors for UI elements
- **Touch Settings**: Sensitivity and deadzone
- **Tracing Settings**: Tolerance, completion threshold, line widths
- **UI Settings**: Button sizes, font sizes, character display size

## Project Structure

```
LeahLearning/
├── main.py                 # Entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── assets/
│   ├── fonts/            # Font files (optional)
│   └── sounds/           # Sound effects (optional)
└── src/
    ├── display_manager.py    # Screen initialization
    ├── touch_handler.py      # Touch input handling
    ├── tracing_engine.py     # Tracing logic and validation
    ├── ui/
    │   ├── menu_screen.py    # Main menu
    │   ├── tracing_screen.py # Tracing interface
    │   └── ui_components.py  # UI components
    └── languages/
        ├── english.py        # English alphabet data
        ├── numbers.py        # Numbers data
        ├── korean.py         # Korean characters
        └── chinese.py        # Chinese characters
```

## Troubleshooting

### Touchscreen Not Working
- Check if touchscreen is detected: `ls /dev/input/`
- Try running with `FULLSCREEN = False` first
- Check touchscreen calibration
- Some displays require specific drivers - consult your display documentation

### Display Issues
- Verify screen resolution in `config.py` matches your display
- Try different resolutions if the display isn't filling the screen
- Check `/boot/config.txt` for display configuration

### Performance Issues
- Close other applications to free up resources
- Reduce `CHARACTER_DISPLAY_SIZE` in `config.py` if rendering is slow
- Check Raspberry Pi temperature: `vcgencmd measure_temp`

### Application Won't Start
- Verify Python version: `python3 --version` (needs 3.7+)
- Check dependencies: `pip3 list | grep pygame`
- Run with error output: `python3 main.py 2>&1 | tee error.log`

## Development

### Adding New Characters

To add characters to a language module:

1. Edit the appropriate file in `src/languages/` (e.g., `english.py`)
2. Add character data in the `CHARACTERS` dictionary:
   ```python
   'NEW': {
       'strokes': [
           [(x1, y1), (x2, y2), ...],  # Stroke 1
           [(x3, y3), (x4, y4), ...],  # Stroke 2
       ],
       'name': 'NEW',
       'pronunciation': 'pronunciation guide'
   }
   ```
3. Coordinates are normalized (0-100 scale) and will be automatically scaled

### Testing

Test on your development machine first with `FULLSCREEN = False` in `config.py`, then test on the Raspberry Pi hardware.

## License

This project is provided as-is for educational purposes.

## Contributing

Feel free to add more characters, improve the tracing algorithm, or add new features!

## Support

For issues specific to:
- **Raspberry Pi hardware**: Consult Raspberry Pi documentation
- **Touchscreen displays**: Consult your display manufacturer's documentation
- **Application bugs**: Check the troubleshooting section above
