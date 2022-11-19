'''
    Checks if a mesh has joints belonging to different skeletons (root joints). Unreal considers FBX skinned to different skeletons as invalid.

    Instructions:
    1. Select the mesh.
    2. Run the script.
'''

import maya.cmds as mc

# get selection
sel = mc.ls(sl=True)

# get list of joints the mesh is bound to
joints = mc.skinCluster(sel, inf = True, q = True)

roots_list = []
# get the root of each joint
for item in joints:
    # root = item.split('|')[0]
    # print(root)
    # get full path for the joint and find its root
    sel  = mc.ls(item, l = True)[0].split('|')[1]
    print(sel)