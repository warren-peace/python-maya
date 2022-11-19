'''
Program that disables the color of the joints: 
    Select joint. This program will disable the 
    override colors of the joint AND its children.

    Works on multiple selected joints.
'''

import maya.cmds as mc

selected = mc.ls(sl=True,long=True)
mc.select(clear=True)
for item in selected:
    # select first item
    mc.select(item,add=True) 
    # select every joint descendant
    l1 = mc.listRelatives(allDescendents=True, type='joint',f=True)
    # include selected joint in the list
    l1.append(item) 
    for list_item in l1:
        print(list_item)
        mc.setAttr(list_item + '.overrideEnabled', 0)
mc.select(clear=True)