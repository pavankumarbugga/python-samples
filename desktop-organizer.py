import os
import shutil

# Define the path to your desktop folder
desktop_path = os.path.expanduser("~/Desktop")

# Define a dictionary to map file extensions to folder names
folder_mapping = {
    ".txt": "Text Files",
    ".pdf": "PDF Files",
    ".png": "Image Files",
    ".jpg": "Image Files",
    ".jpeg": "Image Files",
    ".gif": "Image Files",
    ".mp4": "Video Files",
    ".mov": "Video Files",
    ".zip": "Archive Files",
    ".rar": "Archive Files",
    ".exe": "Programs",
    ".msi": "Programs",
    ".dmg": "Programs",
}

# Create folders if they do not exist
for folder_name in folder_mapping.values():
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Loop through files in desktop folder and move them to corresponding folders
for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)
    if os.path.isfile(file_path):
        _, extension = os.path.splitext(file_path)
        folder_name = folder_mapping.get(extension, "Other Files")
        folder_path = os.path.join(desktop_path, folder_name)
        shutil.move(file_path, folder_path)
