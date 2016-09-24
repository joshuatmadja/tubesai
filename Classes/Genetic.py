from .MatKulOnlyTime import MatKulOnlyTime
from .Matriks import Matriks
from .Jadwal import Jadwal
from random import randint, shuffle

class Genetic:
    inputs = []
    result = []

    @staticmethod
    def fitness(self, chromosome):
        M = Matriks()
        for mkot in chromosome:
            t = 0
            for ruangan in Jadwal.daftar_ruangan:
                if(mkot == ruangan.nama):
                    awal = (mkot.h_selected-1) * 24 + (mkot.j_selected)
                    for i in range(awal, awal + sks):
                        M[t][i].append(mkot)
                    break
                else:
                    t += 1
        return Jadwal.total_pasangan - M.conflict_count()

    # mutate ini dilakukan abis chromosomenya digabungin
    def mutate(self, chromosome):

        pass # bingung mau ganti hari juga apa gimana, soalnya ini pinginnya jadi lebih bagus gitu sih

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
        pass

    @staticmethod
    def add(self, jadwal):
        self.inputs.append(jadwal)

    @staticmethod
    def best(self):
        return self.result[-1]

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
