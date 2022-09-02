import bpy
import importlib
from bpy.props import BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty


# Adding split normals on selected objects
def add_split_normals():
    current_selected_objects = bpy.context.selected_objects
    # object = bpy.context.scene.objects

    for obj in current_selected_objects:
        if obj.type == "MESH":
            bpy.context.view_layer.objects.active = bpy.context.scene.objects[obj.name]
            bpy.ops.mesh.customdata_custom_splitnormals_add()
        else:
            print(obj.name + " Not type mesh")


# Clear split normals on selected objects
def clear_split_normals():
    current_selected_objects = bpy.context.selected_objects

    for obj in current_selected_objects:
        if obj.type == "MESH":
            bpy.context.view_layer.objects.active = bpy.context.scene.objects[obj.name]
            bpy.ops.mesh.customdata_custom_splitnormals_clear()
        else:
            print(obj.name + " Not type mesh")


# Duplicating selected objects
def duplicate_objects():
    duplicate_objects = []
    all_collections = bpy.data.collections
    # current_selected_objects = bpy.context.selected_objects
    # selected = bpy.data.objects

    # adding a new collection to put all duplicate objects
    SimpleExport_collection = bpy.data.collections.new(name="SimpleExport")
    bpy.context.scene.collection.children.link(SimpleExport_collection)

    # duplicating selected objects
    bpy.ops.object.duplicate()
    duplicated_objects = bpy.context.selected_objects

    # adding duplicated objects to duplicate_objects list
    for obj in duplicated_objects:
        duplicate_objects.append(obj)

    # remove duplicated objects from all collections
    for col in all_collections:
        # print(col.name)
        for obj in duplicate_objects:
            try:
                # print(obj.name + " unlinking object from " + col.name)
                col.objects.unlink(obj)
            except RuntimeError:
                pass

    # add selected objects to duplicated collection
    for obj in duplicated_objects:
        try:
            SimpleExport_collection.objects.link(obj)
            # print(obj.name + " linked to " + duplicate_collection.name)
        except RuntimeError:
            pass


def prep_objects_for_combine():
    current_selected_objects = bpy.context.selected_objects
    first_active_obj = bpy.context.active_object
    print(first_active_obj.name)

    bpy.ops.object.make_single_user(object=True, obdata=True)

    for obj in current_selected_objects:

        bpy.data.objects[obj.name].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[obj.name]
        if obj.type == "MESH":
            print("converting " + obj.name)
            bpy.ops.object.convert(target='MESH')
        else:
            print(obj.name + "Not a mesh")
    bpy.context.view_layer.objects.active = first_active_obj
    bpy.context.view_layer.objects.active = bpy.data.objects[first_active_obj.name]

    add_split_normals()


# Grouping ojects by parent empty and combining with parent name
def combine_objects_by_parent():
    active_object = bpy.context.view_layer.objects.active

# duplicate_objects()
# prep_objects_for_combine()


# Needs work
def mark_as_finished():
    """Mark asset as finished and move to "Finished" Collection"""
    active_objects = bpy.context.view_layer.objects.selected
    print(active_objects)

    all_collections = bpy.data.collections
    selected = bpy.data.objects

    # adding a new collection to put all duplicate objects
    if "Finished" in all_collections:
        print("Finished collection found")
        pass
    else:
        print("Making Finished collection")
        Finished_collection = bpy.data.collections.new(name="Finished")
        bpy.context.scene.collection.children.link(Finished_collection)

    # # remove duplicated objects from all collections
    # for col in all_collections:
    #     # print(col.name)
    #     for obj in active_objects:
    #         try:
    #             # print(obj.name + " unlinking object from " + col.name)
    #             col.objects.unlink(obj)
    #         except RuntimeError:
    #             pass


    # # # add selected objects to duplicated collection
    # for obj in active_objects:
    #     try:
    #         Finished_collection.objects.link(obj)
    #         # print(obj.name + " linked to " + duplicate_collection.name)
    #     except RuntimeError:
    #         pass


def clear_custom_normals_selection():
    print("clearing custom normals")
    bpy.ops.mesh.separate(type='SELECTED')
    bpy.ops.object.editmode_toggle()

    selection = bpy.context.view_layer.objects.selected
    selection_1 = bpy.context.view_layer.objects
    modifymesh = selection[1]
    originalobj = selection[0]

    bpy.context.view_layer.objects.active = modifymesh
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[modifymesh.name].select_set(True)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
    bpy.ops.mesh.mark_sharp(clear=True)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.customdata_custom_splitnormals_clear()

    print(selection_1)
    for obj in selection:
        bpy.context.view_layer.objects[obj.name].select_set(True)
        bpy.context.view_layer.objects.active = obj

    bpy.context.view_layer.objects.active = originalobj
    bpy.ops.object.join()
