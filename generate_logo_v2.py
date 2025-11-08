#!/usr/bin/env python3
"""
Dark Gothic T-Shirt Logo Generator V2
Creates a powerful, edgy "SHUT UP" logo with skull and flame elements
Using custom drawn text for better control
"""

from PIL import Image, ImageDraw, ImageFilter
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

def draw_block_letter(draw, letter, x, y, width, height, color=(240, 240, 240, 255)):
    """Draw bold block letters"""
    stroke_width = width * 0.15

    if letter == 'S':
        # Top curve
        draw.arc([x, y, x + width, y + height * 0.4], start=180, end=0, fill=color, width=int(stroke_width))
        # Bottom curve
        draw.arc([x, y + height * 0.6, x + width, y + height], start=0, end=180, fill=color, width=int(stroke_width))
        # Middle connection
        draw.line([x + width * 0.85, y + height * 0.3, x + width * 0.15, y + height * 0.7], fill=color, width=int(stroke_width))

    elif letter == 'H':
        # Left vertical
        draw.line([x + width * 0.15, y, x + width * 0.15, y + height], fill=color, width=int(stroke_width))
        # Right vertical
        draw.line([x + width * 0.85, y, x + width * 0.85, y + height], fill=color, width=int(stroke_width))
        # Horizontal bar
        draw.line([x + width * 0.15, y + height * 0.5, x + width * 0.85, y + height * 0.5], fill=color, width=int(stroke_width))

    elif letter == 'U':
        # Left vertical
        draw.line([x + width * 0.15, y, x + width * 0.15, y + height * 0.75], fill=color, width=int(stroke_width))
        # Right vertical
        draw.line([x + width * 0.85, y, x + width * 0.85, y + height * 0.75], fill=color, width=int(stroke_width))
        # Bottom curve
        draw.arc([x + width * 0.15, y + height * 0.5, x + width * 0.85, y + height], start=0, end=180, fill=color, width=int(stroke_width))

    elif letter == 'T':
        # Top horizontal
        draw.line([x, y + stroke_width * 0.5, x + width, y + stroke_width * 0.5], fill=color, width=int(stroke_width))
        # Vertical stem
        draw.line([x + width * 0.5, y, x + width * 0.5, y + height], fill=color, width=int(stroke_width))

    elif letter == 'P':
        # Left vertical
        draw.line([x + width * 0.15, y, x + width * 0.15, y + height], fill=color, width=int(stroke_width))
        # Top curve
        draw.arc([x + width * 0.15, y, x + width * 0.85, y + height * 0.5], start=270, end=90, fill=color, width=int(stroke_width))
        # Close the P
        draw.line([x + width * 0.15, y + height * 0.5, x + width * 0.5, y + height * 0.5], fill=color, width=int(stroke_width))

def draw_heavy_text(draw, text, x, y, letter_width, letter_height, spacing, color=(240, 240, 240, 255)):
    """Draw text using block letters"""
    current_x = x
    for letter in text:
        if letter == ' ':
            current_x += letter_width * 0.7
        else:
            draw_block_letter(draw, letter, current_x, y, letter_width, letter_height, color)
            current_x += letter_width + spacing

def add_distressed_texture(img):
    """Add grunge/distressed effect"""
    noise = Image.new('RGBA', img.size, (0, 0, 0, 0))
    noise_draw = ImageDraw.Draw(noise)

    import random
    random.seed(42)

    # Add random scratches and wear
    for _ in range(400):
        x1 = random.randint(0, WIDTH)
        y1 = random.randint(0, HEIGHT)
        x2 = x1 + random.randint(-150, 150)
        y2 = y1 + random.randint(-30, 30)
        alpha = random.randint(15, 50)
        noise_draw.line([x1, y1, x2, y2], fill=(0, 0, 0, alpha), width=random.randint(2, 6))

    # Add random spots for grunge
    for _ in range(800):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(3, 15)
        alpha = random.randint(25, 70)
        noise_draw.ellipse([x, y, x + size, y + size], fill=(0, 0, 0, alpha))

    # Add some larger distress marks
    for _ in range(100):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(10, 40)
        alpha = random.randint(30, 80)
        noise_draw.ellipse([x, y, x + size, y + size], fill=(0, 0, 0, alpha))

    return Image.alpha_composite(img, noise)

def main():
    print("🎨 Generating dark gothic 'SHUT UP' logo (V2)...")

    # Create base image with alpha channel
    img = Image.new('RGBA', (WIDTH, HEIGHT), BACKGROUND_COLOR + (255,))
    draw = ImageDraw.Draw(img)

    # Add subtle horizontal lines texture
    for i in range(0, HEIGHT, 40):
        alpha = 8
        draw.line([(0, i), (WIDTH, i)], fill=(255, 255, 255, alpha), width=1)

    # Draw flame elements in corners
    flame_positions = [
        (80, 350, 250, 500),   # Top left
        (2070, 350, 250, 500), # Top right
        (250, 750, 180, 450),  # Middle left
        (1970, 750, 180, 450), # Middle right
    ]

    print("🔥 Adding flame elements...")
    for fx, fy, fw, fh in flame_positions:
        draw_flame(draw, fx, fy, fw, fh, (255, 255, 255, 25))
        # Add secondary smaller flames
        draw_flame(draw, fx + fw * 0.2, fy + fh * 0.15, fw * 0.6, fh * 0.7, (255, 255, 255, 15))

    # Draw skulls in all four corners
    skull_positions = [
        (120, 150, 200),   # Top left
        (2080, 150, 200),  # Top right
        (70, 1250, 180),   # Bottom left
        (2150, 1250, 180), # Bottom right
    ]

    print("💀 Adding skull elements...")
    for sx, sy, s_size in skull_positions:
        create_skull(draw, sx, sy, s_size, opacity=70)

    # Text parameters
    letter_width = 280
    letter_height = 400
    spacing = 50

    # Calculate text positions for "SHUT" and "UP"
    shut_width = (letter_width + spacing) * 4
    up_width = (letter_width + spacing) * 2

    shut_x = (WIDTH - shut_width) // 2
    shut_y = HEIGHT // 2 - 280

    up_x = (WIDTH - up_width) // 2
    up_y = HEIGHT // 2 + 180

    print("✍️  Drawing main text...")

    # Create shadow layers for depth
    shadow_layers = [
        (15, 15, (20, 20, 20, 220)),
        (10, 10, (30, 30, 30, 180)),
        (5, 5, (40, 40, 40, 150)),
    ]

    for offset_x, offset_y, shadow_color in shadow_layers:
        draw_heavy_text(draw, "SHUT", shut_x + offset_x, shut_y + offset_y,
                       letter_width, letter_height, spacing, shadow_color)
        draw_heavy_text(draw, "UP", up_x + offset_x, up_y + offset_y,
                       letter_width, letter_height, spacing, shadow_color)

    # Red glow effect
    print("✨ Adding red glow effect...")
    glow_offsets = [(0, 0), (3, 3), (-3, -3), (3, -3), (-3, 3), (6, 0), (-6, 0), (0, 6), (0, -6)]
    for offset_x, offset_y in glow_offsets:
        draw_heavy_text(draw, "SHUT", shut_x + offset_x, shut_y + offset_y,
                       letter_width, letter_height, spacing, (200, 0, 0, 80))
        draw_heavy_text(draw, "UP", up_x + offset_x, up_y + offset_y,
                       letter_width, letter_height, spacing, (200, 0, 0, 80))

    # Main white text
    draw_heavy_text(draw, "SHUT", shut_x, shut_y, letter_width, letter_height, spacing)
    draw_heavy_text(draw, "UP", up_x, up_y, letter_width, letter_height, spacing)

    # Add cracks and distress to text area
    print("⚡ Adding distress effects...")
    import random
    random.seed(123)

    # Cracks across the text
    for _ in range(80):
        crack_x = WIDTH // 2 + random.randint(-800, 800)
        crack_y = HEIGHT // 2 + random.randint(-400, 400)
        crack_length = random.randint(30, 120)
        angle = random.uniform(0, math.pi * 2)
        end_x = crack_x + crack_length * math.cos(angle)
        end_y = crack_y + crack_length * math.sin(angle)
        draw.line([crack_x, crack_y, end_x, end_y],
                 fill=(0, 0, 0, random.randint(100, 180)), width=random.randint(3, 7))

    # Add decorative border
    print("🖼️  Adding border...")
    border_thickness = 35
    draw.rectangle([35, 35, WIDTH - 35, HEIGHT - 35],
                  outline=(255, 255, 255, 100), width=border_thickness)
    draw.rectangle([60, 60, WIDTH - 60, HEIGHT - 60],
                  outline=(255, 255, 255, 50), width=12)
    draw.rectangle([85, 85, WIDTH - 85, HEIGHT - 85],
                  outline=(255, 255, 255, 30), width=6)

    # Apply heavy grunge texture
    print("🎨 Applying heavy grunge texture...")
    img = add_distressed_texture(img)

    # Save high-resolution logo
    output_file = 'shut_up_logo.png'
    img.save(output_file, 'PNG', quality=95)
    print(f"\n✅ SUCCESS! Logo saved as: {output_file}")
    print(f"   Resolution: {WIDTH}x{HEIGHT}px")
    print(f"   Style: Dark Gothic / Grunge / Edgy")
    print(f"   Elements: Skulls, Flames, Distressed texture")

    # Create a smaller preview version
    preview_size = (1200, 800)
    preview = img.resize(preview_size, Image.Resampling.LANCZOS)
    preview_file = 'shut_up_logo_preview.png'
    preview.save(preview_file, 'PNG', quality=90)
    print(f"✅ Preview saved as: {preview_file}")
    print(f"   Resolution: {preview_size[0]}x{preview_size[1]}px\n")

    print("🎉 Your powerful, intimidating t-shirt logo is ready!")
    print("   Perfect for dark, edgy apparel designs!")

if __name__ == "__main__":
    main()
