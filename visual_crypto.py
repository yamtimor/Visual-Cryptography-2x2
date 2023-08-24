from PIL import Image
import random

def generate_shares(image_path, block_size=10):
    original_image = Image.open(image_path)
    original_image = original_image.convert('1')  # Convert to binary image
    original_width, original_height = original_image.size

    # Resize the original image down to create larger pixels
    small_image = original_image.resize(
        (original_width // block_size, original_height // block_size), Image.NEAREST
    )

    # Create two empty shares at the reduced size
    small_share1 = Image.new("1", (original_width // block_size, original_height // block_size))
    small_share2 = Image.new("1", (original_width // block_size, original_height // block_size))

    # Iterate through each pixel in the small image
    for x in range(original_width // block_size):
        for y in range(original_height // block_size):
            pixel = small_image.getpixel((x, y))
            pattern = random.choice([0, 1])

            if pixel == 0:  # Black pixel
                small_share1.putpixel((x, y), pattern)
                small_share2.putpixel((x, y), 1 - pattern)
            else:  # White pixel
                small_share1.putpixel((x, y), pattern)
                small_share2.putpixel((x, y), pattern)

    # Resize the small shares back up to create larger pixels
    share1 = small_share1.resize((original_width, original_height), Image.NEAREST)
    share2 = small_share2.resize((original_width, original_height), Image.NEAREST)

    return share1, share2
