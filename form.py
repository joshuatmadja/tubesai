import tkinter
from tkinter import *
from tkinter import ttk 

class form(tkinter.Tk):
	def __init__(self, parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.mulai()

	def mulai(self):
		self.grid()
		self.resizable(False,False)

		#frame ruangan
		frRuang = ttk.Frame(self, padding="10 10 10 10", borderwidth= 10, relief = "solid")
		frRuang.grid(sticky="NWES", padx=(10,10), pady=(10,10))
		frRuang.columnconfigure(0, weight=1)
		frRuang.rowconfigure(0, weight=1)

		labelRuangan = tkinter.Label(frRuang, text=u"Ruangan", anchor="w")
		labelRuangan.grid(column=0, row=0, pady=(0,10))

		entryRuangVariable = tkinter.StringVar()
		entryRuang = tkinter.Entry(frRuang, textvariable=entryRuangVariable, width = 20)
		entryRuang.grid(column=1, row=0,padx=(10,0),columnspan=6, sticky="w")
		#entryRuangVariable.set(u"Masukan nama ruangan")

		labelHari = tkinter.Label(frRuang, text=u"Hari", anchor="w")
		labelHari.grid(column=0, row=1, sticky="W")

		checkMonR = tkinter.IntVar()
		checkTueR = tkinter.IntVar()
		checkWedR = tkinter.IntVar()
		checkThuR = tkinter.IntVar()
		checkFriR = tkinter.IntVar()
		RMonday = tkinter.Checkbutton(frRuang, text="Senin", variable = checkMonR, onvalue=1, offvalue=0)
		RMonday.grid(column=1, row=1,padx=(10,0), sticky="W")
		RTuesday = tkinter.Checkbutton(frRuang, text="Selasa", variable = checkTueR, onvalue=1, offvalue=0)
		RTuesday.grid(column=1, row=2,padx=(10,0),sticky="W")
		RWednesday = tkinter.Checkbutton(frRuang, text="Rabu", variable = checkWedR, onvalue=1, offvalue=0)
		RWednesday.grid(column=1, row=3,padx=(10,0),sticky="W")
		RThursday = tkinter.Checkbutton(frRuang, text="Kamis", variable = checkThuR, onvalue=1, offvalue=0)
		RThursday.grid(column=1, row=4,padx=(10,0),sticky="W")
		RFriday = tkinter.Checkbutton(frRuang, text="Jumat", variable = checkFriR, onvalue=1, offvalue=0)
		RFriday.grid(column=1, row=5,padx=(10,0), sticky="W")

		labelJam = tkinter.Label(frRuang, text=u"Jam", anchor="w")
		labelJam.grid(column=2, row = 1, sticky ="w", padx=(30,0))

		entryJamMulaiVar = tkinter.IntVar()
		entryJamMulai = tkinter.Entry(frRuang, textvariable=entryJamMulaiVar, width = 3, justify="right")
		entryJamMulai.grid(column=3, row=1, sticky="w")
		label00 = tkinter.Label(frRuang, text=": 00 -", anchor="w")
		label00.grid(column=4, row=1, sticky = "w")

		entryJamSelesaiVar = tkinter.IntVar()
		entryJamSelesai = tkinter.Entry(frRuang, textvariable=entryJamSelesaiVar, width = 3, justify="right")
		entryJamSelesai.grid(column=5, row=1, sticky="w")
		label00_ = tkinter.Label(frRuang, text=": 00", anchor="w")
		label00_.grid(column=6, row=1, sticky = "w")

		buttonRuangan = tkinter.Button(frRuang,text=u"Input Ruangan")
		buttonRuangan.grid(column=0, row=6, columnspan=9, padx=(10,10), pady=(10,0))

		#tabel = ttk.Treeview(canvasRuang, columns=('','Senin','Selasa','Rabu','Kamis','Jumat'))
		#tabel.grid(column=0, row=4)
		#tabel.resizable(True,True)
		#tabel.insert('','end','widgets',text='Widget Tour')

if __name__ == "__main__":
	app = form(None)
	app.title('AI berDARAH')
	app.mainloop()