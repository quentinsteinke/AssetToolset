import os


# Files to update
user_path = os.path.expanduser("~")
destination_path = "\\AppData\\Roaming\\Blender Foundation\\Blender\\3.2\\scripts\\addons\\QuentinAddon"
g_cwd = os.getcwd()

print("------------New Directory------------")
print(f">{g_cwd}")


def copy_all_Files(cwd):
    print("starting search")
    search_files = []
    remove_files = []
    dir_list = []

    search_files = (os.listdir(cwd))
    print(search_files)

    # Copy python files
    for file in search_files:
        if file.endswith(".py"):
            print(file)
            remove_files.append(file)
        elif os.path.isdir(f"{cwd}\\{file}") is True and file.startswith(".") == False:
            dir_list.append(file)
        else:
            pass

    for dir in dir_list:
        new_cwd = f"{cwd}\\{dir}"
        print("------------New Directory------------")
        print(f">{dir}")
        copy_all_Files(new_cwd)

    # Remove copied files from search list
    for file in remove_files:
        search_files.remove(file)


copy_all_Files(g_cwd)
