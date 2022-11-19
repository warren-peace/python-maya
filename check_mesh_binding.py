'''
    Checks if a mesh has joints belonging to different skeletons (root joints). Unreal considers FBX skinned to different skeletons as invalid.

    Instructions:
    1. Select the mesh.
    2. Run the script.

    Output:
    - Prints the name of the root joints
    - Colors the outline of the joints based on its root
'''

import maya.cmds as mc

# Functions start
def color_joint(the_joint, the_color):
    mc.setAttr(the_joint+'.overrideEnabled',1)
    mc.setAttr(the_joint+'.overrideColor', the_color)
    return
# Functions end

# Main start
# ---
# get selection
sel = mc.ls(sl=True)

# get list of joints the mesh is bound to
joints = mc.skinCluster(sel, inf = True, q = True)

roots_list = {}
ctr = 0
# get the root of each joint
for item in joints:
    # get full path for the joint and find its root
    sel  = mc.ls(item, l = True)[0].split('|')[1]
    if((sel in roots_list.keys()) == False):
        roots_list[sel] = ctr + 4
        ctr+=1
        # color the joint
        color_joint(item,roots_list[sel])
        
# Print the names of the roots
print('Root of all joints bound to the mesh:')
for item in roots_list.keys():
    print('\t'+item)

