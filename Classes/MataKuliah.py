class MataKuliah:
    def __init__(self, nama, ruangan, awal, akhir, sks, hari):
        self.nama = nama
        self.ruangan = ruangan
        self.jam_awal = awal
        self.jam_akhir = akhir
        self.sks = sks
        self.hari = hari
        self.jam_available = [] #bakal diubah lagi
