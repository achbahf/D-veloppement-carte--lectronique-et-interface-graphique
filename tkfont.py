#ce programme affiche les polices d'ecriture tkFont  

import Tkinter as tk
import tkFont

root=tk.Tk()
b=(tkFont.families(root))	

for i in range (0,len(b)/8):
	font=tkFont.Font(family=b[i])
	tk.Label(root, text=b[i],font=font).grid(row=i,column=0)
for i in range (len(b)/8,len(b)/4):
	font=tkFont.Font(family=b[i])
	tk.Label(root, text=b[i],font=font).grid(row=i-(len(b)/8), column=1)

for i in range (len(b)/4,3*len(b)/8):
	font=tkFont.Font(family=b[i])
	tk.Label(root, text=b[i],font=font).grid(row=i-(len(b)/4),column=2)

for i in range (3*len(b)/8,len(b)/2):
	font=tkFont.Font(family=b[i])
	tk.Label(root, text=b[i],font=font).grid(row=i-(3*len(b)/8),column=3)

for i in range (len(b)/2,5*len(b)/8):
	font=tkFont.Font(family=b[i])
	tk.Label(root, text=b[i],font=font).grid(row=i-(len(b)/2),column=4)
for i in range (5*len(b)/8,6*len(b)/8):
	font=tkFont.Font(family=b[i])
	tk.Label(root, text=b[i],font=font).grid(row=i-(5*len(b)/8),column=5)

for i in range (3*len(b)/4,7*len(b)/8):
	font=tkFont.Font(family=b[i])
	tk.Label(root, text=b[i],font=font).grid(row=i-(3*len(b)/4),column=6)

for i in range (7*len(b)/8,len(b)):
	font=tkFont.Font(family=b[i])
	tk.Label(root, text=b[i],font=font).grid(row=i-(7*len(b)/8),column=7)
root.mainloop()
