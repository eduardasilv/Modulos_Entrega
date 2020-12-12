    
def posInicial(g,k): #equivale as condicoes da sopa inicialmente.  #???? nao sei 
   
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
    

def exprandom(m):
    x=random.uniform(0,1)
    return -m*log(x)







def con(ind1,ind2,sopa): 
    #ind 2 é um aleatorio dos "cincoprox (ind1,sopa)" 
    ind3=i.novoind()
    ind3=i.novocaminho(ind3,i.caminho(ind1)[:-1]+i.caminho(ind2))
    ind3=i.novapos(ind3,[(i.posicao(ind1)[0]+i.posicao(ind2)[0])/2 , (i.posicao(ind1)[1]+i.posicao(ind2)[1])/2 , (i.posicao(ind1)[2]+i.posicao(ind2)[2])/2 ])
    ind3=i.novoID(ind3,i.nID(sopa))
    return ind3

def des(ind):

    x=i.posicao(ind)[0]
    y=i.posicao(ind)[1]
    z=i.posicao(ind)[2]
    
    c=i.size(ind)
    
    novox=float("{:.8f}".format(random.uniform(x-(1/c), x+(1/c)))) 
    novoy=float("{:.8f}".format(random.uniform(y-(1/c), y+(1/c))))
    novoz=float("{:.8f}".format(random.uniform(z-(1/c), z+(1/c))))
    while novox>1 or novox<0:
        novox=float("{:.8f}".format(random.uniform(x-(1/c), x+(1/c))))
    while novoy>1 or novoy<0 :
        novoy=float("{:.8f}".format(random.uniform(y-(1/c), y+(1/c))))
    while novoz>1 or novoz<0:
        novoz=float("{:.8f}".format(random.uniform(z-(1/c), z+(1/c))))
    pos=[novox,novoy,novoz]        
    ind=i.novapos(ind,pos)
    return ind

def cisao(sopa,g):
    
    for individuo in sopa:
        
        if i.size(individuo) > g.numnos(g):
            
            s=int(random.uniform(2,g.numnos(g)/2))
            while i.size(individuo)-s < 2:    
                s=int(random.uniform(2,g.numnos(g)/2))  #novo len do caminho que é escolhido aleatoriamente entre 2 e metade do desejado  
                      
            ind1=i.novoind()
            ind1=i.novocaminho(ind1,i.caminho(individuo)[:s+1])
            ind1=i.novapos(ind1,[float("{:.8f}".format(random.uniform(0,1))), float("{:.8f}".format(random.uniform(0,1))), float("{:.8f}".format(random.uniform(0,1)))])
            ind1=i.novoID(ind1,sp.nID(ind1,sopa))
            sopa = sp.addS(ind1,sopa)
            
            ind2=i.novoind()
            ind2=i.novocaminho(ind2,i.caminho(individuo)[s:])
            ind2=i.novapos(ind2,[float("{:.8f}".format(random.uniform(0,1))), float("{:.8f}".format(random.uniform(0,1))), float("{:.8f}".format(random.uniform(0,1)))])
            ind2=i.novoID(ind2,sp.nID(ind2,sopa))
            sopa = sp.addS(ind2,sopa)
            
            sopa = sp.removeS(individuo,sopa)
       
    return sopa
        
 
