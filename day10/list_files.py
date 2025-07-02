import os

def list_files_in_folder(dir_path):
    try:
        files = os.listdir(dir_path)
        return (files, None)
    except FileNotFoundError:
        return (None, "Folder not found")
    except PermissionError:
        return (None, "Permission denied")

def main():
    dir_paths = input("Enter dir paths separated by <,> to list their content: ").split(",")
    for dir_path in dir_paths:
        files, error_message = list_files_in_folder(dir_path)
        if(files):
            print(f"Files in {dir_path}:")
            print(files)
        else:
            print(f"Error in {dir_path}: {error_message}")    

# this line makes sure that this script is not going
# to get executed when imported, only when executed directly
if __name__ == "__main__":
    main()