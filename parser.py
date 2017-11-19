import string
import time

def setup(container, config):
	# setting up variables using config file
	for rules in config:
		# split the rules into words
		info = rules.split(" ")

		if info[0] == "runs":
			container.runs = int(info[2])
		elif info[0] == "fitness":
			container.fitness = int(info[2])
		elif info[0] == "k":
			container.k = int(info[2])
		elif info[0] == "d":
			container.d = int(info[2])
		elif info[0] == "l":
			container.l = int(info[2])
		elif info[0] == "parentNumber":
			container.parentNumber = int(info[2])
		elif info[0] == "n":
			container.n = int(info[2])
		elif info[0] == "mu":
			container.mu = float(info[2])
		elif info[0] == "lambda":
			container.generations = int(info[2])
		elif info[0] == "p":
			container.p = int(info[2])
		elif info[0] == "terminationEvals":
			container.terminationEvals = int(info[2])
		elif info[0] == "prob_log_file":
			container.prob_log_file = info[2]
		elif info[0] == "prob_solution_file":
			container.prob_solution_file = info[2]
		elif info[0] == "Initialize:":
			if info[1] == "Ramped_halfandhalf" and info[3] == '1':
				container.Ramped = 1
		elif info[0] == "parentSelection:":
			if info[1] == "Fitness_Proportional_Selection" and info[3] == '1,':
				container.fitnessProportional = 1
			elif info[4] == "Over_Selection" and info[6] == '1':
				container.overSelection = 1
		elif info[0] == "Recombination:":
			if info[1] == "subTree_Crossover_Recombination" and info[3] == '1':
				container.subTree_Crossover_Recombination = 1
		elif info[0] == "Mutation:":
			if info[1] == "subTree_Crossover_Mutation" and info[3] == '1':
				container.subTree_Crossover_Mutation = 1
		elif info[0] == "survivalSelection:":
			if info[1] == "Truncation" and info[3] == '1,':
				container.truncation = 1
			elif info[4] == "kTournament" and info[6] == '1':
				container.kTournament = 1
		elif info[0] == "bloatControl:":
			if info[1] == "parsimonyPressure" and info[3] == '1':
				container.parsimonyPressure = 1
		elif info[0] == "Termination:":
			if info[1] == "numEvals" and info[3] == '1,':
				container.numEvals = 1
			elif info[4] == "noChange" and info[6] == '1':
				container.noChange = 1
		elif info[0] == "newSeed":
			if info[2] == '1':
				container.seed = time.time()
				break
			else:
				obtained_seed = open(container.prob_log_file).read().splitlines(2)
				for lines in obtained_seed:
					line = lines.split(" ")
					if line[0] == "Random":
						container.seed = line[3]
						break
