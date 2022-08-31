import os

blender_addon_path = "'C:\\Users\\Quentin Steinke\\AppData\\Roaming\\Blender Foundation\\Blender\\3.2\\scripts\\addons\\QuentinAddon'"
current_dir = os.getcwd()

# Files to update
file_name = [
    "__init__.py",
    "operations",
    "utils"
]

for file in file_name:
    os.system(f"xcopy '{current_dir}\\{file}' {blender_addon_path} /c /d /e /h /i /k /q /r /s /x /y")
