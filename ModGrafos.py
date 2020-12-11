##GRAFOS
def newgraph(wnos):
    return [[wnos],[]]

def jaresta(g,i,j):
    [wnos,w]=g
    w=w+[(i,j)]
    return [wnos,w]

def nos(g):
    return g[0]

def arestas(g):
    return g[1]

def copias(g,k): #cada elemento de "copias" é um individuo inicial
    r=[]
    for x in arestas(g):
        r+=[x]*k
    for j in range(len(r)):
        r[j]= [r[j],[], j+1]
    return r

def numnos(g):
    return len(nos(g))
