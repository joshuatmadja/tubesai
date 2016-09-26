from .Jadwal import Jadwal

class Assign:
	#belom aktifin jadwal
	#belum nyari ruang di daftar_ruangan
	#belum aktifin daftar_matkul_time
		
	def cariruang(matkul):
		bol = False
		if matkul.ruangan != '-':
			ruang = matkul.ruangan
			for hari in matkul.hari:
				if bol:
					break
				for haris in ruang.hari:
					if hari == haris:
						if matkul.jam_awal >= ruang.jam_awal:
							if matkul.jam_awal + matkul.sks <= ruang.jam_akhir:
								matkul.setTime(ruang, matkul.jam_awal, hari, matkul.sks)
								bol = True
								break	
		else:
			for ruang in jadwal.daftar_ruangan:
				if bol:
					break				
				for hari in matkul.hari:
					if bol:
						break
					for haris in ruang.hari:
						if hari == haris:
							if matkul.jam_awal >= ruang.jam_awal:
								if matkul.jam_awal + matkul.sks <= ruang.jam_akhir:
									matkul.setTime(ruang, matkul.jam_awal, hari, matkul.sks)
									bol = True
									break
				
	def masukkan(matkuls):
		for matkul in matkuls:			
			cariruang(matkul)
