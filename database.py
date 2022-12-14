import mov as mov

def search_in_file(keys):
    file_types = {}
    with open(f"file_types/types_Cus.txt", "r") as file:
            for line in file:
                (key, val) = line.split()
                file_types[key] = val
            for i in file_types:
                if i == keys:
                    return True
            return False

def get_file():
    file_types = {}
    with open(f"file_types/types_Cus.txt", "r") as file:
            for line in file:
                (key, val) = line.split()
                file_types[key] = val
            return file_types
               
           

def add_to_file(key, value):
    with open(f"file_types/types_Cus.txt", "a") as file:
        if search_in_file(key):
            return "Error: File type already exists"
        else:   
            content = ""
            content += f" \n{key} {value}"
            print(content)
            #write in file on the next line
            file.write(content)
            return "File type added"

def change_in_file(key, value):
    with open(f"file_types/types_Cus.txt", "r") as file:
        content = get_file()
        if key in content.keys():
            content[key] = value
            return "File type changed"
        else:
            return "Error: File type does not exist"

def delete_from_file(key, value):
    with open(f"file_types/types_Cus.txt", "r") as file:
        content = get_file()
        if key in content.keys():
            del content[key]
            return "File type deleted"
        else:
            return "Error: File type does not exist"