import os


# Files to update
user_path = os.path.expanduser("~")
destination_path = "\\AppData\\Roaming\\Blender Foundation\\Blender\\3.2\\scripts\\addons\\QuentinAddon"
g_cwd = os.getcwd()


def copy_all_Files(cwd):
    search_files = []
    remove_files = []

    search_files = (os.listdir(cwd))


    # Copy python files
    for file in search_files:
        print("------------")
        print(f"> Checking {file}")
        if file.endswith(".py"):
            print(f"Coppying {file}")
            print(f'copy "{cwd}\\{file}" "{user_path}\\{destination_path}"')
            remove_files.append(file)
            print("(Remaining files: ")
            for i in search_files:
                print(f"({i}")
            print("------------")
        else:
            os.listdir(f"{cwd}\\{file}")

    # Remove copied files from search list
    for file in remove_files:
        print(f"Removing copied files {file}")
        search_files.remove(file)


copy_all_Files(g_cwd)
