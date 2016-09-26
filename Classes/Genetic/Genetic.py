from ..MatKulOnlyTime import MatKulOnlyTime
from ..Matriks import Matriks
from ..Jadwal import Jadwal
from random import randint, shuffle
from math import ceil

class Genetic:
    inputs = []
    result = []

    @staticmethod
    def fitness(self, chromosome):
        M = Matriks()
        for mkot in chromosome:
            awal = (mkot.h_selected-1) * 24 + (mkot.j_selected)
            for i in range(awal, awal + sks):
                M[mkot.r_selected][i].append(mkot)

        return Jadwal.total_pasangan - M.conflict_count()

    # mutate ini dilakukan abis chromosomenya digabungin
    def random_assign(self, x):

        bisa = False
        MBaru = MatKulOnlyTime()
        COMB_PER_HARI = Jadwal.daftar_mata_kuliah[x].akhir - Jadwal.daftar_mata_kuliah[x].awal - Jadwal.daftar_mata_kuliah[x].sks + 1
        JUMLAH_HARI = len(Jadwal.daftar_mata_kuliah[x].hari)
        comb_waktu = COMB_PER_HARI * JUMLAH_HARI
        urut_waktu = []
        for i in range(comb_waktu):
            urut_waktu.append(i)

        shuffle(urut_waktu)
        if(Jadwal.daftar_mata_kuliah[x].ruangan == '-'):
            urut_ruangan = []
            comb_ruangan = len(Jadwal.daftar_ruangan)

            for i in range(comb_ruangan):
                urut_ruangan.append(i)

            shuffle(urut_ruangan)
            for ruangan_selected in urut_ruangan:
                if bisa:
                    break
                for z in urut_waktu:
                    hari_selected = Jadwal.daftar_mata_kuliah[x].hari[z / COMB_PER_HARI]
                    jam_selected = Jadwal.daftar_mata_kuliah[x].awal + (z % COMB_PER_HARI) - 1
                    temp_ruangan = Jadwal.daftar_ruangan[ruangan_selected]
                    if(hari_selected in temp_ruangan.hari and jam_selected >= temp_ruangan.awal and jam_selected + Jadwal.daftar_mata_kuliah[x].sks <= temp_ruangan.akhir):
                        MBaru.setTime(ruangan_selected, jam_selected, hari_selected, Jadwal.daftar_mata_kuliah[x].sks)
                        break
        else:
            ruangan_selected = Jadwal.daftar_ruangan.index(Jadwal.daftar_mata_kuliah[x].ruangan)
            for z in urut_waktu:
                hari_selected = Jadwal.daftar_mata_kuliah[x].hari[z / COMB_PER_HARI]
                jam_selected = Jadwal.daftar_mata_kuliah[x].awal + (z % COMB_PER_HARI) - 1
                temp_ruangan = Jadwal.daftar_ruangan[ruangan_selected]
                if(hari_selected in temp_ruangan.hari and jam_selected >= temp_ruangan.awal and jam_selected + Jadwal.daftar_mata_kuliah[x].sks <= temp_ruangan.akhir):
                    MBaru.setTime(ruangan_selected, jam_selected, hari_selected, Jadwal.daftar_mata_kuliah[x].sks)
                    break
        return MBaru

    def mutate(self, chromosome):
        panjang = len(chromosome)
        bnyk = math.ceil(panjang / 20)
        for i in range(bnyk):
            x = randint(0, panjang - 1)
            chromosome[x] = self.random_assign(x)
        # bingung mau ganti hari juga apa gimana, soalnya ini pinginnya jadi lebih bagus gitu sih

    def selectidx(self, n, fitness_total, r_num):
        now = 0
        idx = 0
        for i in range(n):
            now += fitness_total[i]
            if(now > r_num):
                break
            idx += 1
        return idx

    @staticmethod
    def run(self, loops):

        for xxx in range(loops):
            fitness_total = []
            n = len(self.inputs)

            # calculate total fitness
            for chromosome in self.inputs:
                fitness_total.append(self.fitness(chromosome))

            # sort based on fitness_total
            for i in range(n):
                for j in range(n-i):
                    if (fitness_total[j] > fitness_total[j+1]):
                        fitness_total[j], fitness_total[j+1] = fitness_total[j+1], fitness_total[j]
                        self.inputs[j], self.inputs[j+1] = self.inputs[j+1], self.inputs[j]

            pivot = randint(1, len(Jadwal.daftar_mata_kuliah))

            # calculate the total chance
            total_chance = 0
            for i in range(n):
                total_chance += fitness_total[i]

            result = []
            for i in range(n):
                x = self.inputs[selectidx(n, fitness_total, randint(0, total_chance-1))][:pivot]
                y = self.inputs[selectidx(n, fitness_total, randint(0, total_chance-1))][pivot:]
                child = x
                child.append(y)

                if(n > randint(1, n*n)):
                    self.mutate(child)

                result.append(child)

            inputs = result

    @staticmethod
    def init(self):
        self.inputs = []
        self.result = []
        banyak = 10
        n = len(Jadwal.daftar_mata_kuliah)
        for i in range(banyak):
            self.inputs.append([])
            for x in range(n):
                self.inputs[i].append(self.random_assign(x))

    @staticmethod
    def add(self, jadwal):
        self.inputs.append(jadwal)

    @staticmethod
    def best(self):
        return self.result[-1]

    @staticmethod
    def sort(self):
        fitness_total = []
        n = len(self.inputs)

        for chromosome in self.result:
            fitness_total.append(self.fitness(chromosome))

        for i in range(n):
            for j in range(n-i):
                if (fitness_total[j] > fitness_total[j+1]):
                    fitness_total[j], fitness_total[j+1] = fitness_total[j+1], fitness_total[j]
                    self.result[j], self.result[j+1] = self.result[j+1], self.result[j]
