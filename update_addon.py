import os


# Files to update
file_name = [
    "__init__.py",
    "operations",
    "utils"
]

# xcopy args /r /q /c /e /h /i /k /s /x /y

for file in file_name:

    current_dir = os.getcwd()
    blender_addon_path = "C:\\Users\\Quentin Steinke\\AppData\\Roaming\\Blender Foundation\\Blender\\3.2\\scripts\\addons\\QuentinAddon"

    if file.endswith(".py"):
        os.system(f'copy "{current_dir}\\{file}" "{blender_addon_path}"')
        pass
    else:
        current_dir = f'{current_dir}\\{file}'
        blender_addon_path = f'{blender_addon_path}\\{file}'
        files = os.listdir(current_dir)
        for file in files:
            os.system(f'copy "{current_dir}\\{file}" "{blender_addon_path}"')
