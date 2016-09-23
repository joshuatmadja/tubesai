class Matriks:
    row = 0
    col = 0

    def __init__(self, r = row, c = col):
        row = r
        col = c
        self.matriks = []
        for i in range(row):
            self.matriks.append([])
            for j in range(col):
                self.matriks[i].append([])

    def conflict_count(self):
        total = 0
        for ruang in self.matriks:
            for jam in ruang:
                cnt = len(jam)
                total += cnt * (cnt-1) / 2
        return total
