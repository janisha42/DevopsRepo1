import os
import shutil
import sys
import datetime

def backup_files(source_dir, destination_dir):
    try:
        # Check if the source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError("Source directory does not exist.")
        
        # Check if the destination directory exists, create it if not
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        
        # Iterate through files in the source directory
        for filename in os.listdir(source_dir):
            source_file_path = os.path.join(source_dir, filename)
            destination_file_path = os.path.join(destination_dir, filename)
            
            # If the destination file already exists, append a timestamp to the filename
            if os.path.exists(destination_file_path):
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                filename, file_extension = os.path.splitext(filename)
                new_filename = f"{filename}_{timestamp}{file_extension}"
                destination_file_path = os.path.join(destination_dir, new_filename)
            
            # Copy the file from source to destination
            shutil.copy2(source_file_path, destination_file_path)
            print(f"Copied: {filename} to {destination_file_path}")
        
        print("Backup completed successfully.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)
