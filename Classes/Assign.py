from .Jadwal import Jadwal
from .MatKulOnlyTime import MatKulOnlyTime
from .Matriks import Matriks
class Assign:
	daftar_matkul_time = []

	@classmethod
	def nama_to_ruang_idx(cls,nama):
		n  = len(Jadwal.daftar_ruangan)
		for idx in range(n):
			if Jadwal.daftar_ruangan[idx].nama == nama:
				return idx
		return None

	@classmethod
	def hitung_kosong(cls, ruang, jam_awal, jam_akhir):
		selisih = jam_akhir - jam_awal
		hitung = 0
		for i in range(selisih):
			if not cls.matriks[ruang][jam_awal+i]:
				hitung += 1
		return hitung
		
	@classmethod
	def min_kosong(cls, daftar):
		minim = 0
		for i in range(len(daftar)):
			if daftar[i] < daftar[minim]:
				minim = i
		return minim

	@classmethod
	def cariruang(cls, matkul):
		
		temp_matkul_time = MatKulOnlyTime()
		daftar_temp = []
		daftar_kosong = []
		if matkul.ruangan != '-':
			idx = cls.nama_to_ruang_idx(matkul.ruangan)
			ruang = Jadwal.daftar_ruangan[idx]
			for hari in matkul.hari:
				for haris in ruang.hari:
					if hari == haris:
						if max(matkul.jam_awal, ruang.jam_awal) + matkul.sks <= min(matkul.jam_akhir, ruang.jam_akhir):
							temp_matkul_time.setTime(idx, max(matkul.jam_awal, ruang.jam_awal), hari, matkul.sks)
							kosong = cls.hitung_kosong(temp_matkul_time.r_selected, temp_matkul_time.j_selected, min(matkul.jam_akhir, ruang.jam_akhir))
							kosong = kosong - matkul.sks
							if kosong < 0:
								kosong = abs(kosong) + 100
							daftar_kosong.append(kosong)
							daftar_temp.append(temp_matkul_time)
						
		else:
			n = len(Jadwal.daftar_ruangan)
			for idx in range(n):
				ruang = Jadwal.daftar_ruangan[idx]
				for hari in matkul.hari:
					for haris in ruang.hari:
						if hari == haris:
							if max(matkul.jam_awal, ruang.jam_awal) + matkul.sks <= min(matkul.jam_akhir, ruang.jam_akhir):
								temp_matkul_time.setTime(idx, max(matkul.jam_awal, ruang.jam_awal), hari, matkul.sks)
								kosong = cls.hitung_kosong(temp_matkul_time.r_selected, temp_matkul_time.j_selected, min(matkul.jam_akhir, ruang.jam_akhir))
								kosong = kosong - matkul.sks
								if kosong < 0:
									kosong = abs(kosong) + 100
								daftar_kosong.append(kosong)
								daftar_temp.append(temp_matkul_time)
						
		minim = cls.min_kosong(kosong)
		temp_matkul_time_final = temp_matkul_time[minim]
		cls.daftar_matkul_time.append(temp_matkul_time_final)
		
		c = (temp_matkul_time_final.h_selected - 1) * 24 + temp_matkul_time_final.j_selected
		for i in range(temp_matkul_time_final.sks):
			cls.matriks(temp_matkul_time_final.r_selected, c+i)
							
								
	@classmethod
	def __init__(cls):
		cls.matriks = Matriks()
		cls.daftar_matkul_time = []
		for matkul in Jadwal.daftar_mata_kuliah:
			cls.cariruang(matkul)
