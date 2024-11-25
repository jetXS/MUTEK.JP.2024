# The function below is called when any passed values have changed.
# Be sure to turn on the related parameter in the DAT to retrieve these values.
#
# me - this DAT
# renderPickDat - the connected Render Pick DAT
#
# events - a list of named tuples with the fields listed below.
# eventsPrev - a list of events holding the eventsPrev values.
#
#	u				- The selection u coordinate.			(float)
#	v				- The selection v coordinate.			(float)
#	select			- True when a selection is ongoing.		(bool)
#	selectStart		- True at the start of a selection.		(bool)
#	selectEnd		- True at the end of a selection.		(bool)
#	selectedOp		- First picked operator.				(OP)
#	selectedTexture	- Texture coordinate of selectedOp.		(Position)
#	pickOp			- Currently picked operator.			(OP)
#	pos				- 3D position of picked point.			(Position)
#	texture			- Texture coordinate of picked point.	(Position)
#	color			- Color of picked point.				(4-tuple)
#	normal			- Geometry normal of picked point.		(Vector)
#	depth			- Post projection space depth.			(float)
#	instanceId		- Instance ID of the object.			(int)
#	row				- The row associated with this event	(float)
#	inValues		- Dictionary of input DAT strings for the given row, where keys are column headers. (dict)
#	custom	 		- Dictionary of selected custom attributes

import random

def onEvents(renderPickDat, events, eventsPrev):

	for event, eventPrev in zip(events, eventsPrev):
		#insert code for event, eventsPrev here
		if event.selectStart and event.pickOp:
			parentCOMP = event.pickOp.parent()
			
			if parentCOMP.OPType == 'geometryCOMP':
				myMat = parentCOMP.par.material.eval()

				if myMat and myMat.OPType == 'pbrMAT':
					baseColor = myMat.parGroup.basecolor # parGroup
					baseColor.val = (random.random(), random.random(), random.random())
		
	return

	