from visual_crypto import generate_shares
from test_visual_cryptography import test_visual_cryptography
from create_image import create_image

def main(image_path):

    # Create Image
    create_image(r"images/Yam Timor Trio")
    # Generate the shares using the imported function
    share1, share2 = generate_shares(image_path)

    # Save or display the shares if needed
    share1.save("share1.png")
    share2.save("share2.png")

    # Test the visual cryptography using the imported function
    test_visual_cryptography(image_path)

if __name__ == "__main__":
    # Path to the image you want to encrypt
    image_path = "images/image/Yam Timor Trio.png"
    main(image_path)