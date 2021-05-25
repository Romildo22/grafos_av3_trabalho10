import csv
import math
class grafo:
   def __init__(self, matriz,ids):
    self.matriz = matriz
    self.ids = ids


def lerCSV(caminho):
    matriz = []
    with open(caminho) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        ids = csv_reader.__next__()
        ids.pop(0)
        for row in csv_reader:
            aux = []
            for a in row[1:]:
                if(a=="i"):
                    aux.append(math.inf)
                else:
                    aux.append(int(a))
            matriz = matriz + [aux]
    return grafo(matriz, ids)


def bellmanFord(s, grafo):
    d = []*len(grafo.matriz)
    p = [-1]*len(grafo.matriz)
    for i in range(len(grafo.matriz)):
            d.append(math.inf)     
    d[s] = 0
    
    for i in range(len(grafo.matriz)-1):
        c = 0
        for j in range(len(grafo.matriz)):
            if(d[j] != math.inf):
                for k in range(len(grafo.matriz)):
                    if(grafo.matriz[j][k]!=math.inf):
                        soma = d[j] + grafo.matriz[j][k]
                        if(soma<d[k]):
                            d[k] = soma
                            p[k] = j
                            c = 1
        if(c==0):
            break
    for i in range(len(grafo.matriz)):
        for j in range(len(grafo.matriz)):
            if(grafo.matriz[i][j] != math.inf and d[i] != math.inf and d[j]>d[i] + grafo.matriz[i][j]):
                print("Grafo possui ciclo negativo")
                print(i)
                return
                
    printDistances(d, p, s, grafo)
                    
          

def printDistances(distance, previous, s, grafo):
    print("**********************************************")
    print("Distancias a partir do vertice ", grafo.ids[s], end="\n\n")
    for i in range (len(distance)):
        route = []
        aux = previous[i]
        while(aux != -1):
            route.append(aux)
            aux = previous[aux]
        route.reverse()
        print("Vertice ", grafo.ids[i]," = ", distance[i])
        for r in route:
            print(grafo.ids[r], " => ", end="")
        print(grafo.ids[i])
        print("-----------------------------------------------")

                

# 9.2
# grafo2 = lerCSV("Atividade 10\Atividade 10 - Grafos - 9.2.csv")
# bellmanFord(6, grafo2)

# 9.3
# grafo3 = lerCSV("Atividade 10\Atividade 10 - Grafos - 9.3.csv")
# bellmanFord(5, grafo3)

# #teste
# grafoTeste = lerCSV("Atividade 10\grafo_ciclo_negativo.csv")
# bellmanFord(0, grafoTeste)
