import bpy
import importlib


def reload_addon():
    modules = [
        "operations"
    ]
    imported_modules = {}

    for module_name in modules:
        if module_name in locals():
            print(f"Reloading {module_name}")
            importlib.reload(locals()[module_name])
            imported_modules[module_name] = locals()[module_name]
        else:
            exec("from . import {}".format(module_name))
            imported_modules[module_name] = locals()[module_name]


def testing_code():
    print("Testing Code")
    newMesh = bpy.data.meshes.new("newMesh")
    newObject = bpy.data.objects.new(name="newObject", object_data=newMesh)
    scene = bpy.data.scenes["Scene"]

    materials = bpy.data.materials
    print("------------")
    for mat in materials:
        print(mat.name)

    objects = bpy.data.objects
    print("------------")
    for obj in objects:
        obj["myProperty"] = "look at me now"
        try:
            obj.data.vertices[0].co.x += 50
        except AttributeError:
            pass
        except IndexError:
            pass
        print(obj.name)

    meshes = bpy.data.meshes
    print("------------")
    for mesh in meshes:
        print(mesh.name)

    scenes = bpy.data.scenes
    print("------------")
    for sce in scenes:
        print(sce.name)


def test_code_2():
    print("test complete 2")
