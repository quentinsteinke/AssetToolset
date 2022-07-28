import bpy
import os

bl_info = {
    "name": "Advanced Game Exporter",
    "blender": (3, 2, 1),
    "category": "Object",
}

def register():
    print("Enabled the addon")

def unregister():
    print("Disabling the addon")

scene = bpy.context.scene
