import bpy
from . import asset
from .asset import MarkAsFinished, ClearCustomNormals_Selection, PrepForExport, CleanUp, SimpleExport, SimplifyPipes, RenameToSelected
from .test import TestingCode


Register_Unregister_Classes = [
    PrepForExport,
    CleanUp,
    SimpleExport,
    SimplifyPipes,
    RenameToSelected,
    MarkAsFinished,
    ClearCustomNormals_Selection,
    TestingCode,
]


def register():
    bpy.types.Scene.simple_export_path = bpy.props.StringProperty(
        name="Export Folder",
        subtype="DIR_PATH",
    )
    for cls in Register_Unregister_Classes:
        print(str(cls))
        bpy.utils.register_class(cls)


def unregister():
    del bpy.types.Scene.simple_export_path
    for cls in Register_Unregister_Classes:
        print(str(cls))
        bpy.utils.unregister_class(cls)