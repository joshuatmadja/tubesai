from .Ruangan import Ruangan
from .MatKul import MatKul
from .Matriks import Matriks
from .MatKulOnlyTime import MatKulOnlyTime

class Jadwal:
    daftar_ruangan = []
    daftar_mata_kuliah = []
    total_pasangan = 0

    def process_ruangan_dan_mata_kuliah(self, ruangan_raw, mata_kuliah_raw):

        for ruangan in ruangan_raw:
            temp = ruangan.split(';')
            temp[3] = temp[3].split(',')
            temp_ruangan = Ruangan(temp[0], int(float(temp[1])), int(float(temp[2])), temp[3])

            self.daftar_ruangan.append(temp_ruangan)

        for mata_kuliah in mata_kuliah_raw:
            temp = mata_kuliah.split(';')
            temp[5] = temp[5].split(',')
            temp_mata_kuliah = MatKul(temp[0], temp[1], int(float(temp[2])), int(float(temp[3])), int(temp[4]), temp[5])
            self.daftar_mata_kuliah.append(temp_mata_kuliah)

        n = len(self.daftar_mata_kuliah)
        temp_total = 0
        for i in range(0,n):
            self.total_pasangan += temp_total * self.daftar_mata_kuliah[i].sks
            temp_total += self.daftar_mata_kuliah[i].sks
        self.total_pasangan += 1

    def read_file(self,ruangan_raw, mata_kuliah_raw, nama_file):
        f = open(nama_file, "r")
        mylist = f.read().splitlines()
        ruangan_loaded = False
        for line in mylist:
            if line == 'Ruangan' or line == '':
                pass
            elif line == 'Jadwal':
                ruangan_loaded = True
            elif not ruangan_loaded:
                ruangan_raw.append(line)
            else:
                mata_kuliah_raw.append(line)
        f.close()

    def init_file(self,nama_file):
        ruangan_raw = []
        mata_kuliah_raw = []
        self.read_file(ruangan_raw, mata_kuliah_raw, nama_file)
        self.process_ruangan_dan_mata_kuliah(ruangan_raw, mata_kuliah_raw)

    def __init__(self, nama_file):
        self.init_file(nama_file)
        self.matriks = Matriks(len(self.daftar_ruangan), 120)
