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

def compativeis(ind1,ind2):
    if last(ind1) == first(ind2):
        r=True
    else:
        r=False
    return r  

def listacomp(sopa,ind):
    listac=[]
    for individuo in sopa:
        if last(ind) == first(individuo):
            listac+=[individuo]
    return listac
     
def maisprox(ind1,sopa):
    d=+inf
    m=[]
    for individuo in listacomp(sopa,ind1):
          if distancia(ind1,individuo)<=d:
              d=distancia(ind1,individuo)
              m=individuo
    return m

def cincoprox(ind1,sopa):
    cinco=[]
    falta=listacomp(sopa,ind1)
    while len(cinco)<5 and falta!=[]:
        cinco=cinco + [maisprox(ind1,falta)]
        falta.remove(maisprox(ind1,falta))
    return cinco     
