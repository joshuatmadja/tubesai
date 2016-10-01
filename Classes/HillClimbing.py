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
	def search_ruang_constraint(self, code, idx, day):
		room = Jadwal.daftar_ruangan[idx]
		ans = (room.hari[day] - 1) * 24
		if code == 0:
			ans += room.jam_awal  # constraint jam awal
		else:
			ans += room.jam_akhir # constraint jam akhir
		return ans

	# Return boolean value
	def check_matkul_constraint(self, matkul_selected, r_selected, w_selected):

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


	def first_initiate(self):
		# STEP 1 - Take MatkulOnlyTime data (list) of Course
		# convert to index by formula
		nSchedule = len(Jadwal.daftar_mata_kuliah)
		for i in range(nSchedule):
			ruang = Assign.daftar_matkul_time[i].r_selected
			waktu = (Assign.daftar_matkul_time[i].h_selected - 1) * 24 + Assign.daftar_matkul_time[i].j_selected
			temp = (ruang , waktu)
			self.list_idx.append(temp)
		self.tupel = (0, self.list_idx[0][0], self.list_idx[0][1])

	def calculate(self):
		cnt = 0
		while cnt < 10:
			if (self.next_conflict < self.curr_conflict):
				self.curr_conflict = self.next_conflict
			list_temp = []
			found = False

			# Updating daftar_mata_kuliah
			self.list_idx[self.tupel[0]] = (self.tupel[1], self.tupel[2]) # assign ke yang pertama

			# ini ngapain, jangan mutasi Assign.daftar_matkul_time
#			Assign.daftar_matkul_time[self.tupel[0]].j_selected = self.tupel[1] % 24
#			Assign.daftar_matkul_time[self.tupel[0]].h_selected = self.tupel[1] // 24 + 1
#			Assign.daftar_matkul_time[self.tupel[0]].r_selected = self.tupel[2]

			# MAIN ALGORITHM
			# STEP 2 - Conflict checking & solving
			roundtrip = 0
			# cek muter
			while (roundtrip != 2 and (not found)):
				for idx_matkul in range(len(self.list_idx)):
					ruang_awal, waktu_awal = self.list_idx[idx_matkul] # extract the tuple

					if (len(self.matrix[ruang_awal][waktu_awal]) > 1):
						list_temp = self.matrix[ruang_awal][waktu_awal]
						conflicted_matkul = copy.deepcopy(list_temp[0])

						nRoom = len(Jadwal.daftar_ruangan)
						for idx_room in range(nRoom):
							# Constraint slot waktu di matrix sesuai constraint ruangan
							nDay = len(Jadwal.daftar_ruangan[idx_room].hari)
							for idx_day in range(nDay):
								# convert ke jam basis 120
								jam_converted_start = self.search_ruang_constraint(0, idx, idx_day)
								jam_converted_end 	= self.search_ruang_constraint(1, idx, idx_day)

								for (idx_waktu) in range(jam_converted_start, jam_converted_end):
									# ngecek apakah dia udah diisi atau yang dia pilih itu pernah dipilih sebelumnya
									if (len(self.matrix[idx_room][idx_waktu] > 0) or (idx_room == ruang_awal and idx_waktu == waktu_awal)):
										# Search to next slot time
										continue
									else:
										# Check if the slot time match with matkul constraint
										cek = self.check_matkul_constraint(self.matrix[idx_room][idx_waktu][0], idx_room, idx_waktu)
										if (cek):
											# Found the slot
											found = True
											self.matrix[idx_room][idx_waktu].append(conflicted_matkul)
											del (self.matrix[ruang_awal][waktu_awal][0])
											self.tupel = (idx_matkul, idx_room, idx_waktu)
									if found:
										break
							if found:
								break
						if found:
							break
				if ((not found) and (idx_matkul == len(self.list_idx))):
					roundtrip += 1

			# Count conflict of new solution, if cnt reaches 10 then it terminates
			self.next_conflict = self.matrix.conflict_count()
			if (self.next_conflict >= self.curr_conflict or not found):
				cnt += 1
			else:
				cnt = 0

	def __init__(self):
		self.matrix = Matriks(len(Jadwal.daftar_ruangan), 120)
		self.curr_conflict = curr_matriks.conflict_count()
		self.next_conflict = 0
		self.list_idx = [] # punya urutan yang sama dengan Jadwal.daftar_mata_kuliah
		self.tupel = (0,0,0) # (idx_matkul, idx_room, idx_waktu) --> For updating list MatkulOnlyTime and list_idx

# catetan :
# ini belum ada random randomnya
# list temp itu masih bingung
