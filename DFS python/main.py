import random
import math

G = []
color = []
d = []
pi = []
time = 0
tam = 0

def DFS():
  global tam, G, color, d, pi, time
  
  for u in range(tam):
    color.append('w')
    d.append(0)
    pi.append('')

  time = 0

  for u in range(tam):
    if color[u] == 'w':
      DFS_visita(u)

def DFS_visita(U):
  global tam, G, color, d, pi, time

  color[U] = 'g'
  time += 1
  d[U] = time

  for v in range(tam):
    if(G[U][v]==1 and color[v]=='w'):
      pi[v] = U
      DFS_visita(v)

  color[U] = 'b'
    
  
#MAIN
tam = int(input("Insira a quantidade de vértices do grafo: "))

manual = input("\nDeseja inserir sua matriz de adjacencias manualmente[S/N]?\nCaso contrario, sera gerada uma matriz M[tam x tam] aleatória\n\n")
if manual.upper()=="S":
    for i in range(tam):
        G.append([])
        for j in range(tam):
            entrada = int(input("G[{}][{}] = ".format(i,j)))
            G[i].append(entrada)
else:
    """
    Loop para atribuições aleatórias de 0 ou 1 na matriz de adjacências de um grafo
    """
    linha = "\nMatriz:\n\n"
    for i in range(tam):
        linha += "|"
        G.append([])
        for j in range(tam):
            G[i].append(random.randint(0,1))
            linha += str(G[i][j]) + "|"
        linha+="\n"
    
    #Impressão da matriz de adjacências para o usuario
    print(linha)
DFS()
print("\nd: "+str(d))
print("pi: "+str(pi))
print("c: "+str(color))