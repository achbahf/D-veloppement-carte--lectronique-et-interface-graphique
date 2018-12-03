import Tkinter as tk

#Programme de creation d'un clavier

class app:
	def __init__(self):
		global v
		v=tk.IntVar()
		v.set('')
		Frame=tk.Frame(root)
		Frame.grid()
		self.Entry=tk.Entry(Frame, textvariable=v)
		self.Entry.grid()
		def showkb(event, Entry=self.Entry):
			self.Entry.unbind('<FocusIn>')
			return clavier(Entry)
		self.Entry.bind('<FocusIn>',showkb)

class clavier:
	def __init__(self, Entry):
		
		global keyboardF
		keyboardF=tk.Frame(root)
		keyboardF.grid()
		global entry
		entry=Entry
		global compt
		compt=tk.IntVar()
		compt.set(0)
		r=0
		c=0
		self.aB=tk.Button(keyboardF,text='A',command=self.tapedA)
		self.zB=tk.Button(keyboardF,text='Z',command=self.tapedZ)
		self.eB=tk.Button(keyboardF,text='E',command=self.tapedE)
		self.rB=tk.Button(keyboardF,text='R',command=self.tapedR)
		self.tB=tk.Button(keyboardF,text='T',command=self.tapedT)
		self.yB=tk.Button(keyboardF,text='Y',command=self.tapedY)
		self.uB=tk.Button(keyboardF,text='U',command=self.tapedU)
		self.iB=tk.Button(keyboardF,text='I',command=self.tapedI)
		self.reB=tk.Button(keyboardF,text='<=',command=self.tapedret)
		self.oB=tk.Button(keyboardF,text='O',command=self.tapedO)
		self.pB=tk.Button(keyboardF,text='P',command=self.tapedP)
		self.qB=tk.Button(keyboardF,text='Q',command=self.tapedQ)
		self.sB=tk.Button(keyboardF,text='S',command=self.tapedS)
		self.dB=tk.Button(keyboardF,text='D',command=self.tapedD)
		self.fB=tk.Button(keyboardF,text='F',command=self.tapedF)
		self.gB=tk.Button(keyboardF,text='G',command=self.tapedG)
		self.hB=tk.Button(keyboardF,text='H',command=self.tapedH)
		self.jB=tk.Button(keyboardF,text='J',command=self.tapedJ)
		self.kB=tk.Button(keyboardF,text='K',command=self.tapedK)
		self.lB=tk.Button(keyboardF,text='L',command=self.tapedL)
		self.mB=tk.Button(keyboardF,text='M',command=self.tapedM)
		self.wB=tk.Button(keyboardF,text='W',command=self.tapedW)
		self.xB=tk.Button(keyboardF,text='X',command=self.tapedX)
		self.cB=tk.Button(keyboardF,text='C',command=self.tapedC)
		self.vB=tk.Button(keyboardF,text='V',command=self.tapedV)
		self.bB=tk.Button(keyboardF,text='B',command=self.tapedB)
		self.nB=tk.Button(keyboardF,text='N',command=self.tapedN)

		for widget in keyboardF.winfo_children():
			if widget.winfo_class()=='Button': 
				if c==9:
					c=0
					r=r+1
				widget.grid(row=r,column=c)
				c=c+1

	def tapedA (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'A')
	def tapedZ (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'Z')
	def tapedE (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'E')
	def tapedR (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'R')
	def tapedT (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'T')
	def tapedY (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'Y')
	def tapedU (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'U')
	def tapedI (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'I')
	def tapedO (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'O')
	def tapedret (self):
		compt.set(compt.get()-1)
		entry.delete(compt.get())
	def tapedP (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'P')
	def tapedQ (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'Q')
	def tapedS (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'S')
	def tapedD (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'D')
	def tapedF (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'F')
	def tapedG (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'G')
	def tapedH (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'H')
	def tapedJ (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'J')
	def tapedK (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'K')
	def tapedL (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'L')
	def tapedM (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'M')
	def tapedW (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'W')
	def tapedX (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'X')
	def tapedC (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'C')
	def tapedV (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'V')
	def tapedB (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'B')
	def tapedN (self):
		compt.set(compt.get()+1)
		entry.insert(tk.INSERT, 'N')
	

root=tk.Tk()
bb=test()
root.mainloop()
