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
all_collections = bpy.data.collections

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
    duplicate_objects = []
    global all_collections
    global selected_objects
    selected = bpy.data.objects

    #adding a new collection to put all duplicate objects
    duplicate_collection = bpy.data.collections.new(name="Duplicated")
    bpy.context.scene.collection.children.link(duplicate_collection)

    #duplicating selected objects
    bpy.ops.object.duplicate()
    duplicated_objects = bpy.context.selected_objects

    #adding duplicated objects to duplicate_objects list
    for obj in duplicated_objects:
        duplicate_objects.append(obj)

    #remove duplicated objects from all collections
    for col in all_collections:
        #print(col.name)
        for obj in duplicate_objects:
            try:
                #print(obj.name + " unlinking object from " + col.name)
                col.objects.unlink(obj)
            except RuntimeError:
                pass
    
    #add selected objects to duplicated collection
    for obj in duplicated_objects:
        try:
            duplicate_collection.objects.link(obj)
            #print(obj.name + " linked to " + duplicate_collection.name)
        except RuntimeError:
            pass


def prep_objects_for_combine():
    selected_objects = bpy.context.selected_objects

    bpy.ops.object.make_single_user(object=True, obdata=True)

    for obj in selected_objects:

        bpy.data.objects[obj.name].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[obj.name]
        if obj.type == "MESH":
            print("converting " + obj.name)
            bpy.ops.object.convert(target='MESH')
        else:
            print(obj.name + "Not a mesh")

    add_split_normals()

duplicate_objects()
prep_objects_for_combine()

def unregister():
    print("Disabling the addon")