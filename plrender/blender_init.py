import bpy
import sys
import os

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )

import plrender
import importlib
importlib.reload(plrender)


#Check if headless
args = sys.argv[2] if len(sys.argv) >= 3 else None

if str(args) is args == '-b':
    print(args)
    print('Headless')
    plrender.run()
else:
    print(args)
    print('GUI')
    
