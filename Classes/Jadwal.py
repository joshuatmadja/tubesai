from .Ruangan import Ruangan
from .MatKul import MatKul
from .Matriks import Matriks

class Jadwal:
    def process_ruangan_dan_mata_kuliah(self, ruangan_raw, mata_kuliah_raw):
        for ruangan in ruangan_raw:
            temp = ruangan.split(';')
            temp[3] = temp[3].split(',')
            temp_ruangan = Ruangan(temp[0], temp[1], temp[2], temp[3])
            self.daftar_ruangan.append(temp_ruangan)

        for mata_kuliah in mata_kuliah_raw:
            temp = mata_kuliah.split(';')
            temp[5] = temp[5].split(',')
            temp_mata_kuliah = MatKul(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])
            self.daftar_mata_kuliah.append(temp_mata_kuliah)

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
        self.daftar_ruangan = []
        self.daftar_mata_kuliah = []
        self.init_file(nama_file)
        self.matriks = Matriks(len(self.daftar_ruangan), 115)
