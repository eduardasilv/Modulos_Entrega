import random
from math import log
from math import sqrt
from math import inf

##GRAFOS
# g=[[1,2,3,4],[[1,2],[1,3],[2,3],[3,2],[2,4],[3,4]]]
# nos(g)=[1,2,3,4]
# arestas(g)= [[1,2],[1,3],[2,3],[3,2],[2,4],[3,4]]

def nos(g):
    return g[0]

def arestas(g):
    return g[1]

def copias(g,k): #cada elemento de "copias" é um individuo inicial
    r=[]
    for x in arestas(g):
        r+=[x]*k
    for i in range(len(r)):
        r[i]= [r[i],[], i+1]
    return r

def numnos(g):
    return len(nos(g))



### INDIVIDUOS
#    individuo = [caminho, pos]
#    pos=[x,y,z]
#    caminho=[lista de nos por onde passa]
#    comprimento de individuo = len(individuo[0])

def ind(caminho, pos,ID):
    return [caminho, pos,ID]

def caminho(ind):
    return ind[0] # = len(caminho(ind))

def posicao(ind):
    return ind[1]

def ID(ind):
    return ind[2]

def size(ind):
    return len(ind[0])

def novoind():
    return[[],[],[]]

def first(ind):
    return caminho(ind)[0]

def last(ind):
    return caminho(ind)[-1]

def od(ind,o,d):
    if first(ind)!=o or last(ind)!=d:
        return False
    else:
        return True
    
def length(ind,g):
    if size(ind)!=numnos(g):
        return False
    else:
        return True
    
def todos(ind,g):
    ok=True 
    for x in nos(g):
        if x not in caminho(ind):
            ok=False
    return ok

def hamilton(ind,g,o,d):
    if od(ind,o,d) and length(ind,g) and todos(ind,g):
        return True
    else:
        return False
    

#SOPA

def exprandom(m):
    x=random()
    return -m*log(x)


##TEMOS DE MUDAR PARA RANDOM UNIFORM
def posInicial(g,k): #equivale as condicoes da sopa inicialmente
    r= copias(g,k)
    sopa=[]
    listapos=[]
    for copia in r:
        [caminho,pos,ID]=copia
        pos= [float("{:.8f}".format(random())), float("{:.8f}".format(random())), float("{:.8f}".format(random()))]
        while pos in listapos:
            pos= [float("{:.8f}".format(random())), float("{:.8f}".format(random())), float("{:.8f}".format(random()))]
        sopa += [[caminho,pos,ID]]
        listapos += [pos]
    return sopa

def conjposicoes(sopa): #lista de todas as coordenadas utilizadas ate agora
    c=[]
    for individuo in sopa:
        c=c+[posicao(individuo)]
    return c

def conjIDS(sopa):
    r=[]
    for individuo in sopa:
        r=r+[ID(individuo)]
    return r

def nID(sopa):
    return conjIDS(sopa)[-1]+1
    
def distancia(ind1,ind2):
    [x1,y1,z1] = posicao(ind1)
    [x2,y2,z2] = posicao(ind2)
    distancia =sqrt(((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2))   
    return distancia

def listacomp(ind,sopa):
    listac=[]
    for individuo in sopa:
        if last(ind) == first(individuo) and (ind1 != individuo):
            listac+=[individuo]
    return listac
     
def maisprox(ind1,sopa):
    d=+inf
    m=[]
    for individuo in listacomp(ind1,sopa):
          if distancia(ind1,individuo)<=d:
              d=distancia(ind1,individuo)
              m=individuo
    return m

def cincoprox(ind1,sopa):
    cinco=[]
    falta=listacomp(indd1,sopa)
    while len(cinco)<5 and falta!=[]:
        cinco=cinco + [maisprox(ind1,falta)]
        falta.remove(maisprox(ind1,falta))
    return cinco     
            
### EVENTOS:: concatenação,deslocação, cisão ("con", "des", "cis")

def con(ind1,sopa): 
    #ind 2 é um aleatorio dos "cincoprox (ind1,sopa)" 
    ind2=random.choice(cincoprox(ind1,sopa))
    ind3=novoind()
    ind3[0]=caminho(ind1)[:-1]+caminho(ind2)
    ind3[1]=[(posicao(ind1)[0]+posicao(ind2)[0])/2 , (posicao(ind1)[1]+posicao(ind2)[1])/2 , (posicao(ind1)[2]+posicao(ind2)[2])/2 ]
    ind3[2]=nID(sopa) 
    return ind3

def des(ind):
    
    x=posicao(ind)[0]
    y=posicao(ind)[1]
    z=posicao(ind)[2]
    
    c=size(ind)
    
    novox=float("{:.8f}".format(random.uniform(x-(1/c), x+(1/c))))
    novoy=float("{:.8f}".format(random.uniform(y-(1/c), y+(1/c))))
    novoz=float("{:.8f}".format(random.uniform(z-(1/c), z+(1/c))))
    while novox>1 or novox<0 or novoy>1 or novoy<0 or novoz>1 or novoz<0:
        novox=float("{:.8f}".format(random.uniform(x-(1/c), x+(1/c))))
        novoy=float("{:.8f}".format(random.uniform(y-(1/c), y+(1/c))))
        novoz=float("{:.8f}".format(random.uniform(z-(1/c), z+(1/c))))            
    ind = [caminho(ind), [novox,novoy,novoz], ID(ind)]
    return ind
    
        
        

#sopa = lista de todos os individuos na solução da simulação
    
def final(sopa,g,o,d):
    r=[]
    for individuo in sopa:
        if hamilton(individuo,g,o,d):
            r+=[[caminho(individuo)]]
    return r



## CAP
def event(t,k):
    if k=="con" or k=="des" or k=="cis":
        return [t,k]

def kind(e):
    return e[1]

def time(e):
    return e[0]

def addE(c,e):
    return [x for x in c in time(x)<time(e)] + [e] + [x for x in c in time(x)>time(e)]
