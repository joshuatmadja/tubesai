import copy
import random
from .Matriks import Matriks
from .Jadwal import Jadwal
from .Assign import Assign

# rooms itu punya form, ini pake jadwal dulu biar sama. roomsnya diganti Jadwal.daftar_ruangan
class HillClimbing:

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
	def first_initiate(cls):
		# STEP 1 - Take MatkulOnlyTime data (list) of Course
		# convert to index by formula
		nSchedule = len(Jadwal.daftar_mata_kuliah)
		for i in range(nSchedule):
			ruang = Assign.daftar_matkul_time[i].r_selected
			waktu = (Assign.daftar_matkul_time[i].h_selected - 1) * 24 + Assign.daftar_matkul_time[i].j_selected
			temp = (ruang, waktu)
			cls.list_idx.append(temp)

		cls.tupel = (0, cls.list_idx[0][0], cls.list_idx[0][1])

	@classmethod
	def calculate(cls):
		cnt = 0
		while cnt < 10:
			if (cls.next_conflict < cls.curr_conflict):
				cls.curr_conflict = cls.next_conflict
			list_temp = []
			found = False

			# Updating daftar_mata_kuliah
			cls.list_idx[cls.tupel[0]] = (cls.tupel[1], cls.tupel[2]) # assign ke yang pertama

			# ini ngapain, jangan mutasi Assign.daftar_matkul_time
#			Assign.daftar_matkul_time[cls.tupel[0]].j_selected = cls.tupel[1] % 24
#			Assign.daftar_matkul_time[cls.tupel[0]].h_selected = cls.tupel[1] // 24 + 1
#			Assign.daftar_matkul_time[cls.tupel[0]].r_selected = cls.tupel[2]

			# MAIN ALGORITHM
			# STEP 2 - Conflict checking & solving
			roundtrip = 0
			# cek muter
			while (roundtrip != 2 and (not found)):
				for idx_matkul in range(len(cls.list_idx)):
					ruang_awal, waktu_awal = cls.list_idx[idx_matkul] # extract the tuple

					if (len(cls.matrix[ruang_awal][waktu_awal]) > 1):
						list_temp = cls.matrix[ruang_awal][waktu_awal]
						conflicted_matkul = copy.deepcopy(list_temp[0])

						nRoom = len(Jadwal.daftar_ruangan)
						for idx_room in range(nRoom):
							# Constraint slot waktu di matrix sesuai constraint ruangan
							nDay = len(Jadwal.daftar_ruangan[idx_room].hari)
							for idx_day in range(nDay):
								# convert ke jam basis 120
								jam_converted_start = cls.search_ruang_constraint(0, idx, idx_day)
								jam_converted_end 	= cls.search_ruang_constraint(1, idx, idx_day)

								# looping terhadap jam yang available, basis 120
								for idx_waktu in range(jam_converted_start, jam_converted_end):
									# ngecek apakah dia udah diisi atau yang dia pilih itu pernah dipilih sebelumnya
									if (len(cls.matrix[idx_room][idx_waktu] > 0) or (idx_room == ruang_awal and idx_waktu == waktu_awal)):
										# Search to next slot time
										continue
									else:
										# Check if the slot time match with matkul constraint
										cek = cls.check_matkul_constraint(cls.matrix[idx_room][idx_waktu][0], idx_room, idx_waktu)
										if (cek):
											# Found the slot
											found = True
											cls.matrix[idx_room][idx_waktu].append(conflicted_matkul)
											del (cls.matrix[ruang_awal][waktu_awal][0])
											cls.tupel = (idx_matkul, idx_room, idx_waktuu)
									if found:
										break
							if found:
								break
						if found:
							break
				if ((not found) and (idx_matkul == len(cls.list_idx))):
					roundtrip += 1

			# Count conflict of new solution, if cnt reaches 10 then it terminates
			cls.next_conflict = cls.matrix.conflict_count()
			if (cls.next_conflict >= cls.curr_conflict or not found):
				cnt += 1
			else:
				cnt = 0

	@classmethod
	def __init__(cls):
		cls.matrix = Matriks(len(Jadwal.daftar_ruangan), 120)
		cls.curr_conflict = curr_matriks.conflict_count()
		cls.next_conflict = 0
		cls.list_idx = [] # punya urutan yang sama dengan Jadwal.daftar_mata_kuliah
		cls.tupel = (0,0,0) # (idx_matkul, idx_room, idx_waktu) --> For updating list MatkulOnlyTime and list_idx

# catetan :
# ini belum ada random randomnya
# list temp itu masih bingung
