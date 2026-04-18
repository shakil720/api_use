from PIL import Image
from slugify import slugify
import os

def resize_image(input_path, output_width):
    img = Image.open(input_path)

    # Maintain aspect ratio
    w_percent = output_width / float(img.width)
    output_height = int(float(img.height) * w_percent)

    resized_img = img.resize((output_width, output_height), Image.LANCZOS)
    return resized_img

def main():
    input_path = input("Enter the image file path: ").strip()

    if not os.path.exists(input_path):
        print("File does not exist.")
        return

    try:
        width = int(input("Enter desired width: "))
    except ValueError:
        print("Invalid width.")
        return

    new_name = input("Enter new file name (without extension): ").strip()
    slug_name = slugify(new_name)

    resized_img = resize_image(input_path, width)

    output_file = f"{slug_name}.webp"
    resized_img.save(output_file, "WEBP")

    print(f"Saved as {output_file}")

if __name__ == "__main__":
    main()