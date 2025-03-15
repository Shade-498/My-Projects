from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

def apply_filter(image, filter_name): # Apply the selected filter to the image
    if filter_name == "blur":
        return image.filter(ImageFilter.BLUR)
    elif filter_name == "contour":
        return image.filter(ImageFilter.CONTOUR)
    elif filter_name == "detail":
        return image.filter(ImageFilter.DETAIL)
    elif filter_name == "edge_enhance":
        return image.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_name == "emboss":
        return image.filter(ImageFilter.EMBOSS)
    elif filter_name == "sharpen":
        return image.filter(ImageFilter.SHARPEN)
    elif filter_name == "smooth":
        return image.filter(ImageFilter.SMOOTH)
    else:
      print("Invalid filter name. Please choose a valid filter.")


def resize_image(image, width, height): # Resize the image to the specified width and height
    return image.resize((width, height))


def rotate_image(image, angle): # Rotate the image by the specified angle
    return image.rotate(angle)


def flip_image(image, direction): # Flip the image horizontally or vertically
    if direction == "h":
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    elif direction == "v":
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        print("Invalid direction. Please choose 'horizontal' or 'vertical'.")


def crop_image(image, left, top, right, bottom): # Crop the image to the specified coordinates
    return image.crop((left, top, right, bottom))


def convert_to_grayscale(image): # Convert the image to grayscale
    return image.convert("L")


def add_watermark(image, watermark_text, position, font_size): # Add a watermark to the image
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)

    bbox = draw.textbbox((0, 0), watermark_text, font=font) # Get the bounding box of the text
    text_width = bbox[2] - bbox[0] # Get the width of the text
    text_height = bbox[3] - bbox[1] # Get the height of the text

    width, height = image.size

    margin = 20

    if position == "top-left":
        x = margin
        y = margin
    elif position == "top-right":
        x = width - text_width - margin
        y = margin
    elif position == "bottom-left":
        x = margin
        y = height - text_height - margin
    elif position == "bottom-right":
        x = width - text_width - margin
        y = height - text_height - margin
    elif position == "center":
        x = (width - text_width) // 2
        y = (height - text_height) // 2
    else:
        print("Invalid position. Please choose 'top-left', 'top-right', 'bottom-left', 'bottom-right', or 'center'.")
        x = width - text_width - margin
        y = height - text_height - margin


    if x < margin:
        x = margin # Left margin
    if y < margin:
        y = margin # Top margin
    if x + text_width > width - margin:
        x = width - text_width - margin # Right margin
    if y + text_height > height - margin:
        y = height - text_height - margin # Bottom margin


    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
    return image


def save_image(image, output_path): # Save the image to the specified output path``
    if not os.path.splitext(output_path)[1]: # If the output path does not have an extension, add .png
        output_path += ".png"
        print("Added .png extension to output path.")

    image.save(output_path)
    print("Image saved successfully.")


def main():
    image_path = input("Enter the path to the image file: ") # Get the path to the image file
    try:
        image = Image.open(image_path) # Open the image file
    except FileNotFoundError:
        print("File not found.")
        return

    while True:
        print("1. Apply filter")
        print("2. Resize image")
        print("3. Rotate image")
        print("4. Flip image")
        print("5. Crop image")
        print("6. Convert to grayscale")
        print("7. Add watermark")
        print("8. Save image")
        print("9. Exit")
        choice = input("Enter your choice(1-9): ")

        if choice == "1": # Apply filter
            filter_name = input("Enter the name of the filter to apply (blur, contour, detail, edge_enhance, emboss, sharpen, smooth): ")
            filtered_image = apply_filter(image, filter_name)
            filtered_image.show()
        elif choice == "2": # Resize image
            width = int(input("Enter the new width: "))
            height = int(input("Enter the new height: "))
            resized_image = resize_image(image, width, height)
            resized_image.show()
        elif choice == "3": # Rotate image
            angle = int(input("Enter the angle to rotate the image: "))
            rotated_image = rotate_image(image, angle)
            rotated_image.show()
        elif choice == "4": # Flip image
            direction = input("Enter the direction to flip the image (horizontal - h or vertical - v): ")
            flipped_image = flip_image(image, direction)
            flipped_image.show()
        elif choice == "5": # Crop image
            left = int(input("Enter the left coordinate: "))
            top = int(input("Enter the top coordinate: "))
            right = int(input("Enter the right coordinate: "))
            bottom = int(input("Enter the bottom coordinate: "))
            cropped_image = crop_image(image, left, top, right, bottom)
            cropped_image.show()
        elif choice == "6": # Convert to grayscale
            grayscale_image = convert_to_grayscale(image)
            grayscale_image.show()
        elif choice == "7": # Add watermark
            watermark_text = input("Enter the text to add as a watermark: ")
            position = input("Enter the position of the watermark (top-left, top-right, bottom-left, bottom-right, center): ")
            font_size = int(input("Enter the font size: ").lower())
            watermarked_image = add_watermark(image, watermark_text, position, font_size)
            watermarked_image.show()
        elif choice == "8": # Save image
            output_path = input("Enter the path to save the image: ")
            save_image(image, output_path)
        elif choice == "9": # Exit
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()