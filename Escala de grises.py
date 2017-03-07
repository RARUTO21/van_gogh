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

tipoCruce = 1
generacion = 0

#LISTA
def iniciarAlgoritmo():
    global tipoCruce,generacion
    contador = 0    
    while not terminado():
        print("Generacion %d"%contador)
        cruzarPoblacion()
        mutarPoblacion()        
        tipoCruce+=1
        if contador%3 == 0 and generacion != 37:
            generacion+=1
        contador += 1
    mejorImagen = np.array(masAptos[len(masAptos)-1],dtype="uint8")
    a = Image.fromarray(mejorImagen,"L")
    a.show()
    print("Termino :O")

#LISTA
def cargarImagenMeta(imagenDestino):
    global imagenMeta
    imagenMeta = np.array(Image.open(imagenDestino).convert("L"))
##    imagen = Image.fromarray(imagenMeta,"L")
##    imagen.show()

#LISTA
def cruzarPoblacion():
    global poblacionActual,poblacionAnterior,ordenada
    ordenada = ordenarMasApto(poblacionActual)
    poblacionActual = []
    poblacionAnterior = []
    contador = 0
    contador2 = 0
    indicador = 0
    for i in range(0,sizePoblacion//2): #Size de poblacion debe ser mayor a 4
        if i!=0 and tipoCruce%50!=0 and tipoCruce%25!=0 and i%2==0 and (contador+4)!=len(ordenada) :
            contador+=2
        #print("Iteracion: ",i,"\n1--> ",contador)
        imagen1 = ordenada[contador]
        poblacionAnterior.append(imagen1)
        contador+=1
        if tipoCruce%50 == 0:
            #print("\nTipo de cruce cambio\n")
            imagen2 = ordenada[((sizePoblacion//2)-1)+contador]
            poblacionAnterior.append(imagen2)            
##        if indicador%2 == 0:
##            imagen2 = ordenada[(((sizePoblacion//2)//2)-1)+contador2]
##            poblacionAnterior.append(imagen2)
##            contador2+=1
        
        else:
            imagen2 = ordenada[contador+1]
            poblacionAnterior.append(imagen2)
        #print("2--> ",contador+1)
        
        if random.randint(0,100) < probCruce:
            hijos = cruzarImagenes(imagen1,imagen2)
            nuevaImagen1 = hijos[0]
            nuevaImagen2 = hijos[1]
            poblacionActual.append(nuevaImagen1)
            poblacionActual.append(nuevaImagen2)
        else:
            poblacionActual.append(imagen1)
            poblacionActual.append(imagen2)
        indicador+=1
        
#LISTA
def cruzarImagenes(imagen1, imagen2):
    res = [None,None]
    corte = random.randint(1,len(imagen1)-1)
    res[0] = imagen1[:corte]+imagen2[corte:]
    res[1] = imagen2[:corte]+imagen1[corte:]
    return res

#LISTA
def menu():
    global sizePoblacion, probCruce, probMutacion
    print("Menu de Van Gogh\n") 
    rutaImagen = "a4.png"#input("Introduzca la ruta y nombre de la imagen: ")
    sizePoblacion = 10 #int(input("Introduzca el tamaño de la población: "))
    probCruce = float(input("Defina el % de probabilidad de cruce: "))
    probMutacion = float(input("Defina el % de probabilidad de mutación: "))
    cargarImagenMeta(rutaImagen)
    GenerarPoblacionInicial(sizePoblacion)
    print("\nIniciando...\n")
    iniciarAlgoritmo()

#LISTA
def GenerarPoblacionInicial(numImagenes):
    global poblacionActual
    imagen = []    
    while numImagenes > 0:
        for i in range(0,len(imagenMeta)):
            imagen.append([])
            for j in range(0,len(imagenMeta[i])):
                imagen[i].append([])
                imagen[i][j] = random.randint(0,255)        
        poblacionActual.append(imagen)
        imagen = []
        numImagenes -= 1
    print("\nPob. inicial creada...")

#LISTA
def terminado():
    if(simMasAptoPA) < 0.1:            
        return True
    return False

#LISTA
def mutarPoblacion():
    global poblacionActual
    global simMasAptoPA
    #poblacionTransicion = poblacionActual
    ordenada = ordenarMasApto(poblacionActual)
    poblacionActual = []
    imagen = []
    contMasApto = 0
    contMenosApto = 0
    indexImageMutadas = []
    indicador = 0
#    while poblacionTransicion != []:
    for i in range(0,len(ordenada)):
        if indicador%8 == 0:            
            #imagen = obtenerMasApto(poblacionTransicion)
            imagen = ordenada[contMasApto]
            imagen = mutarImagen(imagen)
            poblacionActual.append(imagen)
            contMasApto+=1
        elif indicador%3 == 0:     
            #imagen = obtenerMenosApto(poblacionTransicion)
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
        #poblacionTransicion.remove(imagen)
        
    masAptos.append(obtenerMasApto(poblacionActual))
    if simMasAptoPA == 1000:
        simMasAptoPA = compararImagen(imagenMeta,masAptos[len(masAptos)-1])                
    else:
        simMasAptoPAnt = simMasAptoPA
        simMasAptoPA = compararImagen(imagenMeta,masAptos[len(masAptos)-1])                
    print("La similitud del mas apto de esta generacion es: %f"%simMasAptoPA)

#LISTA
def mutarImagen(imagen):
    global generacion
    mutados = []       
    cantMutar = (((np.size(imagenMeta)/3)*probMutacion)//1)
    while len(mutados) < cantMutar:
        row = random.randint(0,len(imagenMeta)-1)
        column = random.randint(0,len(imagenMeta[0])-1)
        if [row,column] not in mutados:
            if (imagenMeta[row][column]-40-generacion)<0:
                imagen[row][column] = imagenMeta[row][column]
            elif (imagenMeta[row][column]+40-generacion)>255:
                imagen[row][column] = imagenMeta[row][column]
            else:
                imagen[row][column] = imagenMeta[row][column]
            mutados.append([row,column])
    return imagen

def mutarImagen1(imagen):
    mutados = []       
    cantMutar = (((np.size(imagenMeta)/3)*probMutacion)//1)
    posPixel = [None,None]
    posIntercambio = [None,None]
    while len(mutados) < cantMutar:
        posPixel[0] = random.randint(0,len(imagenMeta)-1)
        posPixel[1] = random.randint(0,len(imagenMeta[0])-1)
        posIntercambio[0] = random.randint(0,len(imagenMeta)-1)
        posIntercambio[1] = random.randint(0,len(imagenMeta[0])-1)
        valorPixel = imagen[posPixel[0]][posPixel[1]]
        valorIntercambio = imagen[posIntercambio[0]][posIntercambio[1]]
        imagen[posPixel[0]][posPixel[1]] = valorIntercambio
        imagen[posIntercambio[0]][posIntercambio[1]] = valorPixel
        mutados.append([posPixel[0],posPixel[1]])
    return imagen

#LISTA
def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

#LISTA
def compararImagen(imagen1,imagen2):
    avg = 0
    contador = 0
    for i in range(0,len(imagen1)):
        avg += entropiaDistance(imagen1[i],imagen2[i])
        contador+=len(imagen1)
    return avg/contador

#LISTA
def obtenerMasApto(poblacionActual):
    mejor = poblacionActual[0]
    for imagen in poblacionActual:
        mejorSim = compararImagen(imagenMeta,imagen)
        if compararImagen(imagenMeta,imagen) < compararImagen(imagenMeta,mejor):
            mejor = imagen
    return mejor

#LISTA
def obtenerMenosApto(poblacionActual):
    peor = poblacionActual[0]
    for imagen in poblacionActual:
        mejorSim = compararImagen(imagenMeta,imagen)
        if compararImagen(imagenMeta,imagen) > compararImagen(imagenMeta,peor):
            peor = imagen
    return peor

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
          for j in imagenSig[i]:
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

#LISTA
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

#LISTA    
def myKey(item):
    return item[len(item)-1]


def entropiaDistance(x,y):
    suma = 0
    for a, b in zip(x, y):
        if a-b < 0:
            suma+= a-b+255
        else:
            suma+= a-b
    return sqrt(suma)

##def cuadricularImagen():
##    global imagenMeta
##    for i in imagenMeta:
##        if 
menu()
