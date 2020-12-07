##INDIVIDUOS

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
