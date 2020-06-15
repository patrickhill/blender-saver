bl_info = {
    "name": "Saver",
    "category": "Rendering",
    "author": "Patrick Hill",
    "version": (1, 0),
    "blender": (2, 80, 0),
}



import bpy

from os.path import dirname
import time


def main(context):
    format = bpy.data.scenes['Scene'].render.image_settings.file_format
    if format == 'OPEN_EXR_MULTILAYER': extension = '.exr'
    if format == 'JPEG': extension = '.jpg'
    if format == 'PNG': extension = '.png'
    
    try:
        bpy.data.images['Render Result'].save_render(dirname(bpy.data.filepath) + '/exports/' + time.strftime("%y%m%d") + "-" + time.strftime("%H%M%S") + extension, scene=None)
    except:
        print('No renders yet. You must render an image before you can save it.')
    

class Saver(bpy.types.Operator):
    bl_idname="myops.saver"
    bl_label="save rendered file"
    
    def execute(self, context):
        main(context)
        return {'FINISHED'}




class SaverMenu(bpy.types.Menu):
    bl_label = "Layout Demo"
    bl_idname = "viewImage.saverMenu"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Save in background to //exports:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("myops.saver")
    
        

def register():
    bpy.utils.register_class(Saver)
    bpy.utils.register_class(SaverMenu)
#    bpy.ops.wm.call_menu(name=SaverMenu.bl_idname)

def unregister():
    bpy.utils.unregister_class(Saver)
    bpy.utils.unregister_class(SaverMenu)


if __name__ == "__main__":
    register()
