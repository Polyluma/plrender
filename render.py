import bpy
import sys
import os
import objects



def start(job):
    cameras = job["cameras"]
    #mkdir?
    filepath = os.path.dirname(os.path.abspath(__file__))
    path, file_name = os.path.split(filepath)
    renderpath = path + "/render"
    if not os.path.exists(renderpath):
        os.makedirs(renderpath)

    # print(renderpath) 
    out = bpy.data.node_groups['outgroup']

    subfolder = "{}".format(job["label"])

    

    if str(job["background"]) == "flax":
        set_compositing_switch('material',False)
    elif str(job["background"]) == "wood": 
        set_compositing_switch('material',True) 

    if str(job["background"]) != "interior":
        if job["lights"] == "on":
            objects.hide_collection_from_render('lights-off')
            set_compositing_switch('wood',True)
            set_compositing_switch('flax',True)
        elif job["lights"] == "off":
            objects.hide_collection_from_render('lights-on')
            set_compositing_switch('wood',False)
            set_compositing_switch('flax',False)      


    out.nodes['out2'].base_path = '//render/'+subfolder

    #render
    for camera in cameras:
        # print("#### RENDER "+camera)
        #bpy.context.scene.camera = bpy.data.objects['Camera'+str(x)]
        activate_camera('c.'+camera)
    
        out.nodes['out2'].file_slots[0].path = "{}_{}_{}_{}".format(subfolder,job["lights"], camera, 'color')
        if str(job["background"]) != "interior":
            out.nodes['out2'].file_slots[1].path =   "{}_{}_{}_{}".format(subfolder,job["lights"], camera, 'white')
            out.nodes['out2'].file_slots[2].path =  "{}_{}_{}_{}".format(subfolder,job["lights"], camera, 'alpha')

        bpy.context.scene.render.filepath = "//render/render"+subfolder

        filetocheck = "./render/"+subfolder+'/'+"{}_{}_{}_{}".format(subfolder,job["lights"], camera, 'color')+'0001.png' 

        if files_exists(filetocheck): 
            print("SKIP!")
        else:
            bpy.ops.render.render(animation=False, write_still=False)



def files_exists(path):
    print('checking if file exists' + path)
    print(path)
    isFile = os.path.isfile(path) 
    return isFile



def set_compositing_switch(name,value):
    bpy.data.node_groups[name].nodes[name].check = value


def activate_camera(name):
    bpy.context.scene.camera = bpy.data.objects[name]
