import copy
import math
import random
from .Matriks import Matriks

class SimulatedAnnealing:
	
	# Acceptance function, energy represent conflict_count
	def acceptance_function(self, current_energy, new_energy, temperature):
		if (new_energy < current_energy):
			return 1
		else:
			return math.exp((current_energy - new_energy) / temperature)

	def calculate(self)

		# Looping - simulated annealing main point
		while temperature > 1 and least_conflict > 0:
			# Create new Matriks for swapping & conflict_count comparison
			new_solution = copy.deepcopy(current_solution)
			## Swap to create variant - nunggu respon Denden biar sama
			new_conflict = new_solution.conflict_count()
			
			# Decide & keep best solution
			if (self.acceptance_function(least_conflict, new_conflict, temperature) >= random.randrange(0, 1)):
				current_solution = new_solution
				least_conflict = new_conflict
			
			# Cooling
			temperature *= 1 - cooling_rate

	def __init__(self, temperature, cooling_rate, current_solution, least_conflict):
		# Initiate temperature & cooling rate
		self.temperature = 1000
		self.cooling_rate = 0.03
		# Initiate Matriks - complete assignment
		self.current_solution = Matriks()
		self.least_conflict = current_solution.conflict_count()

