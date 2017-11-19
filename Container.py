class Container:
	# The seed used in the current run
	seed = 0

	# Number of runs to be executed
	runs = 0
	# Number of Fitness Evaluations to be done
	fitness = 0

	# Length of Agent Memory
	k = 0
	# Tree Depth
	d = 0
	# Number of iterations to be played in a given evaluation
	l = 0
	# Tournament value
	parentNumber = 0
	# Number till termination
	n = 0
	# Mutation Rate
	mu = 0
	# Number of Generations
	generations = 0
	# Parsimony Pressure Coefficient
	p = 0
	# Number of evals before termination
	terminationEvals = 0
	# Holds the best fitness found for a given execution
	solution_fitness = 0

	# Holds the previous decision, starts with defect
	decision = 'defect'

	# Holds all log_lists which will be used to write to the result file
	results = []

	# Result Log File
	prob_log_file = 0
	# Solution File
	prob_solution_file = 0

	# Settings

	# Initialization
	Ramped = 0

	# parentSelection
	fitnessProportional = 0
	overSelection = 0

	# Recombination
	subTree_Crossover_Recombination = 0

	# Mutation
	subTree_Crossover_Mutation = 0

	# Survival Selection
	truncation = 0
	kTournament = 0

	# Control
	parsimonyPressure = 0

	# Termination
	numEvals = 0
	noChange = 0


