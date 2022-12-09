import bpy
import bmesh


def testing_code():
    print("now does it update?")
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
            obj.data.vertices[0].co.x += 0.25
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


def bmesh_testing():
    myobj = bpy.context.view_layer.objects.active
    mymesh = bpy.data.meshes.get(myobj.to_mesh())
    bmesh.from_edit_mesh(myobj).edges.append(mymesh)
