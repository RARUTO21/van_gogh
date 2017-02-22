from PIL import Image
import numpy as np

poblacionAnterior = []
poblacionActual = []


im = Image.open("a2.png")
im2 = Image.open("a.png")
#im.show()

arreglo = np.array(im)
arreglo2 = np.array(im2)

arr = im.load()

#print(arreglo[20,30])

#print(arr.getpixel(20,30))





def generarPoblacionInicial(size):
    cols = []
    rows = []

    

    
from math import*
 
def euclidean_distance(x,y):
 
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
