import os
from pathlib import Path

# Define the path to the Downloads and Desktop folders
downloads_folder = Path("C:/Users/YourUsername/Downloads")
desktop_folder = Path("C:/Users/YourUsername/Desktop")

# Create a dictionary to map file extensions to their respective categories
file_categories = {
    ".txt": "Text",
    ".docx": "Documents",
    ".xlsx": "Spreadsheets",
    ".jpg": "Images",
    ".mp3": "Music",
    ".mp4": "Videos",
    ".zip": "Archives",
    ".pdf": "Documents",
    ".png": "Images",
    ".gif": "Images",
    ".jpeg": "Images",
    ".rar": "Archives",
    ".blend": "3D Modeling",
    ".fbx": "3D Modeling",
    ".obj": "3D Modeling",
    ".stl": "3D Modeling",
    ".dwg": "CAD Files",
    ".dxf": "CAD Files",
    ".svg": "Vector Images",
    ".ai": "Vector Images",
    ".eps": "Vector Images",
    ".psd": "Photoshop Files",
    ".indd": "InDesign Files",
    ".pptx": "Presentations",
    ".key": "Presentations",
    ".csv": "Spreadsheets",
    ".json": "Data Files",
    ".xml": "Data Files" 
}

# Create a miscellaneous folder to store files with unknown extensions
misc_folder = downloads_folder / "Miscellaneous"
misc_folder.mkdir(exist_ok=True)

def organize_files(folder_path):
    # Iterate over all files in the folder
    for file_path in folder_path.iterdir():
        # Skip directories
        if file_path.is_dir():
            continue

        # Get the file extension
        file_ext = file_path.suffix

        # Determine the category based on the file extension
        category = file_categories.get(file_ext.lower(), "Miscellaneous")

        # Create the category folder if it doesn't exist
        category_folder = folder_path / category
        category_folder.mkdir(exist_ok=True)

        # Move the file to the respective category folder
        try:
            file_path.rename(category_folder / file_path.name)
        except Exception as e:
            print(f"Failed to move file {file_path.name}: {e}")

    print(f"{folder_path.name} files organized successfully!")

organize_files(downloads_folder)
organize_files(desktop_folder)