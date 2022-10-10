from string import whitespace


grafo = {1: [[2,3,4],[5,3,7],0,0],
       	 2: [[5,6,3,1],[7,3,3,5],0,0],
         3: [[6,7,4,1],[2,3,3,3],0,0],
         4: [[7,3,1],[2,3,7],0,0],
         5: [[8,6,2],[2,2,7],0,0],
         6: [[8,9,5,7,3,2],[2,3,2,2,2,3],0,0],
         7: [[9,4,6,3],[2,2,2,3],0,0],
         8: [[10,9,6,5],[5,5,2,2],0,0],
         9: [[10,8,6,7],[1,5,3,2],0,0],
        10: [[8,9],[5,1],0,0]
	}
inicio = int(input("En que nodo inicias?\n"))
fin = int(input("En que nodo Terminas?\n"))
recorrido=[inicio]
costo=0
destino=[fin]
camino = []
print(grafo)
for each_nodo in recorrido:
    for i in grafo[each_nodo][0]:
        if i not in recorrido:
            recorrido.append(i)
            
            for each_nodo in recorrido:
                for conneccion_number in range(len(grafo[each_nodo][0])):
                    #print(grafo[each_nodo][1][conneccion_number])
                    #print(grafo[grafo[each_nodo][0][conneccion_number]][2])
                    #print(grafo[each_nodo][2])
                    if grafo[grafo[each_nodo][0][conneccion_number]][2] == 0 or grafo[grafo[each_nodo][0][conneccion_number]][2] > grafo[each_nodo][2] + grafo[each_nodo][1][conneccion_number]:
                        if grafo[each_nodo][0][conneccion_number] != inicio:
                            grafo[grafo[each_nodo][0][conneccion_number]][2] =  grafo[each_nodo][2] + grafo[each_nodo][1][conneccion_number]  
                            grafo[grafo[each_nodo][0][conneccion_number]][3] = each_nodo

print(grafo)

recorrido.reverse

camino.append(fin)
while(True):
    if fin == inicio:
        break

    camino.append(grafo[fin][3])
    fin = grafo[fin][3]

print(camino)

