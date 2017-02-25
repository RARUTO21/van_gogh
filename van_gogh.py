
from PIL import Image
import numpy as np
import random
from math import*

poblacionAnterior = []
poblacionActual = []

imagenMeta = []


im = Image.open("a.png").convert("RGB")
im2 = Image.open("a2.png").convert("RGB")
im3 = Image.open("a3.png").convert("RGB")
im4 = Image.open("a4.png").convert("RGB")
arreglo = np.array(im)
arreglo2 = np.array(im2)
arreglo3 = np.array(im3)
arreglo4 = np.array(im4)

def menu():
    print("Menu de Van Gogh")
    print("") 
    rutaImagen = input("Introduzca la ruta y nombre de la imagen: ")
    sizePoblacion = int(input("Introduzca el tamaño de la población: "))
    probCruce = float(input("Introduzca el tamaño de la población: "))
     
    
    #print(rutaImagen)
#menu()

def cargarImagenMeta(imagenDestino):
    global imagenMeta
    
    

def generarPoblacionInicial(size):
    cols = []
    rows = []

def GenerarPoblacionInicial(numImagenes):
    global poblacionActual
    imagen = []
    while numImagenes > 0:
        for i in range(0,len(arreglo)):
            imagen.append([])
            for j in range(0,len(arreglo[i])):
                imagen[i].append([])
                for k in range(0,3):
                    imagen[i][j].append([])
                    imagen[i][j][k] = random.randint(0,32)        
        poblacionActual.append(np.array(imagen,dtype = "uint8"))
        imagen = []
        numImagenes -= 1
    print(poblacionActual)

def FuncionTerminado():
    
    
 
def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def compararImagen(imagen1,imagen2):
    avg = 0
    contador = 0
    for i in range(0,len(imagen1)):
        for j in range(0,len(imagen1[i])):
            avg += euclidean_distance(imagen1[i][j],imagen2[i][j])
            contador+=1
    print(contador)
    avg = avg/contador
    return "El % de similitud es de: "+str(avg)


print("NADA")
#def masApto


