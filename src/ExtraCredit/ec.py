from PIL import Image, ImageDraw

def Crown():
    # Create a new image with a white background
    image = Image.new('RGB', (500, 500), (255, 255, 255))

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw the crown shape
    crown_points = [
        (150, 100),
        (200, 50),
        (250, 100),
        (280, 100),
        (280, 120),
        (290, 120),
        (290, 150),
        (260, 180),
        (250, 250),
        (225, 275),
        (200, 290),
        (175, 275),
        (150, 250),
        (140, 180),
        (110, 150),
        (110, 120),
        (120, 120),
        (120, 100),
        (150, 100)
    ]

    draw.polygon(crown_points, fill=(255, 215, 0), outline=(0, 0, 0))

    # Save the image
    image.save('crown.png')
