# Author: Matthew Thompson
# 102343355
# Implements a node for a MDP search
# Origin for x and y coordinates is the bottom left corner of the graph

class MDPNode():
	def __init__(self, x, y, mapValue):
		self.x = x
		self.y = y
		self.mapValue = mapValue
		if (mapValue == 0):
			self.reward = 0
			self.utility = 0
		elif (mapValue == 1):
			self.reward = -1
			self.utility = 0
		elif (mapValue == 2):
			self.reward = 0
			self.utility = 0
		elif (mapValue == 3):
			self.reward = -2
			self.utility = 0
		elif (mapValue == 4):
			self.reward = 1
			self.utility = 0
		elif (mapValue == 50):
			self.reward = 50
			self.utility = 50

