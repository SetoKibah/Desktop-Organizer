import os
import shutil

###### Define the path to the Downloads and Desktop folders
downloads_folder = "Your Downloads Path"
desktop_folder = "Your Desktop Path"

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
misc_folder = os.path.join(downloads_folder, "Miscellaneous")
os.makedirs(misc_folder, exist_ok=True)

# Iterate over all files in the Downloads folder
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue
    
    # Get the file extension
    _, file_ext = os.path.splitext(filename)
    
    # Determine the category based on the file extension
    category = file_categories.get(file_ext.lower(), "Miscellaneous")
    
    # Create the category folder if it doesn't exist
    category_folder = os.path.join(downloads_folder, category)
    os.makedirs(category_folder, exist_ok=True)
    
    # Move the file to the respective category folder
    shutil.move(file_path, os.path.join(category_folder, filename))

print("Files organized successfully!")


# Iterate over all files on the Desktop
for filename in os.listdir(desktop_folder):
    # Ignore the desktop.ini file
    if filename.lower() == "desktop.ini":
        continue
    
    file_path = os.path.join(desktop_folder, filename)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue
    
    # Get the file extension
    _, file_ext = os.path.splitext(filename)
    
    # Determine the category based on the file extension
    category = file_categories.get(file_ext.lower(), "Miscellaneous")
    
    # Create the category folder if it doesn't exist
    category_folder = os.path.join(downloads_folder, category)
    os.makedirs(category_folder, exist_ok=True)
    
    # Move the file to the respective category folder
    shutil.move(file_path, os.path.join(category_folder, filename))

print("Desktop files organized successfully!")