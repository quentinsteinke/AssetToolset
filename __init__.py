import bpy
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
    print(obj.name)
    bpy.context.view_layer.objects.active = bpy.data.objects[obj.name]
    split_custom_normals
    print("____________")
    #split_custom_normals

def unregister():
    print("Disabling the addon")