import cv2
import numpy as np
import networkx as n
from networkx.algorithms import tree

def estaEnLaLista(elemento,array):
    for i in array:
        if np.array_equal(i,elemento):
            return True
    return False

# para cargar el mapa
mapa = cv2.imread('mapa3.png')
# pasamos la imagen a escala de grises
gray = cv2.cvtColor(mapa, cv2.COLOR_BGR2GRAY)
# muestro la imagen en escala de grises
cv2.imshow('mapa',gray)
cv2.waitKey(0)
# obtengo un binarizacion en blaco todos lo pixeles cuyo valor en sea entre 254 y 255
ret, th1 = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY)
# hago un kernel de 11x11 de unos. Los Kernels se acostumbra hacerse de tamaño no par y cuadrados
# para que se den una idea algo asi:
"""
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
"""
kernel = np.ones((11, 11), np.uint8)
# aplico un filtro de dilatacion. Este filtro hace que los puntos los puntos blancos se expandan
# probocando que algunos puntitos negros desaparecan #le pueden hacer un cv.imshow para que vean el resultado
th1 = cv2.dilate(th1, kernel, 1)
kernel = np.ones((11, 11), np.uint8)
# Despues aplico uno de erosion que hace lo opuesto al de dilatacion
th1 = cv2.erode(th1, kernel, 1)
# aplico un flitro gausiando de 5x5  para suavisar los bordes
th1 = cv2.GaussianBlur(th1, (5, 5), cv2.BORDER_DEFAULT)
# muestro como queda mi mapa
cv2.imshow('thres', th1)
cv2.waitKey(0)
# Aplico la deteccion de Esquinas de Harris. para mas informacion consulten https://docs.opencv.org/3.4/dc/d0d/tutorial_py_features_harris.html
dst = cv2.cornerHarris(th1, 2, 3, 0.05)
ret, dst = cv2.threshold(dst, 0.04 * dst.max(), 255, 0)
dst = np.uint8(dst)
ret, th2 = cv2.threshold(th1, 235, 255, cv2.THRESH_BINARY)
th2 = cv2.dilate(th2, kernel, 1)
# aqui devuelvo la imagen binarizada a tres canales
th2 = cv2.cvtColor(th2, cv2.COLOR_GRAY2BGR)
# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst, 30, cv2.CV_32S)
vertices = np.int0(centroids)

aux1 = vertices
aux2 = vertices
verticesConectados = []
aristas = []
peso = []
G = n.Graph()
# aqui voy a buscar cuales son las esquinas que estan conectadas
for h in range(len(aux1)):
    i = aux1[h]
    for k in range(h, len(aux2)):
        j = aux2[k]
        if not (i == j).all():
            medio = (i+j)/2
            Cuarto = (medio+j)/2
            Cuarto2 = (medio+i)/2
            p1=(j+Cuarto)/2
            p2=(i+Cuarto)/2
            p3=(medio+Cuarto)/2
            p4=(medio+Cuarto2)/2
            p5 = (j + Cuarto2) / 2
            p6 = (i + Cuarto2) / 2

            if (th2[int(medio[1])][int (medio[0])] == [255,255,255]).all() and \
            (th2[int(Cuarto[1])][int (Cuarto[0])]==[255,255,255]).all() and \
            (th2[int(Cuarto2[1])][int (Cuarto2[0])]==[255,255,255]).all() and \
            (th2[int(p1[1])][int(p1[0])] == [255, 255, 255]).all()  and \
            (th2[int(p2[1])][int(p2[0])] == [255, 255, 255]).all() and \
            (th2[int(p3[1])][int(p3[0])] == [255, 255, 255]).all() and \
            (th2[int(p4[1])][int(p4[0])] == [255, 255, 255]).all() and \
            (th2[int(p5[1])][int(p5[0])] == [255, 255, 255]).all() and \
            (th2[int(p6[1])][int(p6[0])] == [255, 255, 255]).all():
                costoArista = np.linalg.norm(i-j)

                aristas.append([i,j,costoArista])
                G.add_edge(tuple(i),tuple(j),weidth = costoArista)
                if not estaEnLaLista(i, verticesConectados):
                    verticesConectados.append(i)
                if not estaEnLaLista(j, verticesConectados):
                    verticesConectados.append(j)
                        # aqui deberian sacar los puntos de intermedios y verificar si i y j estan conectados
            # si estan conectados calcular el costo (la distancia en pixeles entre ellos usan teorema de pitagoras papá) y agregarlos al grafo
mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
sorted(sorted(e) for e in edgelist)
# aqui yo dibujo mis lineas de las aristas de color verde, el uno es el grueso de la linea
# arista[0]   y arista[1]  tienen la forma de [fila, columna]
for arista in edgelist:
    cv2.line(th2, tuple(arista[0]), tuple(arista[1]), (0,255,0), 1)
# aqui pinto los puntos de las esquinas que son circulos de de radio de 5 pixeles, el -1 indica que van rellenados los circulos
# point tiene la forma [fila, columna]
for point in vertices:
    cv2.circle(th2, (point[0], point[1]), 5, (255, 255, 0), -1)
    cv2.waitKey(1)

# aqui muestro como quedo de chingon el grafo
cv2.imshow('points', th2)
cv2.waitKey(0)

