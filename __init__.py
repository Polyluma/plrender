# import objects
import bpy
import sys
import os
import json
from time import sleep
sys.path.append('plrender/')

import objects
import render
import importlib
importlib.reload(objects)
#importlib.reload(render)


def run():
    print('READ JSON') 
    job = read_json()
    # print(job)

    # if job is not {} and None:
    print('BUILD') 
    objects.construct(job)
    print('RENDER') 
    render.start(job)


def read_json():
    filepath = os.path.dirname(os.path.abspath(__file__))
    path, file_name = os.path.split(filepath)
    rqueue_filename = "job.json"

    rqueue_folderpath = os.path.join(path)
    rqueue_path = os.path.join(rqueue_folderpath, rqueue_filename)

    try:
        with open(rqueue_path) as json_data:
            jdata = json.load(json_data)
    except:
        jdata = {}
        print("No Job file found!")

    return jdata