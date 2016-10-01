from .Jadwal import Jadwal
from .MatKulOnlyTime import MatKulOnlyTime
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
	def cariruang(cls, matkul):
		temp_matkul_time = MatKulOnlyTime()
		bol = False
		if matkul.ruangan != '-':
			idx = cls.nama_to_ruang_idx(matkul.ruangan)
			ruang = Jadwal.daftar_ruangan[idx]
			for hari in matkul.hari:
				for haris in ruang.hari:
					if hari == haris:
						if matkul.jam_awal >= ruang.jam_awal and matkul.jam_awal + matkul.sks <= ruang.jam_akhir:
							temp_matkul_time.setTime(idx, matkul.jam_awal, hari, matkul.sks)
							cls.daftar_matkul_time.append(temp_matkul_time)
							bol = True
							break

				if bol:
					break
		else:
			n = len(Jadwal.daftar_ruangan)
			for idx in range(n):
				ruang = Jadwal.daftar_ruangan[idx]
				for hari in matkul.hari:
					for haris in ruang.hari:
						if hari == haris:
							if matkul.jam_awal >= ruang.jam_awal and matkul.jam_awal + matkul.sks <= ruang.jam_akhir:
								temp_matkul_time.setTime(idx, matkul.jam_awal, hari, matkul.sks)
								cls.daftar_matkul_time.append(temp_matkul_time)
								bol = True
								break
						if bol:
							break
					if bol:
						break
				if bol:
					break

	@classmethod
	def __init__(cls):
		for matkul in Jadwal.daftar_mata_kuliah:
			cls.cariruang(matkul)
