class MatKulOnlyTime:
    def __init__(self):
        self.r_selected = -1
        self.j_selected = -1
        self.h_selected = -1
        self.sks = -1

    def setTime(self, r, j, h, s):
        self.r_selected = int(r)
        self.j_selected = int(j)
        self.h_selected = int(h)
        self.sks = int(s)
