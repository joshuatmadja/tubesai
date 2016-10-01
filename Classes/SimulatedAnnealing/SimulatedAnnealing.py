import copy
import math
import random
from ..Matriks import Matriks
class SimulatedAnnealing:

	# Acceptance function, energy represent conflict_count
	@classmethod
	def acceptance_function(cls, current_energy, new_energy, temperature):
		if (new_energy <= current_energy):
			return 1
		else:
			return math.exp((current_energy - new_energy) / temperature)

	@classmethod
	def calculate(cls):
		# Looping - simulated annealing main point
		while temperature > 1 and least_conflict > 0:
			# Create new Matriks for swapping & conflict_count comparison
			new_solution = copy.deepcopy(current_solution)
			## Swap to create variant - nunggu respon Denden biar sama
			new_conflict = new_solution.conflict_count()

			# Decide & keep best solution
			if (cls.acceptance_function(least_conflict, new_conflict, temperature) >= random.randrange(0, 1)):
				current_solution = new_solution
				least_conflict = new_conflict

			# Cooling
			temperature *= (1 - cooling_rate)

	@classmethod
	def __init__(cls):
		# Initiate temperature & cooling rate
		cls.temperature = 1000
		cls.cooling_rate = 0.03

		# Initiate Matriks - complete assignment
		cls.current_solution = Matriks()
		cls.least_conflict = current_solution.conflict_count()
