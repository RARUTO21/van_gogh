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


im = Image.open("a.png").convert("RGB")
im2 = Image.open("a2.png").convert("RGB")
im3 = Image.open("a3.png").convert("RGB")
im4 = Image.open("a4.png").convert("RGB")
arreglo = np.array(im)
arreglo2 = np.array(im2)
arreglo3 = np.array(im3)
arreglo4 = np.array(im4)
imagenMeta = arreglo4

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

def generarPoblacionInicial(numImagenes):
    global poblacionActual
    imagen = []
    while numImagenes > 0:
        for i in range(0,len(arreglo)):
            imagen.append([])
            for j in range(0,len(arreglo[i])):
                imagen[i].append([])
                for k in range(0,3):
                    imagen[i][j].append([])
                    imagen[i][j][k] = random.randint(0,255)        
        poblacionActual.append(np.array(imagen,dtype = "uint8"))
        imagen = []
        numImagenes -= 1
    print(poblacionActual)

def terminado():
    for i in poblacionActual:
        if(compararImagen(i,imagenMeta)) < 20:            
            print("Si cumple: ",compararImagen(i,imagenMeta))            
            return True
        #a = Image.fromarray(i,"RGB")
        #a.show()
        print(compararImagen(i,imagenMeta))
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
    
    for i in range(0,len(imagenAnt)-1):
        for j in imagenSig[i]:
            aix

def convertToMatriz(imagen):
    matriz = []
    for i in range(0,len(imagen)):
            matriz.append([])
            for j in range(0,len(imagen[i])):
                matriz[i].append([])
                for k in range(0,3):
                    matriz[i][j].append([])
                    matriz[i][j][k] = imagen[]
    
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


print("NADA")
#def masApto


