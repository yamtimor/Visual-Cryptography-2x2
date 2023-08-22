from PIL import ImageChops


def overlay_shares(share1, share2):
    return ImageChops.multiply(share1, share2)


def test_visual_cryptography(image_path):
    share1, share2 = generate_shares(image_path)
    overlaid_shares = overlay_shares(share1, share2)

    original_image = Image.open(image_path).convert("1")

    # Compare the overlaid shares with the original image
    difference = ImageChops.difference(original_image, overlaid_shares)
    if not difference.getbbox():
        print("Test passed: The shares correctly recreate the original image.")
    else:
        print("Test failed: The shares do not recreate the original image.")


# Test the code with your image path
test_visual_cryptography('path/to/your/image.png')
