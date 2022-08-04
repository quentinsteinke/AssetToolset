import bpy
import time
import os

bl_info = {
    "name": "Advanced Game Exporter",
    "blender": (3, 2, 1),
    "category": "Object",
}

def register():
    print("Enabled the addon")

#clearing Blenders console
os.system('cls')

#Defining Variables
scene = bpy.context.scene
selected_objects = bpy.context.selected_objects
split_custom_normals = bpy.ops.mesh.customdata_custom_splitnormals_add()
active_object = bpy.context.view_layer.objects.active

#Looping through selected objects and adding custom split normals
def split_normals():
    global active_object
    global split_custom_normals
    global selected_objects

    print(active_object.name)

    for obj in selected_objects:
        print("____________")
        print(obj.name)
        print(active_object.name)
        active_object = bpy.data.objects[obj.name]
        #split_custom_normals
        print(active_object.name)
        print("____________")
        time.sleep(1)

    print(active_object.name)

split_normals()

def unregister():
    print("Disabling the addon")