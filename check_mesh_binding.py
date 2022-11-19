'''
    Checks if a mesh has joints belonging to different skeletons (root joints). Unreal considers FBX skinned to different skeletons as invalid.

    Instructions:
    1. Select the mesh.
    2. Run the script.
'''

import maya.cmds as mc

# get selection
sel = mc.ls(sl=True)

joints = mc.skinCluster(sel, inf = True, q = True)

for item in joints:
    print(item)