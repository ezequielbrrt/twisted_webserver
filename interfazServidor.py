from Tkinter import *
import tkMessageBox
import variables as var




def agregarMateria():
	if e1.get() != "" or e2.get() != "" or e3.get() != "" or e4.get() != "":
		f = open('materias.txt', 'a')
		f.write(e1.get()+","+
			e2.get()+","+
			e3.get()+","+e4.get()+"\n")
		f.close()
		materias = open("materias.txt", "r").read()
		e1.delete (0, last= len(e1.get()))	
		e2.delete (0, last= len(e2.get()))	
		e3.delete (0, last= len(e3.get()))	
		e4.delete (0, last= len(e4.get()))	
		materias = materias.split("\n")
		materias = filter(None, materias) # fastest
		tkMessageBox.showinfo("Agregado", "Se ha agregado la informacion con exito")
		materias = open("materias.txt", "r").read()	
		materias = materias.split("\n")
		materias = filter(None, materias) # fastest
		for i,j in zip(materias,range(len(materias))):
			Label(labelframe, text=i).grid(row=j)
	else:
		tkMessageBox.showinfo("Error", "Tienes que escribir un nombre")


root = Tk()


Label(root, text="Nombre Materia").grid(row=0)
Label(root, text="Numero Creditos").grid(row=0,column=1)
Label(root, text="Frecuencia a la semana").grid(row=0,column=2)
Label(root, text="Duracion de la clase").grid(row=2,column=0)
e1 = Entry(root)
e2 = Entry(root)
e2.grid(row=1,column=1)
e3 = Entry(root)
e3.grid(row=1,column=2)
e4 = Entry(root)
e4.grid(row=3,column=0)
e1.grid(row=1, column=0)
Button(root, text='Agregar', command=agregarMateria).grid(row=3,column=1)

labelframe = LabelFrame(root, text="Materias, Creditos, Frecuencia, Horas")
labelframe.grid(row=5,column=1)

materias = open("materias.txt", "r").read()	
materias = materias.split("\n")
materias = filter(None, materias) # fastest

for i,j in zip(materias,range(len(materias))):
	Label(labelframe, text=i).grid(row=j)


root.mainloop()

#import os
#os.system("python servidor.py")

print var.profesores