import bpy
import time
import os

bl_info = {
    "name": "Game Exporter",
    "blender": (3, 2, 1),
    "category": "Object",
}

def register():
    print("Enabled the addon")

#clearing Blenders console
os.system('cls')

selected_objects = bpy.context.selected_objects

def add_split_normals():
    global selected_objects

    for obj in selected_objects:
        bpy.context.view_layer.objects.active = bpy.context.scene.objects[obj.name]
        bpy.ops.mesh.customdata_custom_splitnormals_add()

def add_split_normals():
    global selected_objects

    for obj in selected_objects:
        bpy.context.view_layer.objects.active = bpy.context.scene.objects[obj.name]
        bpy.ops.mesh.customdata_custom_splitnormals_clear()

add_split_normals()

def unregister():
    print("Disabling the addon")