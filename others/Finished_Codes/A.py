import os
import shutil
from pathlib import Path

# Define the directory to watch and where files should go
source_dir = "C:/Users/acer/Downloads"
dest_folders = {
    "CF": "C:/Users/acer/Downloads/CF_Files",
    "PT": "C:/Users/acer/Downloads/product tamples",
    "Default": "C:/Users/acer/Downloads/Other_Files"
}

def sort_files():
    # Create destination folders if they don't exist
    for folder in dest_folders.values():
        Path(folder).mkdir(parents=True, exist_ok=True)
    
    files_moved = 0
    
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        
        # Skip directories, focus on files
        if os.path.isfile(source_path):
            # Logic to check the end of the filename (before extension)
            name, ext = os.path.splitext(filename)
            
            # Determine destination folder
            if name.endswith("CF"):
                dest_folder = dest_folders["CF"]
            elif name.endswith("PT"):
                dest_folder = dest_folders["PT"]
            else:
                dest_folder = dest_folders["Default"]
            
            dest_path = os.path.join(dest_folder, filename)
            
            # Handle filename conflicts
            if os.path.exists(dest_path):
                base_name, extension = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dest_path):
                    new_filename = f"{base_name}_{counter}{extension}"
                    dest_path = os.path.join(dest_folder, new_filename)
                    counter += 1
            
            try:
                shutil.move(source_path, dest_path)
                print(f"Moved: {filename} → {dest_folder}")
                files_moved += 1
            except Exception as e:
                print(f"Error moving {filename}: {e}")
    
    print(f"\nTotal files moved: {files_moved}")

if __name__ == "__main__":
    sort_files()