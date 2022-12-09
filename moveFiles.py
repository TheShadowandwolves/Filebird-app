import os
import shutil




# Create a dictionary that maps file types to folder names
file_types = {
    '.txt': 'text_files',
    '.pdf': 'pdf_files',
    '.docx': 'word_files',
    '.png': 'image_files',
    '.mp3': 'audio_files',
    '.mp4': 'video_files',
    '.zip': 'zip_files',
    '.exe': 'exe_files',
    '.iso': 'iso_files',
    '.jpg': 'image_files',
    '.jpeg': 'image_files',
    '.gif': 'image_files',
    '.bmp': 'image_files',
    '.svg': 'image_files',
    '.psd': 'image_files',
    '.ai': 'image_files',
    '.indd': 'image_files',
    '.mpg': 'video_files',
    '.json': 'json_files',
    '.csv': 'csv_files',
    '.xlsx': 'excel_files',
    '.pptx': 'powerpoint_files',
    '.html': 'html_files',
    '.css': 'css_files',
    '.js': 'js_files',
    '.php': 'php_files',
    '.py': 'python_files',
    '.dll': 'dll_files',
    '.xml': 'xml_files',
    '.xhtml': 'xhtml_files',
    '.sql': 'sql_files',
    '.htm': 'html_files',
    '.c': 'c_files',
    '.cpp': 'cpp_files',
    '.h': 'h_files',
    '.hpp': 'hpp_files',
    '.java': 'java_files',
    '.jar': 'jar_files',
    '.class': 'class_files',
    '.PDF': 'pdf_files',
    '.DOCX': 'word_files',
    '.PNG': 'image_files',
    '.bin': 'bin_files',
    '.stl': 'stl_files',
    '.obj': 'obj_files',
    '.xls': 'excel_files',
    '.viso': 'viso_files',
    '.vmdk': 'vmdk_files',
    '.vdi': 'vdi_files',
    '.7z': '7z_files',
    '.ppt': 'powerpoint_files',
    '.doc': 'word_files',
    '.ico': 'ico_files',
    '.odt': 'odt_files',
}

def edit_file_types():
    print("Enter the file extension you want to add to the dictionary.")
    user_ext = input("Enter the file extension: ")
    while user_ext != "":
        if user_ext in file_types.keys():
            print("File extension already exists in the dictionary.")
            user_ext = input("Enter the file extension: ")
        else:
            print("Enter the folder name you want to add to the dictionary.")
            user_folder = input("Enter the folder name: ")
            file_types[user_ext] = user_folder
            break

def edit_folder_names():
    print("Enter the folder name you want to edit in the dictionary.")
    user_folder = input("Enter the folder name: ")
    while user_folder != "":
        if user_folder not in file_types.values():
            print("Folder name does not exist in the dictionary.")
            user_folder = input("Enter the folder name: ")
        else:
            print("Enter the new folder name you want to add to the dictionary.")
            user_new_folder = input("Enter the new folder name: ")
            for key, value in file_types.items():
                if value == user_folder:
                    file_types[key] = user_new_folder
                    print("Folder name has been changed.")
                    break
            break

def run():
    # Get the path from the user
    user_path = input("Enter the path name: ")
    #check if the path exists
    while user_path != "":
        if not os.path.exists(user_path):
            print("Path does not exist")
            user_path = input("Enter the path name: ")
        else:
            break
    # Exit the program if the user doesn't enter a path
    if user_path == "":
        exit()

    # Define the directory where the files are located
    root_dir = user_path
    # Iterate over the files in the root directory
    for filename in os.listdir(root_dir):
        # Get the file's extension
        ext = os.path.splitext(filename)[1]

        # Check if the file type is in the dictionary
        if ext in file_types:
            # Create the full path to the destination folder
            dest_dir = os.path.join(root_dir, file_types[ext])

            # If the folder doesn't already exist, create it
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            # Move the file to the destination folder
            shutil.move(os.path.join(root_dir, filename), dest_dir)

def intro():
    print("This program will move files from a folder to subfolders based on file type.")
    print("Enter 0 to exit the program.")
    print("Enter 1 to run the program.")
    print("Enter 2 to edit file types.")
    print("Enter 3 to edit folder names.")
    user_choice = input("Enter your choice: ")
    return user_choice

user_choice = intro()
while user_choice != "0":
    if user_choice == "1":
        run()
        user_choice = intro()
    elif user_choice == "2":
        edit_file_types()
        user_choice = intro()
    elif user_choice == "3":
        edit_folder_names()
        user_choice = intro()
    else:
        print("Invalid choice. Exiting program.")
        exit()

