imported_modules = {}


if "bpy" in locals():
    import importlib
    print("Reloading operatoins")
    importlib.reload(operations)
    # imported_modules[module_name] = locals()[module_name]
else:
    print(f"Importing operations")
    from . import operations
    # imported_modules[module_name] = locals()[module_name]

import bpy

bl_info = {
    "name": "Asset Create",
    "author": "Quentin Steinke",
    "version": (1, 0),
    "blender": (3, 2, 0),
    "location": "View3D",
    "description": "A asset creation toolset for Blender",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}


# N panel for the addon
class PANEL_PT_SimpleExport(bpy.types.Panel):
    """Asset Create"""
    bl_label = "AssetCreate"
    bl_idname = "OBJECT_PT_export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AssetCreate"

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
        col.operator(operations.PrepForExport.bl_idname, text=operations.PrepForExport.bl_label, icon="MOD_LINEART")
        row = layout.row()
        col.prop(context.scene, "simple_export_path")
        col.operator("assetcreate.export", icon="DISC")

        col = layout.column(align=True)
        col.label(text="Clean up: ")
        col.operator(operations.CleanUp.bl_idname, text=operations.CleanUp.bl_label, icon="SHADERFX")
        col.operator(operations.ClearCustomNormals_Selection.bl_idname, text=operations.ClearCustomNormals_Selection.bl_label, icon="MOD_TRIANGULATE")

        col = layout.column(align=True)
        col.label(text="WIP: ")
        col.operator(operations.SimplifyPipes.bl_idname, text=operations.SimplifyPipes.bl_label, icon="MOD_REMESH")
        col.operator(operations.RenameToSelected.bl_idname, text=operations.RenameToSelected.bl_label, icon="FONT_DATA")
        col.operator(operations.MarkAsFinished.bl_idname, text=operations.MarkAsFinished.bl_label, icon="CHECKMARK")
        col.operator(operations.GroupForExport.bl_idname, text=operations.GroupForExport.bl_label)
        row = layout.row()
        row.operator(operations.TestingCode.bl_idname, text=operations.TestingCode.bl_label, icon="FILE_SCRIPT")


Register_Unregister_Classes = [
    PANEL_PT_SimpleExport,
]


def register():
    operations.register()
    bpy.types.Scene.simple_export_path = bpy.props.StringProperty(
        name="Export Folder",
        subtype="DIR_PATH",
    )
    for cls in Register_Unregister_Classes:
        bpy.utils.register_class(cls)


def unregister():
    operations.unregister()
    print("Disabling the addon")
    del bpy.types.Scene.simple_export_path
    for cls in Register_Unregister_Classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
