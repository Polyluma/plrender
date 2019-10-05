import bpy
import sys
import os

def construct(job):
    # print('CONSTRUCT LAMP')
    #global settings
    light_state = job['lights']
    rotation = job['rotation']     

    for lamp in job['lamps']: 
        #1 import shade
        append_shade(lamp,light_state)
        #2 import Hub
        append_hub(lamp)
        #3 import Cap
        append_cap(lamp)
        #4 import Cable
        append_cable(lamp)

        #hide instance 
        hide_collection_from_render('build')

def append_cable(lamp):
    set_active_layer(lamp['collection']) 
    # Import Shade
    # print(lamp['cable']) 
    cable_material = lamp['cable_material']
    cable_id = lamp['cable'] 
    cable_folder = "cables/"
    #key = "%s-%s" % (shade_model,shade_material) 
    cable_blenderobject_name = "%s.%s" % (cable_id,cable_material) 
    #model, blenderobject_name, section, 
    try:
        append_from_blendfile(cable_id,cable_blenderobject_name,cable_folder,'Collection')
    except:
        print('no matching CABLE found: ' + cable_blenderobject_name)


def append_cap(lamp):
    set_active_layer(lamp['collection']) 
    # Import Shade
    # print(lamp['cap']) 
    cap_material = lamp['cap_material']
    cap_id = lamp['cap'] 
    cap_folder = "caps/"
    #key = "%s-%s" % (shade_model,shade_material) 
    cap_blenderobject_name = "%s.%s" % (cap_id,cap_material) 
    #model, blenderobject_name, section, 
    try:
        append_from_blendfile(cap_id,cap_blenderobject_name,cap_folder,'Collection')
    except:
        print('no matching CAP found: ' + cap_blenderobject_name)

def append_hub(lamp):
    set_active_layer(lamp['collection']) 
    # Import Shade
    # print(lamp['hub']) 
    hub_material = lamp['hub_material']
    hub_id = lamp['hub'] 
    hub_folder = "hubs/"
    #key = "%s-%s" % (shade_model,shade_material) 
    hub_blenderobject_name = "%s.%s" % (hub_id,hub_material) 
    #model, blenderobject_name, section, 
    try:
        append_from_blendfile(hub_id,hub_blenderobject_name,hub_folder,'Collection')
    except:
        print('no matching HUB found: ' + hub_blenderobject_name)

def append_shade(lamp,light_state):

    set_active_layer(lamp['collection']) 
    # Import Shade
    # print(lamp['shade']) 
    shade_material = lamp['shade_material']
    shelf_id = lamp['shade'] 
    shade_folder = "shades/"
    #key = "%s-%s" % (shade_model,shade_material) 
    shade_blenderobject_name = "%s.%s.%s" % (shelf_id,shade_material,light_state) 
    #model, blenderobject_name, section, 
    try:
        append_from_blendfile(shelf_id,shade_blenderobject_name,shade_folder,'Collection')
    except:
        print('no matching SHADE found: ' + shade_blenderobject_name)

def append_from_blendfile(shelf_id,import_key,shade_folder,section):
    # select lamp collection 
    filepath = os.path.dirname(os.path.abspath(__file__))
    path, file_name = os.path.split(filepath)
    blend_filename = shelf_id+".blend"
    shades_folderpath = os.path.join(path, 'shelf/'+shade_folder)
    blendfile = os.path.join(shades_folderpath, blend_filename)
    section   = "\\"+section+"\\"
    filepath  = blendfile + section + import_key
    directory = blendfile + section
    filename  = import_key
    try:
        # old_obj_list = bpy.data.objects[:]
        bpy.ops.wm.append(filepath=filepath,filename=filename,directory=directory, autoselect=True, active_collection=True,link=False)
        # new_obj_list = bpy.data.objects[:] 
        # obj =  get_new_obj(old_obj_list,new_obj_list)
    except ValueError:
        print('No Object matching!') 

def hide_collection_from_render(name):
    bpy.data.collections[name].hide_render = True

def exclude_active_collection(name):
    set_active_layer(name)
    bpy.context.view_layer.active_layer_collection.exclude = True

def recurLayerCollection(layerColl, collName):
    found = None
    if (layerColl.name == collName):
        return layerColl
    for layer in layerColl.children:
        found = recurLayerCollection(layer, collName)
        if found:
            return found

def set_active_layer(name):
    layer_collection = bpy.context.view_layer.layer_collection
    layerColl = recurLayerCollection(layer_collection, name)
    bpy.context.view_layer.active_layer_collection = layerColl 

def get_new_obj(olist,nlist):
    lastobj = set(nlist) - set(olist)
    return lastobj

def deconstruct_all():
    print('destroy all')
    for obj in shelf:
        print(obj) 
        bpy.data.objects.remove(bpy.data.objects[obj])
        shelf.remove(obj)
