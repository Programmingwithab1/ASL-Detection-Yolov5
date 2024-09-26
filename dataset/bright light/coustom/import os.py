import os
from PIL import Image

def convert_jpeg_to_jpg(input_dir, output_dir):
    """
    Converts all JPEG images in the input directory to JPG format and saves them in the output directory.
    """
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".jpeg") or filename.lower().endswith(".jpg"):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_dir, new_filename)
            img.save(output_path, "JPEG")

if __name__ == "__main__":
    input_directory = r"C:\Users\mabdu\Downloads\bright light\coustom\GH conversion"
    output_directory = r"C:\Users\mabdu\Downloads\bright light\coustom\640 X"  # Replace with your desired output directory
    convert_jpeg_to_jpg(input_directory, output_directory)
    print("Conversion completed successfully!")
