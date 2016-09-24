import tkinter
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

Days = ('Senin','Selasa','Rabu','Kamis','Jumat')
class form(tkinter.Tk):
	nRoom = 0
	nSchedule = 0
	rooms = []
	schedules = []
	
	
	def __init__(self, parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.mulai()

	def mulai(self):
		self.grid()
		self.resizable(False,False)

		#frame ruangan
		frRuang = ttk.Frame(self, padding="10 10 10 10", borderwidth= 2, relief = "solid")
		frRuang.grid(sticky="NWES", padx=(10,10), pady=(10,10))
		#frRuang.columnconfigure(0, weight=1)
		#frRuang.rowconfigure(0, weight=1)

		labelRuangan = tkinter.Label(frRuang, text=u"Ruangan", anchor="w")
		labelRuangan.grid(column=0, row=0, pady=(0,10))

		self.entryRuangVariable = tkinter.StringVar()
		self.entryRuang = tkinter.Entry(frRuang, textvariable=self.entryRuangVariable, width = 20)
		self.entryRuang.grid(column=1, row=0,padx=(10,0),columnspan=6, sticky="w")
		self.entryRuang.focus_set()
		#entryRuangVariable.set(u"Masukan nama ruangan"

		labelHari = tkinter.Label(frRuang, text=u"Hari", anchor="w")
		labelHari.grid(column=0, row=1, sticky="W")

		self.checkR = []
		self.RDay = []
		i=0
		for d in Days:
			self.checkR.append(tkinter.IntVar())
			self.RDay.append(tkinter.Checkbutton(frRuang,text=d,variable=self.checkR[i],onvalue=1, offvalue=0))
			self.RDay[i].grid(column=1, row=i+1,sticky="w")
			i+=1

		labelJam = tkinter.Label(frRuang, text=u"Jam", anchor="w")
		labelJam.grid(column=2, row = 1, sticky ="w", padx=(30,0))

		self.entryJamMulaiVar = tkinter.IntVar()
		self.entryJamMulai = tkinter.Entry(frRuang, textvariable=self.entryJamMulaiVar, width = 3, justify="right")
		self.entryJamMulai.grid(column=3, row=1, sticky="w")
		label00 = tkinter.Label(frRuang, text=": 00 -", anchor="w")
		label00.grid(column=4, row=1, sticky = "w")

		self.entryJamSelesaiVar = tkinter.IntVar()
		self.entryJamSelesai = tkinter.Entry(frRuang, textvariable=self.entryJamSelesaiVar, width = 3, justify="right")
		self.entryJamSelesai.grid(column=5, row=1, sticky="w")
		label00_ = tkinter.Label(frRuang, text=": 00", anchor="w")
		label00_.grid(column=6, row=1, sticky = "w")

		self.entryJamMulaiVar.set(7)
		self.entryJamSelesaiVar.set(8)

		buttonRuangan = tkinter.Button(frRuang,text=u"Submit Ruangan",command=self.validateRuang)
		buttonRuangan.grid(column=0, row=9, columnspan=9, padx=(10,10), pady=(10,0), sticky="s")

		frJadwal = ttk.Frame(self,padding="10 10 10 10", borderwidth=2, relief="solid")
		frJadwal.grid(column=1, row=0, sticky="NESW", padx=(10,10),pady=(10,10))
		#frJadwal.columnconfigure(0, weight=1)
		#frJadwal.rowconfigure(0,weight=1)

		labelJadwal = tkinter.Label(frJadwal, text=u"Mata Kuliah", anchor="w")
		labelJadwal.grid(column=0,row=0, sticky="nw")

		self.entryScheduleVar = tkinter.StringVar()
		self.entrySchedule = tkinter.Entry(frJadwal, textvariable=self.entryScheduleVar, width = 20)
		self.entrySchedule.grid(column=1, row=0, sticky="nw", columnspan=3)
		
		labelJadwal = tkinter.Label(frJadwal, text=u"       SKS", anchor="w")
		labelJadwal.grid(column=3,row=0, sticky="ne",columnspan=2)
		self.sks = tkinter.IntVar()
		self.entrySKS = tkinter.Entry(frJadwal,textvariable=self.sks, width=3,justify="right")
		self.entrySKS.grid(column=5, row=0, sticky="nw")

		labelRoom = tkinter.Label(frJadwal, text=u"Ruangan", anchor="w")
		labelRoom.grid(column=0,row=1, sticky="nw")

		self.roomFree = tkinter.IntVar()
		self.radioBebas = tkinter.Radiobutton(frJadwal, text = "Bebas", variable=self.roomFree, value = 0, command=self.selectingRuang)
		self.radioBebas.grid(column=1, row=1, sticky="nw")
		self.roomFree.set(0)
		self.radioSpec = tkinter.Radiobutton(frJadwal, text="Spesifik", variable=self.roomFree, value = 1, command=self.selectingRuang)
		self.radioSpec.grid(column=1, row=2, sticky="nw")
		self.entryRoomVar = tkinter.StringVar()
		self.entryRoom = tkinter.Entry(frJadwal, textvariable=self.entryRoomVar, width = 20, state="disabled")
		self.entryRoom.grid(column=2, row=2, sticky="nw",columnspan=3)
		
		labelHariJ = tkinter.Label(frJadwal, text=u"Hari", anchor="w")
		labelHariJ.grid(column=0, row=3, sticky="W")

		self.checkS = []
		self.SDay = []
		i=0
		for d in Days:
			self.checkS.append(tkinter.IntVar())
			self.SDay.append(tkinter.Checkbutton(frJadwal,text=d,variable=self.checkS[i],onvalue=1, offvalue=0))
			self.SDay[i].grid(column=1, row=i+3,sticky="w")
			i+=1


		labelJamJ = tkinter.Label(frJadwal, text=u"Jam", anchor="w")
		labelJamJ.grid(column=2, row = 3, sticky ="w", padx=(30,0))

		self.entryJamMulaiJVar = tkinter.IntVar()
		self.entryJamMulaiJ = tkinter.Entry(frJadwal, textvariable=self.entryJamMulaiJVar, width = 3, justify="right")
		self.entryJamMulaiJ.grid(column=3, row=3, sticky="w")
		label00J = tkinter.Label(frJadwal, text=": 00 -", anchor="w")
		label00J.grid(column=4, row=3, sticky = "w")

		self.entryJamSelesaiJVar = tkinter.IntVar()
		self.entryJamSelesaiJ = tkinter.Entry(frJadwal, textvariable=self.entryJamSelesaiJVar, width = 3, justify="right")
		self.entryJamSelesaiJ.grid(column=5, row=3, sticky="w")
		label00J_ = tkinter.Label(frJadwal, text=": 00", anchor="w")
		label00J_.grid(column=6, row=3, sticky = "w")

		self.entryJamMulaiJVar.set(7)
		self.entryJamSelesaiJVar.set(8)
		
		buttonJadwal = tkinter.Button(frJadwal,text=u"Submit Jadwal", command=self.validateJadwal)
		buttonJadwal.grid(column=0, row=9, columnspan=9, padx=(10,10), pady=(10,0), sticky="s")

		printR = tkinter.Button(self, text=u"Cetak Ruangan", command=self.onClickPrintRoom)
		printR.grid(column=0, row =1,columnspan=2, sticky="n")
		printJ = tkinter.Button(self, text=u"Cetak Jadwal", command=self.onClickPrintSchedule)
		printJ.grid(column=0, row=2, columnspan=2, sticky="n")
		printRes = tkinter.Button(self, text=u"Hasilkan", command=self.onClickShow)
		printRes.grid(column=0, row=3, columnspan=2, sticky="n")

	def selectingRuang(self):
		if(self.roomFree.get() == 0):
			self.entryRoom.config(state="disabled")
		elif(self.roomFree.get()==1):
			self.entryRoom.config(state="normal")

	def validateRuang(self):
		self.entryRuang.focus_set()
		if(self.entryRuangVariable.get()==''):
			msg = messagebox.showinfo("Kesalahan", "Ruangan harus diisi")
			self.entryRuang.focus_set()
		elif(self.entryJamMulaiVar.get()>=self.entryJamSelesaiVar.get()):
			msg = messagebox.showinfo("Kesalahan", "Jam mulai harus lebih awal daripada jam selesai")
			self.entryJamMulai.focus_set()
		else:
			self.onClickRoom()

	def validateJadwal(self):
		if(self.entryScheduleVar.get()==''):
			msg = messagebox.showinfo("Kesalahan", "Kode mata kuliah harus diisi")
			self.entrySchedule.focus_set()
		elif(self.sks.get()<=0):
			msg = messagebox.showinfo("Kesalahan", "SKS harus lebih dari 0")
			self.entrySKS.focus_set()
		elif(self.roomFree.get()==1 and self.entryRoomVar.get()==''):
			msg = messagebox.showinfo("Kesalahan", "Ruangan spesifik tidak boleh kosong")
			self.entryRoom.focus_set()
		elif(self.entryJamMulaiJVar.get()>=self.entryJamSelesaiJVar.get()):
			msg = messagebox.showinfo("Kesalahan", "Jam mulai harus lebih awal daripada jam selesai")
			self.entryJamMulaiJ.focus_set()
		else:
			self.onClickSchedule()

	def onClickRoom(self):
		hasil = []
		hasil.append(self.entryRuangVariable.get())
		hasil.append(self.entryJamMulaiVar.get())
		hasil.append(self.entryJamSelesaiVar.get())
		for j in range(5):
			if(self.checkR[j].get()==1):
				hasil.append(j+1)
		tup = tuple(hasil)
		self.rooms.append(tup)
		self.nRoom+=1
		print(tup)

		self.entryRuangVariable.set('')
		self.entryJamMulaiVar.set(7)
		self.entryJamSelesaiVar.set(8)
		self.entryRuang.focus_set()
		for j in range(5):
			self.RDay[j].deselect()

	def onClickPrintRoom(self):
		print('Ruangan terkumpul:')
		print(self.rooms)

	def onClickShow(self):
		app = result(None)
		app.title('Result')
		app.mainloop()

	def onClickSchedule(self):
		hasil = []
		hasil.append(self.entryScheduleVar.get())

		if(self.roomFree.get()==0):
			hasil.append('-')
		else:
			hasil.append(self.entryRoomVar.get())

		hasil.append(self.entryJamMulaiJVar.get())
		hasil.append(self.entryJamSelesaiJVar.get())
		hasil.append(self.sks.get())
		for j in range(5):
			if(self.checkS[j].get()==1):
				hasil.append(j+1)
		tup = tuple(hasil)
		self.schedules.append(tup)
		self.nSchedule+=1
		print(tup)

		self.entryScheduleVar.set('')
		self.sks.set(0)
		self.entryJamMulaiJVar.set(7)
		self.entryRoomVar.set('')
		self.roomFree.set(0)
		self.entryJamSelesaiJVar.set(8)
		self.entrySchedule.focus_set()
		for j in range(5):
			self.SDay[j].deselect()
	
	def onClickPrintSchedule(self):
		print('Jadwal terkumpul:')
		print(self.schedules)

class result(tkinter.Tk):
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.mulai()

	def mulai(self):
		tabel = ttk.Treeview(self)
		tabel.grid(column=0, row=3, columnspan=2)
		Time = ('07:00', '08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00')

		tabel["columns"]=Time
		for d in Time:
			tabel.column(d,width=70)
			tabel.heading(d, text=d)

if __name__ == "__main__":
	app = form(None)
	app.title('AI berDARAH')
	app.mainloop()