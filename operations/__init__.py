from . import asset
from .asset import MarkAsFinished, ClearCustomNormals_Selection, PrepForExport, CleanUp, SimpleExport, SimplifyPipes, RenameToSelected, GroupForExport
from . import test
from .test import TestingCode, TestCode2, BmeshTest


Register_Unregister_Classes = [
    PrepForExport,
    CleanUp,
    SimpleExport,
    SimplifyPipes,
    RenameToSelected,
    MarkAsFinished,
    ClearCustomNormals_Selection,
    TestingCode,
    TestCode2,
    BmeshTest,
    GroupForExport
]
<<<<<<< HEAD
=======


def register():
    bpy.types.Scene.simple_export_path = bpy.props.StringProperty(
        name="Export Folder",
        subtype="DIR_PATH",
    )
    for cls in Register_Unregister_Classes:
        print(f"Regertering: {cls.__name__}")
        bpy.utils.register_class(cls)


def unregister():
    del bpy.types.Scene.simple_export_path
    for cls in Register_Unregister_Classes:
        print(str(cls))
        bpy.utils.unregister_class(cls)
>>>>>>> fcf365f718ca3b60d532c8cd224f463eea13783c
