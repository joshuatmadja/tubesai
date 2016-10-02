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

	# pindahkan jadwal suatu mata kuliah
	@classmethod
	def moveMatkul(cls, idx_matkul, ruang_awal, waktu_awal, ruang_akhir, waktu_akhir):
		SKS = Jadwal.daftar_matkul_time[idx_matkul].sks

		nama_matkul = Jadwal.daftar_mata_kuliah[idx_matkul].nama
		# delete matkul dari yang lama
		for idx_waktu in range(waktu_awal, waktu_awal + SKS):
			banyak_matkul_di_slot = len(cls.matrix.matriks[ruang_awal][idx_waktu])
			for j in range(banyak_matkul_di_slot):
				if cls.matrix.matriks[ruang_awal][idx_waktu][j].nama == nama_matkul:
					del cls.matrix.matriks[ruang_awal][idx_waktu][j]
					break

		# insert matkul ke yang baru
		for idx_waktu in range(waktu_akhir, waktu_akhir + SKS):
			kuliah = copy.deepcopy(Jadwal.daftar_mata_kuliah[idx_matkul])
			cls.matrix.matriks[ruang_akhir][idx_waktu].append(kuliah)

		# masukin ke list_idx
		cls.list_idx[idx_matkul] = (ruang_akhir, waktu_akhir)

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

		cls.list_idx = []
		cls.list_idx_best = []
		# Initiate Matriks - complete assignment
		cls.current_solution = Matriks(len(Jadwal.daftar_ruangan), 120)
		cls.least_conflict = current_solution.conflict_count()
