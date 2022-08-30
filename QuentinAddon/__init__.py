import bpy
import sys
import os
import importlib

blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
    sys.path.append(blend_dir)

import operations as op
importlib.reload(op)

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
        scene = context.scene
        col = layout.column(align=True)
        # scene = context.scene
        # obj = context.object

        # Working on adding in a button
        col.label(text="Export: ")
        row = layout.row()
        row.prop(scene, "split_normals")
        row.prop(scene, "duplicate")
        col = layout.column(align=True)
        col.operator(op.PrepForExport.bl_idname, text=op.PrepForExport.bl_label, icon="MOD_LINEART")
        row = layout.row()
        col.prop(context.scene, "simple_export_path")
        col.operator("simpleexport.export", icon="DISC")

        col = layout.column(align=True)
        col.label(text="Simple Clean up: ")
        col.operator(op.CleanUp.bl_idname, text=op.CleanUp.bl_label, icon="SHADERFX")
        col.operator(op.ClearCustomNormals_Selection.bl_idname, text=op.ClearCustomNormals_Selection.bl_label, icon="MOD_TRIANGULATE")

        col = layout.column(align=True)
        col.label(text="Other Tools: ")
        col.operator(op.SimplifyPipes.bl_idname, text=op.SimplifyPipes.bl_label, icon="MOD_REMESH")
        col.operator(op.RenameToSelected.bl_idname, text=op.RenameToSelected.bl_label, icon="FONT_DATA")
        col.operator(op.MarkAsFinished.bl_idname, text=op.MarkAsFinished.bl_label, icon="CHECKMARK")
        row = layout.row()
        row.operator(op.TestingCode.bl_idname, text=op.TestingCode.bl_label, icon="FILE_SCRIPT")


Register_Unregister_Classes = [
    PANEL_PT_SimpleExport,
]


def register():
    op.register()
    print("Enabled the addon")
    bpy.types.Scene.simple_export_path = bpy.props.StringProperty(
        name="Export Folder",
        subtype="DIR_PATH",
    )
    for cls in Register_Unregister_Classes:
        bpy.utils.register_class(cls)


def unregister():
    op.unregister()
    print("Disabling the addon")
    del bpy.types.Scene.simple_export_path
    for cls in Register_Unregister_Classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
