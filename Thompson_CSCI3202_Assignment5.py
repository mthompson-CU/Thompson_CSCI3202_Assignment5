# Author: Matthew Thompson
# 102343355
# CSCI 3202
# Assignment 5

import sys
import MDPNode
import MDP

# Imports the world from a text world file
def importWorld(world):
	worldFile = open(world, 'rb')
	world = []
	for line in worldFile:
		line = line.split()
		world.append(line)
	worldFile.close()

	# Remove blank line at end of file
	world.pop()

	# Transform array into an array of MDPNodes
	for x in range(len(world)):
		for y in range(len(world[0])):
			world[x][y] = MDPNode.MDPNode(x, y, int(world[x][y]))

	return world

def main(argv):
	# Ensure proper number of inputs
	if (len(argv) != 3):
		print 'Usage: python Thompson_CSCI3202_Assignment5.py <world file> <epsilon>'
		return

	# Read in world map
	world = importWorld(argv[1])

	# Create the MDP from the world
	mdp = MDP.MDP(world, float(argv[2]), 0.9)

	# Print the solution to the maze
	mdp.solveMaze()

	return

if __name__ == "__main__":
	main(sys.argv)