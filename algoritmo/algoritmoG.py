import random
import struct
import aptitud as aptitud
import cruza as cruza
import mutacion as mutacion
import seleccion as seleccion

TAMANIO_POBLACION = 1000
NUMERO_GENERACIONES = 100
TAMANIO_GENOTIPO =  7
PROBABILIDAD_CRUZA = 0.95
NUMERO_MEJORESINDIVIDUOS = 5
PROBABILIDAD_MUTACION = 0.5
MATERIAS = []

dias = []
def getKey(item):
	return item[1]
def ordenar(poblacion, aptitudes):
	lista = []
	aux = []
	ordenados = [] 
	for i,(pob,apt) in enumerate(zip(poblacion, aptitudes)):
		aux.append(i)
		aux.append(apt)
		aux.append(pob)
		lista.append(aux)
		aux = []
	lista = sorted(lista,key=getKey,reverse=True)
	for x  in range(len(poblacion)):
		ordenados.append(lista[x][2])
	return ordenados   

def elitismo(Individuos, NUMERO_MEJORESINDIVIDUOS, mejoresIndividuos, aptitudes):
	if mejoresIndividuos == None:
		ordenados=ordenar(Individuos, aptitudes)
		mejoresIndividuos=[]	
		for i in range(0, NUMERO_MEJORESINDIVIDUOS):
			mejoresIndividuos.append(ordenados[i])
	else:
		ordenados=ordenar(Individuos, aptitudes)
		for i in range(NUMERO_MEJORESINDIVIDUOS):
			mejoresIndividuos.append(ordenados[i])
		aptitudes = aptitud.calcular_Aptitud(mejoresIndividuos, TAMANIO_GENOTIPO, MATERIAS)	
		ordenados2=ordenar(mejoresIndividuos, aptitudes)
		mejoresIndividuos=ordenados2[0:NUMERO_MEJORESINDIVIDUOS]
	return mejoresIndividuos
	
	
################### ALGORITMO GENETICO ########################	
	
def algoritmoGen(TAMANIO_POBLACION, NUMERO_GENERACIONES, TAMANIO_GENOTIPO, PROBABILIDAD_CRUZA, NUMERO_MEJORESINDIVIDUOS, listaPadres):
	generacionActual=0 #Listo
	mejoresIndividuos=None #Listo
	Individuos = aptitud.crearPoblacion(TAMANIO_POBLACION,TAMANIO_GENOTIPO)
	aptitudes = aptitud.calcular_Aptitud(Individuos, TAMANIO_GENOTIPO, MATERIAS)
	mejoresIndividuos=elitismo(Individuos, NUMERO_MEJORESINDIVIDUOS, mejoresIndividuos, aptitudes)
	print ("Aptitudes ",  aptitud.calcular_Aptitud(mejoresIndividuos,TAMANIO_GENOTIPO, MATERIAS))
	for i in mejoresIndividuos :
		print (i)
	listaPadres = seleccion.seleccionarPadres(Individuos, aptitudes)
	nuevaPoblacion = Individuos
	while generacionActual <= NUMERO_GENERACIONES :
		nuevaPoblacion = cruza.cruzarPadres(nuevaPoblacion, listaPadres, PROBABILIDAD_CRUZA)
		nuevaPoblacion = mutacion.mutacionUniforme(nuevaPoblacion, PROBABILIDAD_MUTACION, TAMANIO_GENOTIPO)
		aptitudes = aptitud.calcular_Aptitud(nuevaPoblacion, TAMANIO_GENOTIPO, MATERIAS)
		mejoresIndividuos = elitismo(nuevaPoblacion, NUMERO_MEJORESINDIVIDUOS,mejoresIndividuos, aptitudes)
		print ("Generacion: ", generacionActual)
		print ("Aptitudes",  aptitud.calcular_Aptitud(mejoresIndividuos, TAMANIO_GENOTIPO, MATERIAS))
		for i in mejoresIndividuos:
			print (i)
		print("\n")
		listaPadres = seleccion.seleccionarPadres(nuevaPoblacion, aptitudes)
		generacionActual+=1
	mat =  mejoresIndividuos[0]
	print aptitud.FREC
	for i in mejoresIndividuos[0]:
		if i>0:
			dias.append(aptitud.FREC[i])

	return dias


def iniciar():
	listaPadres = []
	return algoritmoGen(TAMANIO_POBLACION, NUMERO_GENERACIONES, TAMANIO_GENOTIPO, PROBABILIDAD_CRUZA, NUMERO_MEJORESINDIVIDUOS, listaPadres)
	

