from PIL import Image
import numpy as np
import random
from math import*

poblacionAnterior = []
poblacionActual = []


im = Image.open("b.jpg").convert("RGB")
im2 = Image.open("a.png").convert("RGB")
#im.show()

arreglo = np.array(im)
arreglo2 = np.array(im2)

arr = im.load()

#print(arreglo[20,30])

#print(arr.getpixel(20,30))

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


