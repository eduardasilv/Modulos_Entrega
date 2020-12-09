#SOPA
import random
from math import log
from math import sqrt
from math import inf
import ModGrafos as gr
import ModInd as i

def exprandom(m):
    x=random()
    return -m*log(x)


def posInicial(g,k): #equivale as condicoes da sopa inicialmente
    r = gr.copias(g,k)
    sopa=[]

    for copia in r:
        a=i.novoind()
        a=i.novocaminho(a,i.caminho(copia))
        a=i.novoID(a,i.ID(copia))
        pos=[float("{:.8f}".format(random.uniform(0,1))), float("{:.8f}".format(random.uniform(0,1))), float("{:.8f}".format(random.uniform(0,1)))]
        a=i.novapos(a,pos)
        sopa=sopa+[a]

    return sopa

def conjposicoes(sopa): #lista de todas as coordenadas utilizadas ate agora
    c=[]
    for individuo in sopa:
        c=c+[i.posicao(individuo)]
    return c

def conjIDS(sopa):
    r=[]
    for individuo in sopa:
        r=r+[i.ID(individuo)]
    return r

def nID(sopa):
    return conjIDS(sopa)[-1]+1

def addS(ind,sopa):
    sopa+=[ind]
    return sopa

def removeS(ind,sopa):
    return [x for x in sopa if x!=ind]
    
def distancia(ind1,ind2):
    [x1,y1,z1] = i.posicao(ind1)
    [x2,y2,z2] = i.posicao(ind2)
    distancia =sqrt(((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2))   
    return distancia

def listacomp(ind,sopa):
    listac=[]
    for individuo in sopa:
        if i.last(ind) == i.first(individuo) and (ind != individuo):
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
    falta=listacomp(ind1,sopa)
    while len(cinco)<5 and falta!=[]:
        cinco=cinco + [maisprox(ind1,falta)]
        falta.remove(maisprox(ind1,falta))
    return cinco     
            