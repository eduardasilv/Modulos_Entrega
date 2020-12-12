### INDIVIDUOS
#    pos=[x,y,z]
#    caminho=[lista de nos por onde passa]
#    comprimento de individuo = len(individuo[0])


def ind(caminho, pos,ID):
    return [caminho, pos, ID]

def novoind():
    return[[],[],[]]

def novocaminho(ind,caminho):
    ind[0]=caminho
    return ind

def novapos(ind,pos):
    ind[1]=pos
    return ind

def novoID(ind,ID):
    ind[2]=ID
    return ind

def caminho(ind):
    return ind[0] # = len(caminho(ind))

def posicao(ind):
    return ind[1]

def ID(ind):
    return ind[2]

def size(ind):
    return len(caminho(ind))

def first(ind):
    return caminho(ind)[0]

def last(ind):
    return caminho(ind)[-1]
