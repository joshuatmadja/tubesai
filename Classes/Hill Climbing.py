import copy
import random
from .Matriks import Matriks
from .Jadwal import Jadwal
from .form import Form
from .Assign import Assign

class HillClimbing:
	
	def search_ruang_constraint(code,idx,day):
		ans = ( rooms[idx][3][day] - 1 ) * 24 + rooms[idx][code+1]
		return ans

	def check_matkul_constraint(matkull, x, y): 
		for idx_hari in range(len(matkull[6])):
			x1 = (matkull[6][idx_hari] - 1) * 24 + matkull[3]
			x2 = x1 + matkull[5]
			if (x <= x1 and x >= x2)
				break
			found = 0
			ans = 0
			for idx_hari in range(len(matkull[2])):
				if (y == matkull[2][idx_hari] ):
					found = 1
					ans = 1
					break
			if (found == 1)
				break
		return ans # 0 means false, 1 means true

	def first_initiate():
		# STEP 1 - Take MatkulOnlyTime data (list) of Course
		# convert to index by formula
		for i in range(len(Jadwal.daftar_mata_kuliah)):
			x = (Assign.daftar_matkul_time[i].h_selected - 1) * 24 + Assign.daftar_matkul_time[i].j_selected
			y = Assign[i].daftar_matkul_time.r_selected
			temp = (x , y)
			self.list_idx.append(temp)
			self.tupel = (0 , self.list_idx[0].x , self.list_idx[0].y)

	def calculate():
		while self.next_conflict < self.curr_conflict:
			self.curr_conflict = self.next_conflict
			self.list_temp = []
			found = 0

			# Updating daftar_mata_kuliah
			self.list_idx[self.tupel[0]].x = self.tupel[1]
			self.list_idx[self.tupel[0]].y = self.tupel[2]

			# MAIN ALGORITHM
			# STEP 2 - Conflict checking & solving
			roundtrip = 0
			while (roundtrip != 2):
				for idx in range(len(self.list_idx)):
					i = self.list_idx[idx].x
					j = self.list_idx[idx].y
					if ( len(self.matrix[i][j]) > 1 ):
						list_temp = self.matrix[i][j]
						conflicted_matkul = copy.deepcopy(list_temp[0])
						for (idx_y) in range j:
							# Constraint slot waktu di matrixx sesuai constraint ruangan
							for day in range(len(rooms[idx][3])):
								x_start =  self.search_ruang_constraint(0,idx,rooms[idx][3][day])
								x_end = self.search_ruang_constraint(1,idx,rooms[idx][3][day])
								for (idx_x) in range(x_start,x_end):
									if (len(self.matrix[idx_x][idx_y]) > 0):
										# Search to next slot time
									else
										# Check if the slot time match with matkul constraint
										cek = self.check_matkul_constraint(self.matrix[idx_x][idx_y][0], idx_x, idx_y):
										if (cek == 1):
										# Found the slot
											found = 1
											(self.matrix[idx_x][idx_y]).append(conflicted_matkul)
											del (self.matrix[i][j])[0]
											self.tupel = (idx , idx_x, idx_y)
											roundtrip = 0	
										# If not found the slot, check next slot
									if (found == 1):
										break
								if (found == 1):
									break
							if (found == 1):
								break
					if (found == 1):
						break
					else if (found == 0 and idx == len(self.list_idx)):
						roundtrip+=1

			# Count conflict of new solution
			self.next_conflict = self.matrix.conflict_count()

	def __init__(self):
		self.matrix = Matriks()
		self.curr_conflict = curr_matriks.conflict_count()
		self.next_conflict = 0
		self.list_idx = []
		self.tupel = (0,0,0)
		pass
		
#self.tupel namanya mencurigakan, mungkin bisa diganti?
#pake self. kalo dia atribut si kelasnya
