from PIL import Image
import numpy as np
import random
from math import*

poblacionAnterior = []
poblacionActual = []


im = Image.open("a2.png").convert("RGB")
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

def GenerarPoblacionInicial():
    global poblacionAnterior
    generacion = []
    for i in range(0,len(arreglo)):
        generacion.append([])
        for j in range(0,len(arreglo[i])):
            generacion[i].append([])
            for k in range(0,3):
                generacion[i][j].append([])
                generacion[i][j][k] = random.randint(0,32)
    print(generacion)
    poblacionAnterior = generacion
    
 
def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))


