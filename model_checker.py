import bpy

draw_calls = 0

selected_obj = bpy.context.selected_objects
first_selected = bpy.context.view_layer.objects.active

for obj in selected_obj:
    
    bpy.data.objects[obj.name].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[obj.name]
    
    material_slots = obj.material_slots
    
    draw_calls += len(material_slots)

print(draw_calls)