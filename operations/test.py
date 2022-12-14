import bpy
import bmesh
from .. utils.test import testing_code, test_code_2, bmesh_testing


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


class BmeshTest(bpy.types.Operator):
    """Testing out Bmesh"""
    bl_label = "Testing Bmesh"
    bl_idname = "assetcreate.bmeshtesting"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bmesh_testing()

        return {"FINISHED"}
