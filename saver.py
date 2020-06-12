import bpy

from os.path import dirname, exists, join
import time

def main(context):
    format = bpy.data.scenes['Scene'].render.image_settings.file_format
    if format == 'OPEN_EXR_MULTILAYER': extension = '.exr'
    if format == 'JPEG': extension = '.jpg'
    if format == 'PNG': extension = '.png'
    
    try:
        bpy.data.images['Render Result'].save_render(dirname(bpy.data.filepath) + '/exports/' + time.strftime("%y%m%d") + "-" + time.strftime("%H%M%S") + extension, scene=None)
    except:
        print('No renders yet. Rendering one for you.')
        bpy.ops.render.render(use_viewport=True)
    

class Saver(bpy.types.Operator):
    bl_idname="myops.saver"
    bl_label="save rendered file"
    
    def execute(self, context):
        main(context)
        return {'FINISHED'}


class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Layout Demo"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        bpy.app.handlers.render_complete

        layout.label(text="Save in background to //exports:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("myops.saver")
    
        
def my_handler(scene):
    print("Frame Change")
    bpy.utils.register_class(LayoutDemoPanel)


def register():
    bpy.utils.register_class(Saver)
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(Saver)
    bpy.utils.unregister_class(LayoutDemoPanel)


if __name__ == "__main__":
    register()

