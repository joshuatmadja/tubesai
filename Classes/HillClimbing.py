import copy
import random
from .Matriks import Matriks
from .Jadwal import Jadwal
from ..form import form
from .Assign import Assign

# kalo liat list, rooms[idx][3] itu list harinya

class HillClimbing:
	# Calculate index x and y value from selected slot
	# code = 0 means beginning idx x
	# code = 1 means end idx x
	def search_ruang_constraint(self, code, idx, day):
		ans = (rooms[idx][3][day] - 1) * 24 + rooms[idx][code+1]
		return ans
	# Return boolean value
	def check_matkul_constraint(self, matkull, x, y):

		banyak_hari = len(matkull[5])
		for idx_hari in range(banyak_hari):
			ans = 0

			# Check idx x (start and end), fulfill the constraint or not
			# If selected slot x fulfill the constraint, continue the check.
			# If not, end the looping, move check next matkul (conflicted or not)
			x1 = (matkull[5][idx_hari] - 1) * 24 + matkull[2]
			x2 = x1 + matkull[4] #tambah sks
			if (x < x1 or x > x2):
				break

			found = 0

			# If idx x fulfill the constraint, check room constraint
			# Check if slot idx y fulfill the constraint
			for idx_hari in range(len(matkull[1])):
				if (y == matkull[1][idx_hari]):
					found = 1
					ans = 1
					break
			if (found == 1):
				break
		return ans
		# 0 means false, 1 means true

	def first_initiate(self):
		# STEP 1 - Take MatkulOnlyTime data (list) of Course
		# convert to index by formula
		nSchedule = len(Jadwal.daftar_mata_kuliah)
		for i in range(nSchedule):
			x = (Assign.daftar_matkul_time[i].h_selected - 1) * 24 + Assign.daftar_matkul_time[i].j_selected
			y = Assign[i].daftar_matkul_time.r_selected
			temp = (x , y)
			self.list_idx.append(temp)
			self.tupel = (0, self.list_idx[0].x, self.list_idx[0].y)

	def calculate(self):
		cnt = 0
		while self.next_conflict < self.curr_conflict or cnt < 10:
			if (self.next_conflict < self.curr_conflict):
				self.curr_conflict = self.next_conflict
			self.list_temp = []
			found = 0

			# Updating daftar_mata_kuliah
			self.list_idx[self.tupel[0]].x = self.tupel[1]
			self.list_idx[self.tupel[0]].y = self.tupel[2]
			daftar_matkul_time[self.tupel[0]].j_selected = self.tupel[1] % 24
			daftar_matkul_time[self.tupel[0]].h_selected = self.tupel[1] // 24
			daftar_matkul_time[self.tupel[0]].r_selected = self.tupel[2] + 1

			# MAIN ALGORITHM
			# STEP 2 - Conflict checking & solving
			roundtrip = 0
			# cek muter
			while (roundtrip != 2):
				for idx_matkul in range(len(self.list_idx)):
					i = self.list_idx[idx].x
					j = self.list_idx[idx].y
					if (len(self.matrix[i][j]) > 1):
						list_temp = self.matrix[i][j]
						conflicted_matkul = copy.deepcopy(list_temp[0])

						for idx_y in range (nRoom):
							# Constraint slot waktu di matrix sesuai constraint ruangan
							for day in range(len(rooms[idx_matkul][3])):
								x_start =  self.search_ruang_constraint(0, idx, rooms[idx_matkul][3][day])
								x_end = self.search_ruang_constraint(1, idx, rooms[idx_matkul][3][day])
								for (idx_x) in range(x_start , x_end):
									if (len(self.matrix[idx_x][idx_y]) > 0 or (idx_x == i and idx_y == j)):
										# Search to next slot time
										pass
									else
										# Check if the slot time match with matkul constraint
										cek = self.check_matkul_constraint(self.matrix[idx_x][idx_y][0], idx_x, idx_y):
										if (cek == 1):
											# Found the slot
											found = 1
											(self.matrix[idx_x][idx_y]).append(conflicted_matkul)
											del (self.matrix[i][j])[0]
											self.tupel = (idx_matkul , idx_x, idx_y)
											roundtrip = 0
										else
											# If not found the slot, check next slot
											pass
									if (found == 1):
										break
								if (found == 1):
									break
							if (found == 1):
								break
					if (found == 1):
						break
					else if (found == 0 and idx_matkul == len(self.list_idx)):
						roundtrip+=1

			# Count conflict of new solution
			self.next_conflict = self.matrix.conflict_count()
			if (self.next_conflict >= self.curr_conflict):
				cnt += 1
			else
				cnt = 0

	def __init__(self):
		self.matrix = Matriks()
		self.curr_conflict = curr_matriks.conflict_count()
		self.next_conflict = 0
		self.list_idx = []
		self.tupel = (0,0,0) # For updating list MatkulOnlyTime and list_idx
