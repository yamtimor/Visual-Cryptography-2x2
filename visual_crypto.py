from PIL import Image
import random

def generate_shares(image_path):
    with Image.open(image_path) as original_image:
        width, height = original_image.size

        # Create two empty shares
        share1 = Image.new("1", (width, height))
        share2 = Image.new("1", (width, height))

        # Iterate through each pixel in the original image
        for x in range(width):
            for y in range(height):
                pixel = original_image.getpixel((x, y))
                pattern = random.choice([0, 1])
                if pixel == 0:  # Black pixel
                    share1.putpixel((x, y), pattern)
                    share2.putpixel((x, y), 1 - pattern)
                else:  # White pixel
                    share1.putpixel((x, y), pattern)
                    share2.putpixel((x, y), pattern)

    return share1, share2
