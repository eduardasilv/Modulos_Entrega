#SOPA
import random
import ModGrafos as gr
import ModInd as i

def newsp():
    return []

def addS(ind,sopa):
    sopa+=[ind]
    return sopa

def removeS(ind,sopa):
    return [x for x in sopa if x!=ind]

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

