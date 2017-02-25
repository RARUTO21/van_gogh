import warnings
warnings.filterwarnings("ignore")
from PIL import Image
import numpy as np
import random
from math import*


poblacionAnterior = []
poblacionActual = []

probM = 0.10
imagenMeta = []
masAptos = []

probCruce = 0
probMutacion = 0
sizePoblacion = 0

im = Image.open("a.png").convert("RGB")
im2 = Image.open("a2.png").convert("RGB")
aim = np.array(im)
aim2 = np.array(im2)

imagenMeta = aim


def iniciarAlgoritmo():
    while not terminado():
        cruzarPoblacion()
        mutarPoblacion()
    print("Termino :O")

def cargarImagenMeta(imagenDestino):
    global imagenMeta
    imagenMeta = np.array(Image.open(imagenDestino).convert("RGB"))


def cruzarPoblacion():
    global poblacionActual
    global poblacionAnterior
    
    poblacionTransicion = poblacionActual
   # poblacionActual = []
    poblacionAnterior = []
    
    for i in range(0,sizePoblacion//2):
        print("Iniciando generacion %d"%i)
        imagen1 = random.choice(poblacionTransicion)
        print("Tipo de elemento de imagen1 es:")
        print(type(imagen1))
        poblacionAnterior.append(imagen1)
        #poblacionTransicion.remove(imagen1)
        borrarElemento(poblacionTransicion,imagen1)
        
        imagen2 = random.choice(poblacionTransicion)
        poblacionAnterior.append(imagen2)
        #poblacionTransicion.remove(imagen2)
        borrarElemento(poblacionTransicion,imagen1)

        if np.random.randint(0,100) < probCruce:
            hijos = cruzarImagenes(imagen1,imagen2)[0]
            nuevaImagen1 = hijos[0]
            nuevaImagen2 = hijos[1]
            
            poblacionActual.append(nuevaImagen1)
            poblacionActual.append(nuevaImagen2)
        else:
            poblacionActual.append(imagen1)
            poblacionActual.append(imagen2)
            
        masAptos.append(obtenerMasApto(poblacionActual)) #corregir esto porque estoy haciendo generaciones-1 si lo hago desde aqui
        print("La similitud del mas apto de la generacion %d es: %f"%i%compararImagen(imagenMeta,masAptos[i]))


def borrarElemento(arreglo,elemento):
    for i in arreglo:
        if (i == elemento).any():
            (arreglo.remove(i)).any()

def cruzarImagenes(imagen1, imagen2):
    res = [None,None]

    corte = np.random.randint(1,len(imagen1)-1)

    res[0] = np.append(imagen1[:corte],imagen2[corte:],axis=0)
    res[1] = np.append(imagen2[:corte],imagen1[corte:],axis=0)
    return res


def menu():
    global sizePoblacion, probCruce, probMutacion

    print("Menu de Van Gogh")
    print("") 

    rutaImagen = input("Introduzca la ruta y nombre de la imagen: ")
    sizePoblacion = int(input("Introduzca el tamaño de la población: "))
    probCruce = float(input("Defina el % de probabilidad de cruce: "))
    probMutacion = float(input("Defina el % de probabilidad de mutación: "))
    cargarImagenMeta(rutaImagen)
    GenerarPoblacionInicial(sizePoblacion)
    print("")
    print("Iniciando...")
    print("")

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
        poblacionActual.append(np.array(imagen,dtype = "uint8"))
        imagen = []
        numImagenes -= 1
    #print(poblacionActual)


def terminado():
    for i in poblacionActual:
        if(compararImagen(i,imagenMeta)) < 20:            
            print("Si cumple: ",compararImagen(i,imagenMeta))            
            return True
    return False

def mutarPoblacion():
    for imagen in poblacionActual:
        imagen = mutarImagen(imagen)

def mutarImagen(imagen):
    mutados = []
    cantMutar = ((np.size(imagenMeta)/3)*probM)//1
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
        #print(compararImagen(imagenMeta,imagen))
        if compararImagen(imagenMeta,imagen) < compararImagen(imagenMeta,mejor):
            mejor = imagen
            
    print("El mejor de esta poblacion es de: %f"%compararImagen(imagenMeta,mejor))
    return mejor
print("")

