import warnings
warnings.filterwarnings("ignore")
from PIL import Image
import numpy as np
import random
from math import*

poblacionAnterior = []
poblacionActual = []
ordenada = []

imagenMeta = []
masAptos = []
simMasAptoPAnt = 0
simMasAptoPA = 400

probCruce = 0
probMutacion = 0
sizePoblacion = 0

def iniciarAlgoritmo():
    contador = 0    
    while not terminado():
        print("Generacion %d"%contador)
        cruzarPoblacion()
        mutarPoblacion()
        contador += 1
    a = obtenerMasApto(poblacionActual)
    b = Image.fromarray(a,"RGB")
    b.show()
    print("Termino :O")

def cargarImagenMeta(imagenDestino):
    global imagenMeta
    imagenMeta = np.array(Image.open(imagenDestino).convert("RGB"))


def cruzarPoblacion():
    global poblacionActual,poblacionAnterior,ordenada
    ordenada = ordenarMasApto(poblacionActual)    
    poblacionActual = []
    poblacionAnterior = []
    cont = 0
    for i in range(0,sizePoblacion//2):        
        imagen1 = ordenada[cont]
        poblacionAnterior.append(imagen1)
        cont+=1
        imagen2 = ordenada[cont]
        poblacionAnterior.append(imagen2)
        cont+=1
        if random.randint(0,100) < probCruce:
            hijos = cruzarImagenes(imagen1,imagen2)
            nuevaImagen1 = hijos[0]
            nuevaImagen2 = hijos[1]
            poblacionActual.append(nuevaImagen1)
            poblacionActual.append(nuevaImagen2)
        else:
            poblacionActual.append(imagen1)
            poblacionActual.append(imagen2)

def cruzarImagenes(imagen1, imagen2):
    res = [None,None]
    corte = random.randint(1,len(imagen1)-1)
    res[0] = imagen1[:corte]+imagen2[corte:]
    res[1] = imagen2[:corte]+imagen1[corte:]
    return res


def menu():
    global sizePoblacion, probCruce, probMutacion
    print("Menu de Van Gogh\n") 
    rutaImagen = input("Introduzca la ruta y nombre de la imagen: ")
    sizePoblacion = int(input("Introduzca el tamaño de la población: "))
    probCruce = float(input("Defina el % de probabilidad de cruce: "))
    probMutacion = float(input("Defina el % de probabilidad de mutación: "))
    cargarImagenMeta(rutaImagen)
    GenerarPoblacionInicial(sizePoblacion)
    print("\nIniciando...\n")
    iniciarAlgoritmo()
    
def GenerarPoblacionInicial(numImagenes):
    global poblacionActual
    imagen = []    
    while numImagenes > 0:
        for i in range(0,len(imagenMeta)):
            imagen.append([])
            for j in range(0,len(imagenMeta[i])):
                imagen[i].append([])
                for k in range(0,3):
                    imagen[i][j].append([])
                    imagen[i][j][k] = random.randint(0,255)        
        poblacionActual.append(imagen)
        imagen = []
        numImagenes -= 1
    print("\nPob. inicial creada...")
    #print(poblacionActual)


def terminado():
    if(simMasAptoPA) < 100:            
        print("Si cumple: ",compararImagen(i,imagenMeta))            
        return True
    return False

def mutarPoblacion():
    global poblacionActual
    global simMasAptoPA
    ordenada = ordenarMasApto(poblacionActual)
    poblacionActual = []
    imagen = []
    contMasApto = 0
    contMenosApto = 0
    indexImageMutadas = []
    indicador = 0
    for i in range(0,len(ordenada)):
        if indicador%(len(ordenada)-1) == 0: 
            imagen = ordenada[contMasApto]
            imagen = mutarImagen(imagen)
            poblacionActual.append(imagen)
            contMasApto+=1
        elif indicador%10 == 0:
            imagen = ordenada[(len(ordenada)-1)-contMenosApto]
            imagen = mutarImagen(imagen)
            poblacionActual.append(imagen)
            contMenosApto+=1
        else:
            imagen = []
            while imagen == []:
                index = random.randint(contMasApto,(len(ordenada)-1)-contMenosApto)            
                if index not in indexImageMutadas:
                    imagen = ordenada[index]
                    poblacionActual.append(imagen)
        indicador+=1   
            
            
    ##for imagen in poblacionActual:
    ##    imagen = mutarImagen(imagen)
    masAptos.append(obtenerMasApto(poblacionActual))
    if simMasAptoPA == 1000:
        simMasAptoPA = compararImagen(imagenMeta,masAptos[len(masAptos)-1])                
    else:
        simMasAptoPAnt = simMasAptoPA
        simMasAptoPA = compararImagen(imagenMeta,masAptos[len(masAptos)-1])                
    print("La similitud del mas apto de esta generacion es: %f"%simMasAptoPA)

def mutarImagen(imagen):
    mutados = []
    
    #if simMasAptoPAnt == 0:
        
    cantMutar = (((np.size(imagenMeta)/3)*probMutacion)//1)
##    if simMasAptoPAnt < simMasAptoPA:
##        cantMutar = ((((np.size(imagenMeta)/3)*probMutacion)//1)+((round((simMasAptoPA-simMasAptoPAnt)/2))*2))//1
##    else:
##        cantMutar = ((((np.size(imagenMeta)/3)*probMutacion)//1)-((round((simMAsApto-simMasAptoPAnt)/2))*0.7))//1
    while len(mutados) < cantMutar:
        row = random.randint(0,len(imagenMeta)-1)
        column = random.randint(0,len(imagenMeta[0])-1)
        if [row,column] not in mutados:
            imagen[row][column] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            mutados.append([row,column])
        
    return imagen

def collageImagenes():
    global masAptos
    numGeneraciones = len(masAptos)
    imagenResult = masAptos[0]
    i = 1
    while i >= 10:
        posProxImagen = round(numGeneraciones/10*i)
        imagenSig = masAptos[posProxImagen]
        imagenResult = concatenarImagenes(imagenResult,imagenSig)

def concatenarImagenes(imagenAnt,imagenSig):
     imagenAnt = convertToMatriz(imagenAnt)
     imagenSig = convertToMatriz(imagenSig)
     for i in range(0,len(imagenAnt)):
        #print("Fila I1: ",imagenAnt[i])
          for j in imagenSig[i]:
             #print("Columna a insert: ",j)
            imagenAnt[i].append(j)
     return np.array(imagenAnt,dtype="uint8")
    
def convertToMatriz(imagen):
    matriz = []
    for i in range(0,len(imagen)):
        matriz.append([])
        for j in range(0,len(imagen[i])):
           matriz[i].append([])
           for k in range(0,3):
                    matriz[i][j].append([])
                    matriz[i][j][k] = imagen[i][j][k]
    return matriz
  
def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def compararImagen(imagen1,imagen2):
    avg = 0
    contador = 0
    for i in range(0,len(imagen1)):
        for j in range(0,len(imagen1[i])):
            avg += euclidean_distance(imagen1[i][j],imagen2[i][j])
            contador+=1
    return avg/contador


def obtenerMasApto(poblacionActual):
    mejor = poblacionActual[0]
    for imagen in poblacionActual:
        if compararImagen(imagenMeta,imagen) < compararImagen(imagenMeta,mejor):
            mejor = imagen
    return mejor

def obtenerMenosApto(poblacionActual):
    peor = poblacionActual[0]
    for imagen in poblacionActual:
        if compararImagen(imagenMeta,imagen) > compararImagen(imagenMeta,peor):
            peor = imagen            
    return peor

def ordenarMasApto(poblacionActual):
    global ordenada,imagenMeta
    ordenada = []
    for imagen in poblacionActual:
        similitud = compararImagen(imagenMeta,imagen)
        imagen.append([similitud])
        ordenada.append(imagen)
    ordenada = sorted(ordenada, key = myKey)
    for imagen in ordenada:
        imagen.remove(imagen[len(imagen)-1])
    return ordenada

def myKey(item):
    return item[len(item)-1]

menu()

##Introduzca la ruta y nombre de la imagen: a4.png
##Introduzca el tamaño de la población: 27
##Defina el % de probabilidad de cruce: 60
##Defina el % de probabilidad de mutación: 0.02
