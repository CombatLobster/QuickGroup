bl_info = {
    "name": "Quickgroup",
    "author": "spikedmcgrath",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "description": "Tools for quickly grouping objects to a new empty",
    "warning": "",
    "doc_url": "",
    "category": "Animation",
}

import bpy
import mathutils
    
#Create a new operator: "Group to new empty"
class GroupToNewEmpty(bpy.types.Operator):
    """Parent selected objects new empty at the centre position"""
    bl_label = "Group to empty"
    bl_idname = "object.qgroup_grouptonewempty"
    
    def execute(self, context):
        #Assign selected to list variable ctrlObjects
        ctrlObjects = bpy.context.selected_objects
        locValue = mathutils.Vector((0.00, 0.00, 0.00))

        #Find the mean point
        #Add the value of the .location for each item in the list ctrlObjects[] then divide by the length of the list
        for x in range(0, len(ctrlObjects)):
            locValue = locValue + ctrlObjects[x].location
            x += 1 
        locValue = locValue / len(ctrlObjects)
        bpy.context.scene.cursor.location = locValue

        #Add empty at the location
        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(locValue))


        #Reselect ctrlObjects
        for x in range(0, len(ctrlObjects)):
            ctrlObjects[x].select_set(state = True)
            print("Selected")
            x += 1

        #parent to empty
        bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

        return {'FINISHED'}

#Operator: Group to new empty at cursor location
class GroupAtCursor(bpy.types.Operator):
    """Parent selected objects to a new empty at 3d cursor"""
    bl_label = "Group at cursor"
    bl_idname = "object.qgroup_groupatcursor"
    
    def execute(self, context):
        #Assign selected to list variable ctrlObjects
        ctrlObjects = bpy.context.selected_objects

        locValue = bpy.context.scene.objects.data.cursor.location

        #Add empty at the location
        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(locValue))


        #Reselect ctrlObjects
        for x in range(0, len(ctrlObjects)):
            ctrlObjects[x].select_set(state = True)
            print("Selected")
            x += 1

        #parent to empty
        bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
        return {'FINISHED'}
 
#Create the panel in the 3d View
class QuickGroupPanel(bpy.types.Panel):
     bl_label = "Quick Group"
     bl_idname = "Panel_PT_QuickGroup"
     bl_space_type = 'VIEW_3D'
     bl_region_type = 'UI'
     bl_category = 'Item'
     
     def draw(self, context):
         layout = self.layout
         
         row = layout.row()
         row.operator("object.qgroup_grouptonewempty")
         row = layout.row()
         row.operator("object.qgroup_groupatcursor")
           
#Registration     
def register():
    bpy.utils.register_class(GroupToNewEmpty)
    bpy.utils.register_class(GroupAtCursor)
    bpy.utils.register_class(QuickGroupPanel)


def unregister():
    bpy.utils.unregister_class(GroupToNewEmpty)
    bpy.utils.unregister_class(GroupAtCursor)
    bpy.utils.unregister_class(QuickGroupPanel)

if __name__=="__main__":
    register()
    
