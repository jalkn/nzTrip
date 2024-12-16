from PIL import Image

image_path = './img/3.png'

def flip_image_left_right(image_path):
    try:
        img = Image.open(image_path)
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        return flipped_img
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None

flipped_image = flip_image_left_right(image_path)

if flipped_image:
    # Option 1: Save the flipped image
    flipped_image.save('./img/3.png')