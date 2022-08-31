import bpy
import pathlib
from .. utils import add_split_normals, clear_split_normals, duplicate_objects, prep_objects_for_combine, combine_objects_by_parent, mark_as_finished, clear_custom_normals_selection
from bpy.props import BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty


class MarkAsFinished(bpy.types.Operator):
    """Mark asset as finished and move to "Finished" Collection"""
    bl_label = "Mark as finished"
    bl_idname = "assetcreate.mark_as_finished"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        print("Marking as finished")
        mark_as_finished()

        return {"FINISHED"}


class ClearCustomNormals_Selection(bpy.types.Operator):
    """Clear custom normals by selection"""
    bl_label = "Clear custom normals selection"
    bl_idname = "assetcreate.clear_customnormals_selection"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        clear_custom_normals_selection()

        return {"FINISHED"}


bpy.types.Scene.split_normals = BoolProperty(name="fix normals", description="Split normals before combine", default=True)
bpy.types.Scene.duplicate = BoolProperty(name="duplicate", description="Duplicate meshes before combine", default=True)


# Operator button to prep models
class PrepForExport(bpy.types.Operator):
    """Duplicates, preps and combines meshes for export"""
    bl_label = "Prep for export"
    bl_idname = "assetcreate.prepforexport"
    bl_options = {"REGISTER", "UNDO"}

    split_normals: BoolProperty(name="fix normals", description="Split normals before combine", default=True)
    duplicate: BoolProperty(name="duplicate", description="Duplicate meshes before combine", default=True)

    def draw(self, context):
        layout = self.layout
        duplicate = context.scene.duplicate
        split_normals = context.scene.split_normals
        col = layout.column()
        row = layout.row()
        row.prop(duplicate, "duplicate")
        row.prop(split_normals, "split_normals")

    def execute(self, context):
        print("Prepping assets")

        prep_objects_for_combine()

        # if self.split_normals == True:
            # self.add_split_normals()
        
        # if self.duplicate == True:
            # self.duplicate_objects()

        return {"FINISHED"}


# Operator button to clean up
class CleanUp(bpy.types.Operator):
    """Clean up simple export"""
    bl_label = "Clear Custom Normals"
    bl_idname = "assetcreate.cleanup"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        print("Simple clean up")
        clear_split_normals()

        return {"FINISHED"}


class SimpleExport(bpy.types.Operator):
    """Export selected objects"""
    bl_label = "Export Selected"
    bl_idname = "assetcreate.export"
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
    bl_idname = "assetcreate.simplepipes"
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


class RenameToSelected(bpy.types.Operator):
    """Rename active object to selected adding proper Prefix"""
    bl_label = "Rename To Selected"
    bl_idname = "assetcreate.renametoselected"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        print("RENAME TO SELECTED:")

        # get selected objects

        current_selected_objects = bpy.context.selected_objects
        current_active_object = bpy.context.view_layer.objects.active

        rename_objects = []

        for obj in current_selected_objects:
            rename_objects.append(obj)

        num = len(rename_objects)
        print(num)

        # check to to see if there are only 2 objects selected
        if len(rename_objects) == 2:
            print("RENAMING OBJECT:")
            print("index 0 object is: " + rename_objects[0].name)
            print("index 1 object is: " + rename_objects[1].name)
            obj0 = rename_objects[0]
            obj1 = rename_objects[1]

        elif len(rename_objects) > 2:
            self.report({"ERROR"}, "Too many objects selected. Select 2 objects to Rename To Selected")
        else:
            self.report({"ERROR"}, "You need to select 2 objects to Rename to Selected")
        # get not the selected objects name and store it in a "name" variable
        # add SM_ prefix to "name"
        # rename active object with "name"

        return {"FINISHED"}
