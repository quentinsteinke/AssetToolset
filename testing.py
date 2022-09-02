import os


# Files to update
user_path = os.path.expanduser("~")
destination_path = "\\AppData\\Roaming\\Blender Foundation\\Blender\\3.2\\scripts\\addons\\QuentinAddon"
g_cwd = os.getcwd()

print(f">{g_cwd}")

tab = "  "


def copy_all_Files(cwd, c):
    search_files = []
    remove_files = []
    dir_list = []
    tab = c
    search_files = (os.listdir(cwd))

    # Copy python files
    for file in search_files:
        if file.endswith(".txt"):
            print(f"{tab}  |<{file}")
            remove_files.append(file)
        elif os.path.isdir(f"{cwd}\\{file}") is True and file.startswith(".") == False:
            tab += tab
            print("")
            print(f"{tab}>{file}")
            print(f"{tab}  |")
            new_cwd = f"{cwd}\\{file}"
            copy_all_Files(new_cwd, tab)

            dir_list.append(file)
        else:
            pass


copy_all_Files(g_cwd, tab)
