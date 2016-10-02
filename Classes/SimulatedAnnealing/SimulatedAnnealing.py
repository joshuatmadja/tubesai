import copy
import math
import random
from ..Jadwal import Jadwal
from ..Matriks import Matriks
from ..Assign import Assign

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
	def search_ruang_constraint(cls, code, idx_ruang, day_selected):
		room = Jadwal.daftar_ruangan[idx_ruang]
		ans = (room.hari[day_selected] - 1) * 24
		if code == 0:
			ans += room.jam_awal  # constraint jam awal
		else:
			ans += room.jam_akhir # constraint jam akhir
		return ans

	# Return boolean value
	@classmethod
	def check_matkul_constraint(cls, matkul_selected, r_selected, w_selected):
		banyak_hari = len(matkul_selected.hari)
		for idx_hari in range(banyak_hari):
			batas_waktu_awal = (matkul_selected.hari[idx_hari] - 1) * 24 + matkul_selected.jam_awal
			batas_waktu_akhir = batas_waktu_awal + matkul_selected.sks #tambah sks
			if (w_selected >= batas_waktu_awal and w_selected <= batas_waktu_akhir and r_selected == matkul_selected.ruangan):
				return True
		return False

	@classmethod
	def moveMatkul(cls, matrix, list_idx, idx_matkul, ruang_awal, waktu_awal, ruang_akhir, waktu_akhir):
		SKS = Jadwal.daftar_matkul_time[idx_matkul].sks

		nama_matkul = Jadwal.daftar_mata_kuliah[idx_matkul].nama
		# delete matkul dari yang lama
		for idx_waktu in range(waktu_awal, waktu_awal + SKS):
			banyak_matkul_di_slot = len(matrix.matriks[ruang_awal][idx_waktu])
			for j in range(banyak_matkul_di_slot):
				if matrix.matriks[ruang_awal][idx_waktu][j].nama == nama_matkul:
					del matrix.matriks[ruang_awal][idx_waktu][j]
					break

		# insert matkul ke yang baru
		for idx_waktu in range(waktu_akhir, waktu_akhir + SKS):
			kuliah = copy.deepcopy(Jadwal.daftar_mata_kuliah[idx_matkul])
			matrix.matriks[ruang_akhir][idx_waktu].append(kuliah)

		# masukin ke list_idx
		list_idx[idx_matkul] = (ruang_akhir, waktu_akhir)

	@classmethod
	def climbing(cls, matrix, list_idx):
		# MAIN ALGORITHM
		# STEP 2 - Conflict checking & solving
		# cek muter
		roundtrip = 0
		found = False
		while (roundtrip != 2 and (not found)):
			for idx_matkul in range(len(list_idx)):
				ruang_awal, waktu_awal = list_idx[idx_matkul] # extract the tuple
				if (len(matrix.matriks[ruang_awal][waktu_awal]) > 1):
					list_temp = matrix.matriks[ruang_awal][waktu_awal]

					# nyari matkul yang mau diubah
					conflicted_matkul = None
					nama_matkul = Jadwal.daftar_mata_kuliah[idx_matkul].nama
					for i in range(len(list_temp)):
						if list_temp[i].nama == nama_matkul:
							conflicted_matkul = copy.deepcopy(Jadwal.daftar_mata_kuliah[idx_matkul])

					# nyari ruangan yang bisa diubah
					nRoom = len(Jadwal.daftar_ruangan)
					for idx_room in range(nRoom):
						# Constraint slot waktu di matrix sesuai constraint ruangan
						nDay = len(Jadwal.daftar_ruangan[idx_room].hari)
						for idx_day in range(nDay):
							# convert ke jam basis 120
							jam_converted_start = cls.search_ruang_constraint(0, idx_room, idx_day)
							jam_converted_end 	= cls.search_ruang_constraint(1, idx_room, idx_day)

							# looping terhadap jam yang available, basis 120
							for idx_waktu_start in range(jam_converted_start, jam_converted_end):
								# ngecek apakah dia udah diisi atau yang dia pilih itu pernah dipilih sebelumnya
								if (len(matrix.matriks[idx_room][idx_waktu_start]) > 0 or (idx_room == ruang_awal and idx_waktu_start == waktu_awal)):
									# Search to next slot time
									continue
								else:
									# Check if the slot time match with matkul constraint
									time_and_space_matchs = cls.check_matkul_constraint(conflicted_matkul, idx_room, idx_waktu_start)
									if (time_and_space_matchs): # Found the slot
										found = True
										cls.moveMatkul(matrix, list_idx, idx_matkul, ruang_awal, waktu_awal, idx_room, idx_waktu_start)
								if found:
									break
						if found:
							break
					if found:
						break
			if not found:
				roundtrip += 1

	@classmethod
	def insert_jadwal_into_matriks(cls):
		cls.current_solution = Matriks(len(Jadwal.daftar_ruangan), 120)
		nMatKul = len(Jadwal.daftar_mata_kuliah)
		for i in range(nMatKul):
			ruang = Assign.daftar_matkul_time[i].r_selected
			waktu = (Assign.daftar_matkul_time[i].h_selected - 1) * 24 + Assign.daftar_matkul_time[i].j_selected
			kuliah = copy.deepcopy(Jadwal.daftar_mata_kuliah[i]) # biar bikin object baru
			SKS = Assign.daftar_matkul_time[i].sks
			for j in range(waktu, waktu + SKS):
				cls.current_solution.matriks[ruang][j].append(kuliah)

		# copy yang pertama banget
		cls.least_conflict = cls.current_solution.conflict_count()

	@classmethod
	def first_initiate(cls):
		# STEP 1 - Take MatkulOnlyTime data (list) of Course
		# convert to index by formula (dari Jadwal.daftar_matkul_time)
		cls.current_list_idx = []
		nMatKul = len(Jadwal.daftar_mata_kuliah)
		for i in range(nMatKul):
			ruang = Assign.daftar_matkul_time[i].r_selected
			waktu = (Assign.daftar_matkul_time[i].h_selected - 1) * 24 + Assign.daftar_matkul_time[i].j_selected
			temp = (ruang, waktu)
			cls.current_list_idx.append(temp)

	@classmethod
	def init(cls):
		cls.first_initiate()
		cls.insert_jadwal_into_matriks()

	@classmethod
	def calculate(cls):
		# Looping - simulated annealing main point
		list_idx = copy.deepcopy(cls.current_list_idx)
		temperature = cls.temperature
		cooling_rate = cls.cooling_rate

		while temperature > 1 and cls.least_conflict > 0:
			# Create new Matriks for swapping & conflict_count comparison
			new_solution = copy.deepcopy(cls.current_solution)
			## Swap to create variant - nunggu respon Denden biar sama

			cls.climbing(new_solution, list_idx)
			new_conflict = new_solution.conflict_count()
			# Decide & keep best solution
			if (cls.acceptance_function(cls.least_conflict, new_conflict, temperature) >= random.randrange(0, 1)):
				cls.current_solution = new_solution
				least_conflict = new_conflict
				cls.current_list_idx = copy.deepcopy(list_idx)

			# Cooling
			temperature *= (1 - cooling_rate)

	@classmethod
	def finishing(cls):
		cls.matrix_hasil = Matriks(len(Jadwal.daftar_ruangan), 120)
		nRoom = len(Jadwal.daftar_ruangan)
		for idx_room in range(nRoom):
			for idx_waktu in range(120):
				for matkul in cls.current_solution.matriks[idx_room][idx_waktu]:
					cls.matrix_hasil.matriks[idx_room][idx_waktu].append(copy.deepcopy(matkul.nama))

	@classmethod
	def __init__(cls):
		# Initiate temperature & cooling rate
		cls.temperature = 1000
		cls.cooling_rate = 0.03
		cls.list_idx_cur = []
		# Initiate Matriks - complete assignment
		cls.current_solution = Matriks(len(Jadwal.daftar_ruangan), 120)
		cls.least_conflict = cls.current_solution.conflict_count()
