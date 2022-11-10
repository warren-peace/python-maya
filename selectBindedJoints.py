import maya.cmds as mc

sel = mc.ls(sl = True)

jnts = mc.skinCluster(sel, inf = True, q = True)

mc.select(jnts)