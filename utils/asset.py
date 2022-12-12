import bpy
from bpy.props import BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty


def rename_asset(obj):
    obj_name = obj.name

    if "SM_" not in obj_name:
        obj_name = "SM_" + obj_name

    if ".0" in obj_name:
        obj_name = obj_name[:-4]

    if ".1" in obj_name:
        obj_name = obj_name[:-4]

    try:
        bpy.context.object.name = obj_name
    except NameError:
        pass


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

    # duplicating selected objects
    bpy.ops.object.duplicate()
    return bpy.context.selected_objects


def selected_to_simpleexport():
    selected_objects = bpy.context.selected_objects


    def link_selected_to_collection(collection_name):
        collection = bpy.data.collections[collection_name]
        
        for obj in selected_objects:
            try:
                collection.objects.link(obj)
            except RuntimeError:
                pass
            

    if "SimpleExport" in bpy.data.collections:
        
        for col in bpy.data.collections:
            for obj in selected_objects:
                try:
                    col.objects.unlink(obj)
                    link_selected_to_collection("SimpleExport")
                except RuntimeError:
                    pass
        
    else:
        
        SimpleExport_collection = bpy.data.collections.new(name="SimpleExport")
        bpy.context.scene.collection.children.link(SimpleExport_collection)
        
        for col in bpy.data.collections:
            for obj in selected_objects:
                try:
                    col.objects.unlink(obj)
                    link_selected_to_collection("SimpleExport")
                except RuntimeError:
                    pass


def prep_objects_for_combine():
    current_selected_objects = bpy.context.selected_objects
    first_active_obj = bpy.context.active_object

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
    simple_export_collection = bpy.data.collections["SimpleExport"]
    group_list = []

    for obj in simple_export_collection.all_objects:
        if "export" in obj:
            group_list.append(obj)

    for obj in group_list:
        parent_name = obj.name
        
        bpy.ops.object.select_all(action='DESELECT')
        
        bpy.data.objects[obj.name].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[obj.name]
        
        parent_location = obj.location
        parent_rotation = obj.rotation_euler
        
        bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE')
        group_children = bpy.context.selected_objects
            
        bpy.context.view_layer.objects.active = bpy.data.objects[group_children[0].name]

        bpy.ops.object.join()

        rename_asset(obj)



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


def select_object(object):
    bpy.data.objects[object.name].select_set(True)

def group_for_export():
    # get selected objects
    selected_obj = bpy.context.selected_objects
    first_selected = bpy.context.view_layer.objects.active

    # position cursor to center of objects
    bpy.context.scene.cursor.location = first_selected.location
    bpy.context.scene.cursor.rotation_euler = first_selected.rotation_euler
    cursor_locaiton = bpy.context.scene.cursor.location
    cursor_rotation = bpy.context.scene.cursor.rotation_euler
    # add empty to cursor position

    bpy.ops.object.empty_add(
        type='PLAIN_AXES',
        align='CURSOR',
        location=(cursor_locaiton),
        rotation=(cursor_rotation),
        scale=(1, 1, 1)
        )
    bpy.context.object.name = first_selected.name + "_GRP"

    group_parent = bpy.context.selected_objects
    group_parent = group_parent[0]

    # add custom property "export" to id it as a parent to export
    group_parent["export"] = True
    
    # parent selected objects to empty
    for obj in selected_obj:
        bpy.data.objects[obj.name].select_set(True)
    
    bpy.data.objects[group_parent.name].select_set(True)
    bpy.context.view_layer.objects.active = group_parent
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)


def group_export_fbx(export_path):
    selected_objects = bpy.context.selected_objects


    for obj in selected_objects:
        model_name = obj.name
        sufix_name = ".fbx"
        
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[obj.name].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[obj.name]
        
        bpy.ops.export_scene.fbx(
        filepath=export_path + model_name + sufix_name,
        check_existing=True, use_selection=True,
        apply_scale_options="FBX_SCALE_NONE",
        object_types={"EMPTY","MESH"},
        mesh_smooth_type="FACE",
        use_mesh_modifiers=True
        )


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
