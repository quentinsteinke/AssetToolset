import bpy
from .. utils.test import testing_code, test_code_2, reload_addon


class ReloadAddon(bpy.types.Operator):
    """Reload Addon"""
    bl_label = "Reload Addon"
    bl_idname = "assetcreate.reloadaddon"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        reload_addon()

        return {"FINISHED"}


class TestingCode(bpy.types.Operator):
    """Testing code"""
    bl_label = "Testing code"
    bl_idname = "assetcreate.testingcode"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        testing_code()

        return {"FINISHED"}


class TestCode2(bpy.types.Operator):
    """Testing Code 2"""
    bl_label = "Testing Code 2"
    bl_idname = "assetcreate.testingcode2"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        test_code_2()

        return {"FINISHED"}
