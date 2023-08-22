from PIL import Image, ImageDraw, ImageFont


def create_image(text, path, width=900, height=300, font_path="arial.ttf"):
    image = Image.new('1', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Change font size if needed
    font = ImageFont.truetype(font_path, size=100)

    # Center the text
    text_width, text_height = draw.textsize(text, font=font)
    position = ((width - text_width) / 2, (height - text_height) / 2)

    draw.text(position, text, fill="black", font=font)
    image.save(path + "\\" + "new_image.png")

