import os
import shutil


def get_file_types(chose):
    # insert from the types_<chose>.txt file the file types
    file_types = {}
    for i in chose:
        if i == "All":
            with open(f"file_types/types_All.txt", "r") as file:
                for line in file:
                    (key, val) = line.split()
                    file_types[key] = val
                return file_types
        else:
            with open(f"file_types/types_{i}.txt", "r") as file:
                for line in file:
                    (key, val) = line.split()
                    file_types[key] = val
    #print(file_types)
    return file_types


def run(origin, destination, chose):
    # Get the path from the user
    user_path = origin

    #get destination path
    dest_path = destination
    print(f'{user_path} + " " + {dest_path}')
    choosen = []
    #check if chose is not empty    
    for i in chose:
        if i != "0" or i != "":
            choosen.append(i)
    if len(choosen) == 0:
        return "Error: NO CHOICE WAS MADE"


    #check if the path exists
    if not os.path.exists(user_path) or not os.path.exists(dest_path):
        return "Error: Path does not exist"
        
    else:
        # Define the directory where the files are located
        root_dir = user_path
        # Iterate over the files in the root directory
        for filename in os.listdir(root_dir):
            # Get the file's extension
            ext = os.path.splitext(filename)[1]
            # Get the file types from the dictionary
            get_files = get_file_types(choosen)
            # Check if the file type is in the dictionary
            if ext in get_files.keys():
                # Create the full path to the destination folder
                dest_dir = os.path.join(dest_path, get_files[ext])

                # If the folder doesn't already exist, create it
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                # Move the file to the destination folder
                try:
                    shutil.move(os.path.join(dest_path, filename), dest_dir)
                except:
                    #return "Error: File already exists"
                    pass
        return "success"
