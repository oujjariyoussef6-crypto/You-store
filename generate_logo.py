#!/usr/bin/env python3
"""
Dark Gothic T-Shirt Logo Generator
Creates a powerful, edgy "SHUT UP" logo with skull and flame elements
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

# Canvas settings
WIDTH = 2400
HEIGHT = 1600
BACKGROUND_COLOR = (0, 0, 0)

def create_skull(draw, x, y, size, opacity=180):
    """Draw a stylized skull"""
    color = (255, 255, 255, opacity)

    # Skull main shape
    draw.ellipse([x, y, x + size, y + size * 0.9], fill=color)

    # Eye sockets (dark)
    eye_size = size * 0.15
    eye_y = y + size * 0.3
    draw.ellipse([x + size * 0.25, eye_y, x + size * 0.25 + eye_size, eye_y + eye_size * 1.2], fill=(0, 0, 0))
    draw.ellipse([x + size * 0.6, eye_y, x + size * 0.6 + eye_size, eye_y + eye_size * 1.2], fill=(0, 0, 0))

    # Nose triangle
    nose_y = y + size * 0.55
    nose_points = [
        (x + size * 0.5, nose_y),
        (x + size * 0.4, nose_y + size * 0.15),
        (x + size * 0.6, nose_y + size * 0.15)
    ]
    draw.polygon(nose_points, fill=(0, 0, 0))

    # Teeth/jaw
    jaw_y = y + size * 0.7
    for i in range(5):
        tooth_x = x + size * 0.25 + (i * size * 0.13)
        draw.rectangle([tooth_x, jaw_y, tooth_x + size * 0.08, jaw_y + size * 0.15], fill=(0, 0, 0))

def draw_flame(draw, x, y, width, height, color=(255, 255, 255, 100)):
    """Draw a stylized flame shape"""
    points = [
        (x + width * 0.5, y),  # Top point
        (x + width * 0.7, y + height * 0.3),
        (x + width * 0.9, y + height * 0.5),
        (x + width * 0.8, y + height * 0.7),
        (x + width, y + height),  # Right bottom
        (x + width * 0.5, y + height * 0.85),
        (x, y + height),  # Left bottom
        (x + width * 0.2, y + height * 0.7),
        (x + width * 0.1, y + height * 0.5),
        (x + width * 0.3, y + height * 0.3),
    ]
    draw.polygon(points, fill=color)

def add_distressed_texture(img):
    """Add grunge/distressed effect"""
    # Create noise layer
    noise = Image.new('RGBA', img.size, (0, 0, 0, 0))
    noise_draw = ImageDraw.Draw(noise)

    import random
    random.seed(42)

    # Add random scratches and wear
    for _ in range(300):
        x1 = random.randint(0, WIDTH)
        y1 = random.randint(0, HEIGHT)
        x2 = x1 + random.randint(-100, 100)
        y2 = y1 + random.randint(-20, 20)
        alpha = random.randint(10, 40)
        noise_draw.line([x1, y1, x2, y2], fill=(0, 0, 0, alpha), width=random.randint(1, 4))

    # Add random spots
    for _ in range(500):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(2, 10)
        alpha = random.randint(20, 60)
        noise_draw.ellipse([x, y, x + size, y + size], fill=(0, 0, 0, alpha))

    return Image.alpha_composite(img, noise)

def main():
    print("🎨 Generating dark gothic 'SHUT UP' logo...")

    # Create base image with alpha channel
    img = Image.new('RGBA', (WIDTH, HEIGHT), BACKGROUND_COLOR + (255,))
    draw = ImageDraw.Draw(img)

    # Add subtle texture background
    for i in range(0, HEIGHT, 50):
        alpha = 10
        draw.line([(0, i), (WIDTH, i)], fill=(255, 255, 255, alpha), width=1)

    # Draw flame elements in background (left and right)
    flame_positions = [
        (100, 400, 200, 400),
        (2100, 400, 200, 400),
        (300, 800, 150, 350),
        (1950, 800, 150, 350),
    ]

    for fx, fy, fw, fh in flame_positions:
        draw_flame(draw, fx, fy, fw, fh, (255, 255, 255, 30))

    # Draw skulls in background
    skull_positions = [
        (150, 200, 180),
        (2050, 200, 180),
        (80, 1100, 150),
        (2150, 1100, 150),
    ]

    for sx, sy, s_size in skull_positions:
        create_skull(draw, sx, sy, s_size, opacity=60)

    # Main text layer
    text = "SHUT UP"

    # Try to use a bold system font, fallback to default
    try:
        # Try multiple font paths
        font_size = 380
        font_paths = [
            "/usr/share/fonts/liberation/LiberationSans-Bold.ttf",
            "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/google-roboto/Roboto-Bold.ttf",
        ]

        font = None
        for font_path in font_paths:
            try:
                font = ImageFont.truetype(font_path, font_size)
                print(f"✓ Using font: {font_path}")
                break
            except:
                continue

        if font is None:
            font = ImageFont.load_default()
            print("⚠ Using default font")
    except Exception as e:
        font = ImageFont.load_default()
        print(f"⚠ Font loading issue: {e}")

    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center position
    text_x = (WIDTH - text_width) // 2
    text_y = (HEIGHT - text_height) // 2

    # Create text shadow/outline effect (multiple layers)
    shadow_offsets = [
        (8, 8), (-8, -8), (8, -8), (-8, 8),
        (12, 12), (-12, -12), (12, -12), (-12, 12),
        (4, 4), (-4, -4), (4, -4), (-4, 4),
    ]

    # Dark shadow
    for offset_x, offset_y in shadow_offsets:
        draw.text((text_x + offset_x, text_y + offset_y), text,
                 font=font, fill=(40, 40, 40, 200))

    # Red glow effect (slightly behind)
    glow_offsets = [(0, 0), (2, 2), (-2, -2), (2, -2), (-2, 2)]
    for offset_x, offset_y in glow_offsets:
        draw.text((text_x + offset_x, text_y + offset_y), text,
                 font=font, fill=(180, 0, 0, 100))

    # Main text (white with slight gray)
    draw.text((text_x, text_y), text, font=font, fill=(240, 240, 240, 255))

    # Add cracks/distress over text
    import random
    random.seed(123)
    for _ in range(50):
        crack_x = text_x + random.randint(0, text_width)
        crack_y = text_y + random.randint(0, text_height)
        crack_length = random.randint(20, 80)
        angle = random.uniform(0, math.pi * 2)
        end_x = crack_x + crack_length * math.cos(angle)
        end_y = crack_y + crack_length * math.sin(angle)
        draw.line([crack_x, crack_y, end_x, end_y],
                 fill=(0, 0, 0, random.randint(80, 150)), width=random.randint(2, 5))

    # Add border decorative elements
    border_thickness = 30
    draw.rectangle([40, 40, WIDTH - 40, HEIGHT - 40], outline=(255, 255, 255, 80), width=border_thickness)
    draw.rectangle([70, 70, WIDTH - 70, HEIGHT - 70], outline=(255, 255, 255, 40), width=10)

    # Apply grunge texture
    print("🎨 Applying distressed texture...")
    img = add_distressed_texture(img)

    # Save high-resolution logo
    output_file = 'shut_up_logo.png'
    img.save(output_file, 'PNG', quality=95)
    print(f"✓ Logo saved as: {output_file}")
    print(f"  Resolution: {WIDTH}x{HEIGHT}px")
    print(f"  Style: Dark Gothic / Grunge")

    # Create a smaller preview version
    preview_size = (1200, 800)
    preview = img.resize(preview_size, Image.Resampling.LANCZOS)
    preview_file = 'shut_up_logo_preview.png'
    preview.save(preview_file, 'PNG', quality=90)
    print(f"✓ Preview saved as: {preview_file}")
    print(f"  Resolution: {preview_size[0]}x{preview_size[1]}px")

if __name__ == "__main__":
    main()
