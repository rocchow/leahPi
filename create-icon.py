#!/usr/bin/env python3
"""
Create a simple icon for the desktop launcher
Generates a basic icon image if one doesn't exist
"""
import os
try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("PIL/Pillow not available. Creating simple icon with pygame...")
    import pygame

def create_icon_pygame():
    """Create icon using pygame"""
    pygame.init()
    
    # Create a 128x128 icon
    size = 128
    surface = pygame.Surface((size, size))
    
    # Background - light blue
    surface.fill((100, 149, 237))  # Cornflower blue
    
    # Draw a simple "L" for Leah
    font = pygame.font.Font(None, 96)
    text = font.render("L", True, (255, 255, 255))
    text_rect = text.get_rect(center=(size//2, size//2))
    surface.blit(text, text_rect)
    
    # Save as PNG
    icon_path = os.path.join(os.path.dirname(__file__), "assets", "icon.png")
    os.makedirs(os.path.dirname(icon_path), exist_ok=True)
    pygame.image.save(surface, icon_path)
    print(f"✅ Icon created: {icon_path}")
    
    pygame.quit()

def create_icon_pil():
    """Create icon using PIL/Pillow"""
    size = 128
    img = Image.new('RGB', (size, size), color=(100, 149, 237))
    draw = ImageDraw.Draw(img)
    
    # Draw "L" text
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
    except:
        font = ImageFont.load_default()
    
    text = "L"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size - text_width) // 2, (size - text_height) // 2)
    
    draw.text(position, text, fill=(255, 255, 255), font=font)
    
    icon_path = os.path.join(os.path.dirname(__file__), "assets", "icon.png")
    os.makedirs(os.path.dirname(icon_path), exist_ok=True)
    img.save(icon_path)
    print(f"✅ Icon created: {icon_path}")

if __name__ == "__main__":
    icon_path = os.path.join(os.path.dirname(__file__), "assets", "icon.png")
    
    # Check if icon already exists
    if os.path.exists(icon_path):
        print(f"ℹ️  Icon already exists: {icon_path}")
        print("   Delete it first if you want to regenerate.")
    else:
        if HAS_PIL:
            create_icon_pil()
        else:
            create_icon_pygame()
