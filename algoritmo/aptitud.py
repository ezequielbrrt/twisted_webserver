import random

FREC={	1:["Lunes 16:30-18:00 ","Miercoles 16:30-18:00","Jueves 16:30-18:00"],
		2: ["Lunes 13:30-15:00","Martes 13:30-15:00","Viernes 13:30-15:00"],
		3: ["Martes 15:00-16:30", "Miercoles 15:00-16:30","Viernes 15:00-16:30"],
		4: ["Lunes 15:00-16:30","Jueves 15:00-16:30","Viernes 16:30-18:00"],
		5: ["Martes 18:30-20:00","Miercoles 18:30-20:00","Jueves 18:30-20:00"],
		6: ["Lunes 20:00-21:30","Miercoles 20:00-21:30","Jueves 20:00-21:30"],
		7: ["Martes 12:00-13:30","Miercoles 12:00-13:30","Viernes 12:00-13:30"]}
###Funcion que genera numeros aleatorios, con esto se generaran horarios.


def aleatorios(tamanioGenotipo):
	genotipo = []
	x = 0
	for i in range(tamanioGenotipo):
		x = int(random.uniform(0,7))
		genotipo.append(x)
	return genotipo
	
def crearPoblacion(tamanioPoblacion,tamanioGenotipo):
	arr = []
	for i in range(tamanioPoblacion):
		x = aleatorios(tamanioGenotipo)
		arr.append(x)
	return arr
# FREC={	1:[1,0,1,1,0],
			# 2: [1,0,1,0,1],
			# 3: [0,1,1,0,1],
			# 4: [1,0,0,1,1],
			# 5: [0,1,0,1,1],
			# 6: [1,0,1,1,0],
			# 7: [0,1,1,0,1]}
	
###########Calcular Aptitud########
def evaluar_funcion(materias,x1,tamanioGenotipo):
	CREDITOS=[4.50,4.36,4.39,4.39,4.39,4.39,4.46]
	y=[7,7,7,7,7,7,7]
	HORAS = [1.30,1.30,1.30,1.30,1.30,1.30,1.30]
	TOTAL=20
	suma = 0
	aptitud =0
	resultado = 0
	# print("XXXXXX",x1)
	for i in range(len(materias)):
		if(materias[i]==1):
			suma=suma+CREDITOS[i]
			if(x1[i] is 1|2|3|4|5|6|7):
				suma = suma - 30			
		if(materias[i]==0):
			if(x1[i]!=0):
				suma = suma - 40
	if(suma > TOTAL):
		suma = suma - 100
	aptitud=suma
	
	return aptitud
	
def calcular_Aptitud(poblacion, tamanioGenotipo, materias):
	aptitudes = []
	for i in range(0,len(poblacion)):
		x1 = poblacion[i]
		aptitudes.append(evaluar_funcion(materias, x1, tamanioGenotipo))
	#print len(aptitud)
	#print aptitud
	return aptitudes
##############################

# for key, value in FREC.items():
    # print (key, value)
#print(aleatorios(30))
