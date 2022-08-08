bl_info = {
    "name": "Simple Export",
    "author": "Quentin Steinke",
    "version": (1, 0),
    "blender": (3, 2, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Export game ready assets the simple way",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy
import os

class PANEL_PT_SimpleExport(bpy.types.Panel):
    """Simple export panel"""
    bl_label = "SimpleExport"
    bl_idname = "OBJECT_PT_export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SimpleExport"

    def draw(self, context):
        layout = self.layout
        row = self.layout.row
        scene = context.scene
        obj = context.object

        layout.label(text="Simple Row: ")

Register_Unregister_Classes = (
    PANEL_PT_SimpleExport,

)


def register():
    print("Enabled the addon")

    for cls in Register_Unregister_Classes:
        bpy.utils.register_class(cls)

#clearing Blenders console
#os.system('cls')

def add_split_normals():
    current_selected_objects = bpy.context.selected_objects
    object = bpy.context.scene.objects

    for obj in current_selected_objects:
        if obj.type == "MESH":
            bpy.context.view_layer.objects.active = bpy.context.scene.objects[obj.name]
            bpy.ops.mesh.customdata_custom_splitnormals_add()
        else:
            print(obj.name + " Not type mesh")

def clear_split_normals():
    current_selected_objects = bpy.context.selected_objects

    for obj in current_selected_objects:
        bpy.context.view_layer.objects.active = bpy.context.scene.objects[obj.name]
        bpy.ops.mesh.customdata_custom_splitnormals_clear()

def duplicate_objects():
    duplicate_objects = []
    all_collections = bpy.data.collections
    current_selected_objects = bpy.context.selected_objects
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
    current_selected_objects = bpy.context.selected_objects

    bpy.ops.object.make_single_user(object=True, obdata=True)

    for obj in current_selected_objects:

        bpy.data.objects[obj.name].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[obj.name]
        if obj.type == "MESH":
            print("converting " + obj.name)
            bpy.ops.object.convert(target='MESH')
        else:
            print(obj.name + "Not a mesh")

    add_split_normals()

def combine_objects_by_parent():
    active_object = bpy.context.view_layer.objects.active

#duplicate_objects()
#prep_objects_for_combine()

def unregister():
    print("Disabling the addon")

    for cls in Register_Unregister_Classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()