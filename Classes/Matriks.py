class Matriks:
    def __init__(self, row, col):
        self.matriks = []
    def init(self, row, col):
        for i in row:
            self.matriks.append([])
            for j in col:
                self.matriks[i].append([])

    def conflict_count(self):
        total = 0
        for ruang in self.matriks:
            for jam in ruang:
                cnt = len(jam)
                total += cnt * (cnt-1) / 2
        return total
