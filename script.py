import os
import shutil

# Source folder
source_folder = "source_images"

# Destination folder
destination_folder = "jpg_files"

# Create destination folder automatically
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Check files in source folder
for file_name in os.listdir(source_folder):

    # Move only JPG files
    if file_name.endswith((".jpg", ".png", ".jpeg")):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)

        print(file_name + " moved successfully!")

print("All JPG files moved!")