class MatKulOnlyTime:
    def __init__(self):
        self.r_selected = -1
        self.j_selected = -1
        self.h_selected = -1
        self.sks = -1

    def setTime(self, r, j, h, s):
        self.r_selected = r
        self.j_selected = j
        self.h_selected = h
        self.sks = s
