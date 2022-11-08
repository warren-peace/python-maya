'''
The program:
	1. Highlights the missing joints in the REFERENCE
	2. Highlights the extra joints in the second skeleton
	3. prints the path of the highlights in the console

INSTRUCTIONS:
	Select the ROOT joint of the REFERENCE first
	then select the ROOT joint of the second skeleton. 
	Run script

Color Codes:
	RED: Joints in the REFERENCE missing in the second skeleton
	GREEN: Joints in the REFERENCE that might be misplaced in the second skeleton
	PINK: Joints that may be misplaced based on REFERENCE
	BLUE: Extra joints in the second skeleton
'''

# main part
compareJoints():
	# list selected joints
	selected = mc.ls(sl=True,long=True)

	# deselect everything and just select the first joint
	mc.select(clear=True)
	mc.select(selected[0],add=True)

	# select every joint descendant
	l2 = mc.listRelatives(allDescendents=True, type='joint',f=True)

# call main
compareJoints()