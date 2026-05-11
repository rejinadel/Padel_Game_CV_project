import os
import random
import shutil


# INPUT DIRECTORIES


#  resized image folder
image_dir = r"C:\Users\prashant\OneDrive\Desktop\Taskcv_project\data\frames\resized_frames"

# YOLO txt labels folder
label_dir = r"C:\Users\prashant\OneDrive\Desktop\Taskcv_project\labelled"


# OUTPUT DIRECTORIES


# Images
train_img_dir = r"C:\Users\prashant\OneDrive\Desktop\Taskcv_project\datasets\images\train"
val_img_dir = r"C:\Users\prashant\OneDrive\Desktop\Taskcv_project\datasets\images\val"
test_img_dir = r"C:\Users\prashant\OneDrive\Desktop\Taskcv_project\datasets\images\test"

# Labels
train_lbl_dir = r"C:\Users\prashant\OneDrive\Desktop\Taskcv_project\datasets\labels\train"
val_lbl_dir = r"C:\Users\prashant\OneDrive\Desktop\Taskcv_project\datasets\labels\val"
test_lbl_dir = r"C:\Users\prashant\OneDrive\Desktop\Taskcv_project\datasets\labels\test"

# CREATE OUTPUT FOLDERS

output_dirs = [
    train_img_dir,
    val_img_dir,
    test_img_dir,
    train_lbl_dir,
    val_lbl_dir,
    test_lbl_dir,
]

for folder in output_dirs:
    os.makedirs(folder, exist_ok=True)

# GET ALL IMAGES

images = [
    f for f in os.listdir(image_dir)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

print(f"\nTotal images found: {len(images)}")

# Shuffle images
random.shuffle(images)

# SPLIT RATIOS

train_ratio = 0.7
val_ratio = 0.2

total_images = len(images)

train_end = int(total_images * train_ratio)
val_end = train_end + int(total_images * val_ratio)

train_files = images[:train_end]
val_files = images[train_end:val_end]
test_files = images[val_end:]

# COPY FUNCTION

def copy_files(file_list, img_dest, lbl_dest):

    for image_file in file_list:

        # Full image source path
        img_src = os.path.join(image_dir, image_file)

        # Label filename
        label_file = os.path.splitext(image_file)[0] + ".txt"

        # Full label source path
        lbl_src = os.path.join(label_dir, label_file)

        # Copy image
        shutil.copy(img_src, os.path.join(img_dest, image_file))

        # Copy label if exists
        if os.path.exists(lbl_src):
            shutil.copy(lbl_src, os.path.join(lbl_dest, label_file))
        else:
            print(f"Missing label: {label_file}")

# COPY TRAIN / VAL / TEST

copy_files(train_files, train_img_dir, train_lbl_dir)
copy_files(val_files, val_img_dir, val_lbl_dir)
copy_files(test_files, test_img_dir, test_lbl_dir)

# FINAL SUMMARY

print("\nDataset split complete!")
print(f"Train images: {len(train_files)}")
print(f"Validation images: {len(val_files)}")
print(f"Test images: {len(test_files)}")