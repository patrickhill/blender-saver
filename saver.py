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


def main(context,self):
    format = bpy.data.scenes['Scene'].render.image_settings.file_format
    if format == 'OPEN_EXR_MULTILAYER': extension = '.exr'
    if format == 'JPEG': extension = '.jpg'
    if format == 'PNG': extension = '.png'
    
    
    try:
        bpy.data.images['Render Result'].save_render(dirname(bpy.data.filepath) + '/exports/' + time.strftime("%y%m%d") + "-" + time.strftime("%H%M%S") + extension, scene=None)
        self.report({'INFO'}, "Image Saved")
    except:
        self.report({'INFO'}, "You must render an image before saving")
    

class Saver(bpy.types.Operator):
    bl_idname="myops.saver"
    bl_label="save rendered file"
    
    def execute(self, context):
        main(context,self)
        return {'FINISHED'}



addon_keymaps = []


def register():
    bpy.utils.register_class(Saver)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="Image", space_type="IMAGE_EDITOR")
        kmi = km.keymap_items.new("myops.saver", type="S", value="PRESS", shift=True, ctrl=True, oskey=True)
        addon_keymaps.append((km, kmi))

def unregister():
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(Saver)


if __name__ == "__main__":
    register()
