import os


# Files to update
user_path = os.path.expanduser("~")
destination_path = "\\AppData\\Roaming\\Blender Foundation\\Blender\\3.2\\scripts\\addons\\QuentinAddon"
g_cwd = os.getcwd()

print(f">{g_cwd}")
print(user_path + destination_path)

tab = "  "


def copy_all_Files(cwd, c):
    search_files = []
    remove_files = []
    dir_list = []
    tab = c
    current_dir = cwd.split("\\")[-1]
    search_files = (os.listdir(cwd))

    # Copy python files
    for file in search_files:
        if file.endswith(".py"):
            print(f"coppying {cwd}\\{file} to {user_path}{destination_path}\\{current_dir}")
            os.system(f'copy "{cwd}\\{file}" "{user_path}{destination_path}\\{current_dir}"')
            remove_files.append(file)
        elif os.path.isdir(f"{cwd}\\{file}") is True and file.startswith(".") == False:
            tab += tab
            new_cwd = f"{cwd}\\{file}"
            copy_all_Files(new_cwd, tab)

            dir_list.append(file)
        else:
            pass


copy_all_Files(g_cwd, tab)
