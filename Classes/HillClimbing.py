import copy
from random import randint
from .Matriks import Matriks
from .Jadwal import Jadwal
from .Assign import Assign

# rooms itu punya form, ini pake jadwal dulu biar sama. roomsnya diganti Jadwal.daftar_ruangan
class HillClimbing:
	# global variable
	matrix_hasil = []
	# Calculate index x and y value from selected slot
	# code = 0 means beginning idx x
	# code = 1 means end idx x
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

			# Check idx x (start and end), fulfill the constraint or not
			# If selected slot x fulfill the constraint, continue the check.
			# If not, end the looping, move check next matkul (conflicted or not)
			batas_waktu_awal = (matkul_selected.hari[idx_hari] - 1) * 24 + matkul_selected.jam_awal
			batas_waktu_akhir = batas_waktu_awal + matkul_selected.sks #tambah sks
			if (w_selected < batas_waktu_awal or w_selected > batas_waktu_akhir):
				continue

			# If idx x fulfill the constraint, check room constraint
			# Check if slot idx y fulfill the constraint

			# assumption : len(matkul_selected.ruangan) == 1
			if(r_selected == maktul_selected.ruangan):
				return True

#			# assumption : len(matkul_selected.ruangan) > 1
#			for idx_hari in range(len(matkul_selected.ruangan)):
#				if (y == matkul_selected.ruangan[idx_hari]):
#					return 1
#					break
		return False
		# 0 means false, 1 means true



	@classmethod
	def insert_jadwal_into_matriks(cls):
		nMatKul = len(Jadwal.daftar_mata_kuliah)
		for i in range(nMatKul):
			ruang = Assign.daftar_matkul_time[i].r_selected
			waktu = (Assign.daftar_matkul_time[i].h_selected - 1) * 24 + Assign.daftar_matkul_time[i].j_selected
			kuliah = copy.deepcopy(Jadwal.daftar_mata_kuliah[i]) # biar bikin object baru
			cls.matrix[ruang][waktu].append(kuliah)

		# copy yang pertama banget
		cls.matrix_best = copy.deepcopy(cls.matrix)
	@classmethod
	def first_initiate(cls):
		# STEP 1 - Take MatkulOnlyTime data (list) of Course
		# convert to index by formula (dari Jadwal.daftar_matkul_time)
		nMatKul = len(Jadwal.daftar_mata_kuliah)
		for i in range(nMatKul):
			ruang = Assign.daftar_matkul_time[i].r_selected
			waktu = (Assign.daftar_matkul_time[i].h_selected - 1) * 24 + Assign.daftar_matkul_time[i].j_selected
			temp = (ruang, waktu)
			cls.list_idx.append(temp)

		cls.list_idx_best = copy.deepcopy(cls.list_idx)
	# pindahkan jadwal suatu mata kuliah
	@classmethod
	def moveMatkul(cls, idx_matkul, ruang_awal, waktu_awal, ruang_akhir, waktu_akhir):
		SKS = Jadwal.daftar_matkul_time[idx_matkul].sks

		nama_matkul = Jadwal.daftar_mata_kuliah[idx_matkul].nama
		# delete matkul dari yang lama
		for idx_waktu in range(waktu_awal, waktu_awal + SKS):
			banyak_matkul_di_slot = len(cls.matrix[ruang_awal][idx_waktu])
			for j in range(banyak_matkul_di_slot):
				if cls.matrix[ruang_awal][idx_waktu][j].nama == nama_matkul:
					del cls.matrix[ruang_awal][idx_waktu][j]
					break

		# insert matkul ke yang baru
		for idx_waktu in range(waktu_akhir, waktu_akhir + SKS):
			kuliah = copy.deepcopy(Jadwal.daftar_mata_kuliah[idx_matkul])
			cls.matrix[ruang_akhir][idx_waktu].append(kuliah)

		# masukin ke list_idx
		cls.list_idx[idx_matkul] = (ruang_akhir, waktu_akhir)

	@classmethod
	def calculate(cls):
		cnt = 0
		while cnt < 10:

			# kalo ketemu yang lebih bagus, dicopy semua
			if (cls.next_conflict < cls.curr_conflict):
				cls.curr_conflict = cls.next_conflict
				cls.matrix_best = copy.deepcopy(cls.matrix)
				cls.list_idx_best = copy.deepcopy(cls.list_idx)

			# MAIN ALGORITHM
			# STEP 2 - Conflict checking & solving
			# cek muter
			roundtrip = 0
			found = False
			while (roundtrip != 2 and (not found)):
				for idx_matkul in range(len(cls.list_idx)):
					ruang_awal, waktu_awal = cls.list_idx[idx_matkul] # extract the tuple

					if (len(cls.matrix[ruang_awal][waktu_awal]) > 1):
						list_temp = cls.matrix[ruang_awal][waktu_awal]

						# nyari matkul yang mau diubah
						conflicted_matkul = []
						nama_matkul = Jadwal.daftar_mata_kuliah[idx_matkul]
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
								jam_converted_start = cls.search_ruang_constraint(0, idx, idx_day)
								jam_converted_end 	= cls.search_ruang_constraint(1, idx, idx_day)

								# looping terhadap jam yang available, basis 120
								for idx_waktu_start in range(jam_converted_start, jam_converted_end):
									# ngecek apakah dia udah diisi atau yang dia pilih itu pernah dipilih sebelumnya
									if (len(cls.matrix[idx_room][idx_waktu_start] > 0) or (idx_room == ruang_awal and idx_waktu_start == waktu_awal)):
										# Search to next slot time
										continue
									else:
										# Check if the slot time match with matkul constraint
										time_and_space_matchs = cls.check_matkul_constraint(cls.matrix[idx_room][idx_waktu_start][0], idx_room, idx_waktu_start)
										if (time_and_space_matchs): # Found the slot
											found = True
											cls.moveMatkul(idx_matkul, ruang_awal, waktu_awal, idx_room, idx_waktu_start)
									if found:
										break
							if found:
								break
						if found:
							break
				if not found:
					roundtrip += 1

			# Count conflict of new solution, if cnt reaches 10 then it terminates
			cls.next_conflict = cls.matrix.conflict_count()
			if (cls.next_conflict >= cls.curr_conflict or not found):
				cnt += 1
			else:
				cnt = 0

	@classmethod
	def finishing(cls):
		cls.matrix_hasil = Matriks(len(Jadwal.daftar_ruangan), 120)
		nRoom = len(Jadwal.daftar_ruangan)
		for idx_room in range(nRoom):
			for idx_waktu in range(120):
				cls.matrix_hasil[idx_room][idx_waktu].append(copy.deepcopy(cls.matrix_best[idx_room][idx_waktu].nama))

	@classmethod
	def __init__(cls):
		seed()
		cls.matrix = Matriks(len(Jadwal.daftar_ruangan), 120)
		cls.matrix_best = Matriks(len(Jadwal.daftar_ruangan), 120) # bedanya ini cuma nyimpen nama matkulnya doang
		cls.curr_conflict = curr_matriks.conflict_count()
		cls.next_conflict = 0
		cls.list_idx = [] # punya urutan yang sama dengan Jadwal.daftar_mata_kuliah
		cls.list_idx_best = []
		cls.first_initiate()

# catetan :
# urutan milih didalemnya belum random
