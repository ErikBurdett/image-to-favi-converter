import os
from PIL import Image

# Directories for input images and output converted images
input_directory = 'images'
output_directory = 'conversion'

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define sizes and formats to convert
sizes = [(32, 32), (128, 128), (512, 512)]
formats = ['jpg', 'png', 'ico']

# Loop through all images in the input directory
for filename in os.listdir(input_directory):
    if filename.lower().endswith((".png", ".jpg", ".webp")):  # Add .webp support
        img_path = os.path.join(input_directory, filename)
        with Image.open(img_path) as img:
            img_basename = os.path.splitext(filename)[0]
            
            # Create a directory for this image inside the output directory
            img_output_dir = os.path.join(output_directory, img_basename)
            if not os.path.exists(img_output_dir):
                os.makedirs(img_output_dir)
            
            # Convert image to each size and format
            for size in sizes:
                # Create a directory for each size inside the image's directory
                size_dir = os.path.join(img_output_dir, f"{size[0]}x{size[1]}")
                if not os.path.exists(size_dir):
                    os.makedirs(size_dir)
                
                resized_img = img.resize(size)
                
                for file_format in formats:
                    # Define output path for each format within the size directory
                    output_path = os.path.join(size_dir, f"{img_basename}.{file_format}")
                    
                    # Save the image in the new size and format
                    if file_format == 'jpg':
                        resized_img.save(output_path, format='JPEG')  # Correct format for JPG
                    elif file_format == 'ico':
                        resized_img.save(output_path, format='ICO')
                    else:
                        resized_img.save(output_path, format=file_format.upper())

print(f"Images have been converted and saved to {output_directory}")
