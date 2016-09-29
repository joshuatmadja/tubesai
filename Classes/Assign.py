from .Jadwal import Jadwal

class Assign:
	daftar_matkul_time = []
	
	def nama_to_ruang(nama):
		for ruang in Jadwal.daftar_ruangan:
			if ruang.nama == nama:
				return ruang
				break
		
	def cariruang(matkul):
		temp_matkul_time = MatKulOnlyTime()
		bol = False
		if matkul.ruangan != '-':
			ruang = nama_to_ruang(matkul.ruangan)
			for hari in matkul.hari:
				if bol:
					break
				for haris in ruang.hari:
					if hari == haris:
						if matkul.jam_awal >= ruang.jam_awal:
							if matkul.jam_awal + matkul.sks <= ruang.jam_akhir:
								temp_matkul_time.setTime(ruang, matkul.jam_awal, hari, matkul.sks)
								self.daftar_matkul_time.append(temp_matkul_time)
								bol = True
								break	
		else:
			for ruang in Jadwal.daftar_ruangan:
				if bol:
					break				
				for hari in matkul.hari:
					if bol:
						break
					for haris in ruang.hari:
						if hari == haris:
							if matkul.jam_awal >= ruang.jam_awal:
								if matkul.jam_awal + matkul.sks <= ruang.jam_akhir:
									temp_matkul_time.setTime(ruang, matkul.jam_awal, hari, matkul.sks)
									self.daftar_matkul_time.append(temp_matkul_time)
									bol = True
									break
				
	def masukkan():
		for matkul in Jadwal.daftar_mata_kuliah:			
			cariruang(matkul)
