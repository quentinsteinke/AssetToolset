import os


# Files to update
search_files = [
    "__init__.py",
    "operations",
    "utils"
]
user_path = os.path.expanduser("~")
blender_path = "\\AppData\\Roaming\\Blender Foundation\\Blender\\3.2\\scripts\\addons\\QuentinAddon"

current_dir = os.getcwd()
blender_addon_path = f"{user_path}{blender_path}"


def copy_files(files):
    new_files = []

    for file in files:
        if file.endswith(".py"):
            print(f"Copping {file}")
            # os.system(f'copy "{current_dir}\\{file}" "{blender_addon_path}"')
            pass
        else:
            print(f"Adding {file} to dir list")
            current_dir = f'{current_dir}\\{file}'
            blender_addon_path = f'{blender_addon_path}\\{file}'
            new_dir = os.listdir(current_dir)
            new_files.append(new_dir)
            copy_files(new_files)


copy_files(search_files)
