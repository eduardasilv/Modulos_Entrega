#SELEÇÃO
import ModGrafos as gr
import ModInd as i

def od(ind,o,d):
    if i.first(ind)!=o or i.last(ind)!=d:
        return False
    else:
        return True
    
def length(ind,g):
    if i.size(ind)!=gr.numnos(g):
        return False
    else:
        return True
    
def todos(ind,g):
    ok=True 
    for x in gr.nos(g):
        if x not in i.caminho(ind):
            ok=False
    return ok   

def hamilton(ind,g,o,d):
    if od(ind,o,d) and length(ind,g) and todos(ind,g):
        return True
    else:
        return False
    
def final(sopa,g,o,d):
    r=[]
    for individuo in sopa:
        if hamilton(individuo,g,o,d):
            r+=[[i.caminho(individuo)]]
    return r
