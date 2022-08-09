from msilib.schema import Icon
import bpy
import pathlib
import os
from bpy.props import BoolProperty

bl_info = {
    "name": "Simple Export",
    "author": "Quentin Steinke",
    "version": (1, 0),
    "blender": (3, 2, 0),
    "location": "View3D",
    "description": "Export game ready assets the simple way",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

# clearing Blenders console
# os.system('cls')


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


# Grouping ojects by parent empty and combining with parent name
def combine_objects_by_parent():
    active_object = bpy.context.view_layer.objects.active

# duplicate_objects()
# prep_objects_for_combine()


# Operator button to prep models
class PrepForExport(bpy.types.Operator):
    """Duplicates, preps and combines meshes for export"""
    bl_label = "Prep for export"
    bl_idname = "simpleexport.prepforexport"
    bl_options = {"REGISTER", "UNDO"}

    split_normals = BoolProperty(name="fix normals", default=True)
    duplicate = BoolProperty(name="duplicate", default=True)

    def draw(self, context):
        layout = self.layout
        # column = layout.column()
        
        row = layout.row()
        row.prop(self, "split_normals")

    def execute(self, context):
        print("Prepping assets")

        if self.split_normals == True:
            self.add_split_normals()
        
        if self.duplicate == True:
            self.duplicate_objects()

        return {"FINISHED"}



# Operator button to clean up
class CleanUp(bpy.types.Operator):
    """Clean up simple export"""
    bl_label = "Clean up"
    bl_idname = "simpleexport.cleanup"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        print("Prepping assets")
        clear_split_normals()

        return {"FINISHED"}


class SimpleExport(bpy.types.Operator):
    """Export selected objects"""
    bl_label = "Export Selected"
    bl_idname = "simpleexport.export"
    bl_options = {"REGISTER", "UNDO"}

    # selected_objects = bpy.context.selected_objects

    def execute(self, context):
        simple_export_path = bpy.path.abspath(context.scene.simple_export_path)
        print(simple_export_path)
        export_path = pathlib.Path(simple_export_path)
        # for 
        # bpy.ops.export_mesh(filepath="")

        return {"FINISHED"}


class SimplifyPipes(bpy.types.Operator):
    """Simplify Pipes"""
    bl_label = "Simplify Pipes"
    bl_idname = "simpleexport.simplepipes"
    bl_options = {"REGISTER", "UNDO"}

    # selected_objects = bpy.context.selected_objects

    def execute(self, context):
        print("SimplifyPipe")

        # Reduce edge count by halfa
        bpy.ops.mesh.loop_multi_select(ring=True)
        bpy.ops.mesh.select_nth()
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.mesh.dissolve_mode(use_verts=True)

        return {"FINISHED"}


# N panel for the addon
class PANEL_PT_SimpleExport(bpy.types.Panel):
    """Simple export panel"""
    bl_label = "SimpleExport"
    bl_idname = "OBJECT_PT_export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SimpleExport"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = layout.column(align=True)
        # scene = context.scene
        # obj = context.object

        # Working on adding in a button
        col.label(text="Export: ")
        row = layout.row()
        col.operator(PrepForExport.bl_idname, text= PrepForExport.bl_label, icon= "FILEBROWSER")
        row = layout.row()
        col.prop(context.scene, "simple_export_path")
        col.operator("simpleexport.export")

        col = layout.column(align=True)
        col.label(text="Clean up: ")
        row = layout.row()
        row = layout.row()
        row.operator(CleanUp.bl_idname, text= CleanUp.bl_label, icon= "SHADERFX")

        col = layout.column(align=True)
        col.label(text="Model Reduction: ")
        col.operator(SimplifyPipes.bl_idname, text= SimplifyPipes.bl_label)


Register_Unregister_Classes = [
    PANEL_PT_SimpleExport,
    PrepForExport,
    CleanUp,
    SimpleExport,
    SimplifyPipes,
]


def register():
    print("Enabled the addon")
    bpy.types.Scene.simple_export_path = bpy.props.StringProperty(
        name="Export Folder",
        subtype="DIR_PATH",
    )
    for cls in Register_Unregister_Classes:
        bpy.utils.register_class(cls)

def unregister():
    print("Disabling the addon")
    del bpy.types.Scene.simple_export_path
    for cls in Register_Unregister_Classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()