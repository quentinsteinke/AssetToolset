import collections
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
scene_collection = bpy.context.scene.collection.children

def add_split_normals():
    global selected_objects
    object = bpy.context.scene.objects

    for obj in selected_objects:
        if obj.type == "MESH":
            bpy.context.view_layer.objects.active = bpy.context.scene.objects[obj.name]
            bpy.ops.mesh.customdata_custom_splitnormals_add()
        else:
            print(obj.name + " Not type mesh")

def clear_split_normals():
    global selected_objects

    for obj in selected_objects:
        bpy.context.view_layer.objects.active = bpy.context.scene.objects[obj.name]
        bpy.ops.mesh.customdata_custom_splitnormals_clear()

def duplicate_objects():
    to_unlink = []
    global selected_objects
    selected = bpy.data.objects

    #adding a new collection to put all duplicate objects
    duplicate_collection = bpy.data.collections.new(name="Duplicated")
    bpy.context.scene.collection.children.link(duplicate_collection)

    #duplicating selected objects
    bpy.ops.object.duplicate()

    #move all duplicated objects to created collection
    for obj in selected_objects:
        try:
            duplicate_collection.objects.link(obj)
            print("objects linked to new collection")
        except RuntimeError:
            pass
        to_unlink.append(obj)
    
    for obj in to_unlink:
        print("code here")

duplicate_objects()

#add_split_normals()

def unregister():
    print("Disabling the addon")