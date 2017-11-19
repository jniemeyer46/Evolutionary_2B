from copy import deepcopy
import random

from Container import Container
from Tree import Tree


def createTree(depth, memoryLength):
	funcNodes = ['AND', 'OR', 'NOT', 'XOR']
	agents = ['P', 'O']
	tree_list = []

	# Initialize a tree
	tree = Tree()

	if depth == 1:
		# Obtain the two things needed to make a leaf
		agent = random.choice(agents)
		num = random.randrange(1, (memoryLength + 1))

		# The termination node created
		leaf = agent + str(num)

		# Set the value equal to the created leaf
		tree.add(leaf)
		tree_list.append(leaf)
	else:
		for level in range(depth):
			if level == 0:
				value = random.choice(funcNodes)

				tree.add(value)
				tree_list.append(value)
			elif level is not (depth - 1):
				for node in range(2 ** level):
					value = random.choice(funcNodes)

					tree.add(value)
					tree_list.append(value)
			else:
				for node in range(2 ** level):
					agent = random.choice(agents)
					num = random.randrange(1, (memoryLength + 1))

					leaf = agent + str(num)

					tree.add(leaf)
					tree_list.append(leaf)

	return tree, tree_list


# Make the list a preorder the list
def reorder(depth, list):
	count = 0
	num = 0
	# Holds the position of the element we want to move
	position = (2**(depth - 1) - 1)

	# We don't need to worry about these two trees
	if depth == 1 or depth == 2:
		return list
	# Worry about the rest
	else:
		# If the depth is 3 then we move the elements 1 back
		if depth == 3:
			count = 2
		# Otherwise we move the elements back by a power of 2 (in terms of the loop)
		else:
			num = depth - 2
			count += 2**num

		for level in reversed(range(count)):
			for i in range(0, 2):
				x = list[position]
				del list[position]
				list.insert(position - level, x)
				position += 1	

	return list


def evaluate(memory, memoryLength, tree):
	# Holds a tree that I can change
	temp = deepcopy(tree)

	# Go through the list backwards
	for loc in reversed(range(len(temp))):
		# Determine whether it is a leaf node or not
		if temp[loc][1:].isdigit():
			# Location of the memory spot
			memoryLocation = memoryLength - int(temp[loc][1:])

			# Unpacking the memory tuple
			x, y = memory[memoryLocation]

			# If the leaf has a P in it use the x position, else use the y
			if temp[loc][0] == 'P':
				temp[loc] = x
			elif temp[loc][0] == 'O':
				temp[loc] = y
		else:
			# If the locations to the right of temp have been evaluated already
			if temp[loc+1] == 0 or temp[loc+1] == 1:
				if temp[loc] == 'NOT':
					if temp[loc+1] >= temp[loc+2]:
						t = temp[loc+1] - temp[loc+2]
					else:
						t = temp[loc+2] - temp[loc+1]

					# Does the flipping of the bit
					if t == 1:
						t = 0
					else:
						t = 1


					# Gets rid of the completely evaluated locations
					del temp[loc + 2]
					del temp[loc + 1]

					temp[loc] = t
				elif temp[loc] == 'AND':
					# Determines whether it should be a 1 or a zero
					if temp[loc+1] == 1 and temp[loc+2] == 1:
						t = 1
					else:
						t = 0

					# Gets rid of the completely evaluated locations
					del temp[loc + 2]
					del temp[loc + 1]

					temp[loc] = t
				if temp[loc] == 'OR':
					# Determines whether it should be a 1 or a zero
					if temp[loc+1] == 1 or temp[loc+2] == 1:
						t = 1
					else:
						t = 0

					# Gets rid of the completely evaluated locations
					del temp[loc + 2]
					del temp[loc + 1]

					temp[loc] = t
				if temp[loc] == 'XOR':
					# Determines whether it should be a 1 or a zero
					if temp[loc+1] == 1 and temp[loc+2] == 0:
						t = 1
					elif temp[loc+1] == 0 and temp[loc+2] == 1:
						t = 1
					else:
						t = 0

					# Gets rid of the completely evaluated locations
					del temp[loc + 2]
					del temp[loc + 1]

					temp[loc] = t

	# Determines whether the agent cooperates or defects based on the tree evaluation
	if temp[0] == 1:
		return 'cooperate'
	elif temp[0] == 0:
		return 'defect'


def yearsInJail(decisionP, decisionO):
	fitnessP = 0
	fitnessO = 0

	# If they both cooperate, they get 2 years in jail, 3 fitness point
	if decisionP == decisionO and decisionP == 'cooperate':
		fitnessP += 3
		fitnessO += 3
	# If they both defect, they get 4 years in jail, 1 fitness point
	elif decisionP == decisionO and decisionP == 'defect':
		fitnessP += 1
		fitnessO += 1
	# If they both defect, they get 4 years in jail, 1 fitness point
	elif decisionP == 'cooperate' and decisionO == 'defect':
		fitnessP += 0
		fitnessO += 5
	# If they both defect, they get 4 years in jail, 1 fitness point
	elif decisionP == 'defect' and decisionO == 'cooperate':
		fitnessP += 5
		fitnessO += 0

	return fitnessP, fitnessO


def noChange(fitnessList, n):
	terminate = False
	count = 0

	fitness = fitnessList[len(fitnessList) - 1]

	for i in reversed(fitnessList):
		if i is fitness:
			count += 1

			if count == n:
				terminate = True
				break

	return terminate


def fitnessProportional(parents, parentFitness, numParents):
	listParents = []
	listParentFitness = []

	for i in range(len(parentFitness)):
		if len(listParents) < numParents:
			listParents.append(parents[i])
			listParentFitness.append(parentFitness[i])
		else:
			for loc in range(len(listParentFitness)):
				if listParentFitness[loc] < parentFitness[i]:
					listParentFitness[loc] = parentFitness[i]
					listParents[loc] = parents[i]

	return listParents, listParentFitness


def OverSelection(parents, parentFitness, numParents):
	listParents = []
	listParentFitness = []

	for i in range(len(parentFitness)):
		if len(listParents) < (numParents*2):
			listParents.append(parents[i])
			listParentFitness.append(parentFitness[i])
		else:
			for loc in range(len(listParentFitness)):
				if listParentFitness[loc] < parentFitness[i]:
					listParentFitness[loc] = parentFitness[i]
					listParents[loc] = parents[i]

	return listParents, listParentFitness


def Recombination(parents):
	p1 = random.choice(parents)
	p2 = random.choice(parents)

	# determine the amout of genes used from parent 1... the rest from parent 2
	amount_parent1_genes = random.randrange(0, len(p1))

	tree_list = p1[0:amount_parent1_genes] + p2[amount_parent1_genes:]

	return tree_list


def mutate(tree_list, memoryLength):
	funcNodes = ['AND', 'OR', 'NOT', 'XOR']
	agents = ['P', 'O']

	for i in range(len(tree_list)):
		if tree_list[i] in funcNodes:
			tree_list[i] = random.choice(funcNodes)
		else:
			# Obtain the two things needed to make a leaf
			agent = random.choice(agents)
			num = random.randrange(1, (memoryLength - 1))

			# The termination node created
			leaf = agent + str(num)

			tree_list[i] = leaf


def Truncation(currentParents, currentParentFitness, parentNumber):
	currentParents = currentParents[0:parentNumber]
	currentParentFitness = currentParentFitness[0:parentNumber]

	return currentParents, currentParentFitness


def kTournament(currentParents, currentParentFitness, parentNumber):
	offspring = []
	offspring_fitness = []

	for num in range(0, parentNumber):
		highest_index = 0

		tournament_pool, tournament_fitness_pool = deepcopy(createOffspringTourney(currentParents, currentParentFitness, parentNumber))

		for index in range(0, len(tournament_fitness_pool)):
			if tournament_fitness_pool[index] > tournament_fitness_pool[highest_index] and index < len(currentParents):
				highest_index = index

		offspring.append(currentParents[highest_index])
		del currentParents[highest_index]
		offspring_fitness.append(currentParentFitness[highest_index])
		del currentParentFitness[highest_index]

	return offspring, offspring_fitness


def createOffspringTourney(currentParents, currentParentFitness, parentNumber):
	Tourney_participants = []
	Tourney_participants_fitness_values = []

	for i in range(0, parentNumber):
		rand_location = random.randrange(0, len(currentParents))
		Tourney_participants.append(currentParents[rand_location])
		Tourney_participants_fitness_values.append(currentParentFitness[rand_location])

	return Tourney_participants, Tourney_participants_fitness_values
		











