import cv2
import os

# Update these paths
input_folder = r'C:\Users\prashant\OneDrive\Desktop\TaskCV_project\data\frames\extracted_frames'             # folder with original images
output_folder = r'C:\Users\prashant\OneDrive\Desktop\TaskCV_project\data\frames'   # where resized images will be saved

# Desired size
resize_width = 1024
resize_height = 1024
filename_prefix = "padel_analytics"

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Loop through images in input folder
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    
    # Skip non-image files
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')):
        print(f"Skipping non-image file: {filename}")
        continue

    # Read image
    image = cv2.imread(input_path)
    if image is None:
        print(f"Could not read image: {filename}")
        continue

    # Resize image
    resized_image = cv2.resize(image, (resize_width, resize_height))

    # Save resized image
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, resized_image)
    print(f"Saved resized image: {output_path}")

print(" Image resizing complete!")
