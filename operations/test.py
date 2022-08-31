import bpy
from .. utils.test import testing_code


class TestingCode(bpy.types.Operator):
    """Testing code"""
    bl_label = "Testing code"
    bl_idname = "simpleexport.testingcode"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        testing_code()

        return {"FINISHED"}
