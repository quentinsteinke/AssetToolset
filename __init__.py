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

scene = bpy.context.scene
selected_objects = bpy.context.selected_objects
split_custom_normals = bpy.ops.mesh.customdata_custom_splitnormals_add()
active_object = bpy.context.view_layer.objects.active

for obj in selected_objects:
    #print(obj.name)
    print(active_object.name)
    active_object = bpy.data.objects[obj.name]
    print(active_object.name)
    #time.sleep(2)
    #split_custom_normals
    print("____________")
    #split_custom_normals

def unregister():
    print("Disabling the addon")