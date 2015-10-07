# Author: Matthew Thompson
# 102343355
# Implements a Markov Decision Process

import sys

class MDP():
	def __init__(self, world, epsilon, discount):
		self.world = world
		self.epsilon = epsilon
		self.discount = discount

	def updateUtilities(self):
		# Initialize delta to a large value to enter loop
		delta = sys.maxint

		while (delta >= (self.epsilon * (1.0 - self.discount) / self.discount)):
			delta = 0
			for x in range(len(self.world)):
				for y in range(len(self.world[0])):
					currentNode = self.world[x][y]

					# Get the adjacent nodes, checking to make sure the node is in bounds
					if ((x + 1) > len(self.world) - 1 or self.world[x + 1][y].utility == 0):
						aboveNode = currentNode
					else:
						aboveNode = self.world[x + 1][y]

					if ((x - 1) < 0 or self.world[x - 1][y].utility == 0):
						belowNode = currentNode
					else:
						belowNode = self.world[x - 1][y]

					if ((y + 1) > len(self.world[0]) - 1 or self.world[x][y + 1].utility == 0):
						rightNode = currentNode
					else:
						rightNode = self.world[x][y + 1]

					if ((y - 1) < 0 or self.world[x][y - 1].utility == 0):
						leftNode = currentNode
					else:
						leftNode = self.world[x][y - 1]

					# Determine the expected utilities of each neighbor
					aboveExpectedUtility = 0.8 * aboveNode.utility + 0.1 * leftNode.utility + 0.1 * rightNode.utility
					belowExpectedUtility = 0.8 * belowNode.utility + 0.1 * leftNode.utility + 0.1 * rightNode.utility
					rightExpectedUtility = 0.8 * rightNode.utility + 0.1 * aboveNode.utility + 0.1 * belowNode.utility
					leftExpectedUtility = 0.8 * leftNode.utility + 0.1 * aboveNode.utility + 0.1 * belowNode.utility
					
					previousUtility = currentNode.utility

					# Determine the new current utility
					currentNode.utility = currentNode.reward + self.discount * max(aboveExpectedUtility, belowExpectedUtility, rightExpectedUtility, leftExpectedUtility)

					# Update delta
					if (abs(previousUtility - currentNode.utility) > delta):
						delta = abs(previousUtility - currentNode.utility)


	def solveMaze(self):
		# Initialize the current loation to the bottom left corner
		currentNode = self.world[len(self.world) - 1][0]

		maxloop = 0
		# Loop until exit is reached
		while (currentNode.reward != 50):
			# Print current location and utility
			print 'Current location (x, y): ' + str(currentNode.x) + ',' + str(currentNode.y)
			print 'Current utility: ' + str(currentNode.utility)

			# Get the adjacent nodes, checking to make sure the node is in bounds
			if ((currentNode.x + 1) > len(self.world) - 1):
				aboveNode = currentNode
			else:
				aboveNode = self.world[currentNode.x + 1][currentNode.y]

			if ((currentNode.x - 1) < 0):
				belowNode = currentNode
			else:
				belowNode = self.world[currentNode.x - 1][currentNode.y]

			if ((currentNode.y + 1) > len(self.world[0]) - 1):
				rightNode = currentNode
			else:
				rightNode = self.world[currentNode.x][currentNode.y + 1]

			if ((currentNode.y - 1) < 0):
				leftNode = currentNode
			else:
				leftNode = self.world[currentNode.x][currentNode.y - 1]

			# Find maximum of adjacent utilites and set the new current node
			maximumUtility = max(aboveNode.utility, belowNode.utility, rightNode.utility, leftNode.utility)

			if (maximumUtility == aboveNode.utility):
				print 'Update to above'
				currentNode = aboveNode
			elif (maximumUtility == belowNode.utility):
				print 'Update to below'
				currentNode = belowNode
			elif (maximumUtility == rightNode.utility):
				print 'Update to right'
				currentNode = rightNode
			elif (maximumUtility == leftNode.utility):
				print 'Update to left'
				currentNode = leftNode
			else:
				print 'Hit wall'

			self.updateUtilities()

			maxloop+=1
			if (maxloop == 20):
				break

		# Print the final location and utility
		print 'Final location (x, y): ' + str(currentNode.x) + ',' + str(currentNode.y)
		print 'Final utility: ' + str(currentNode.utility)








