from PIL import Image
import numpy as np

poblacionAnterior = []
poblacionActual = []


im = Image.open("b.jpg")
#im.show()

arreglo = np.array(im)

arr = im.load()

print(arreglo[20,30])

#print(arr.getpixel(20,30))





def generarPoblacionInicial(size):
    cols = []
    rows = []

    

    
from math import*
 
def euclidean_distance(x,y):
 
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
