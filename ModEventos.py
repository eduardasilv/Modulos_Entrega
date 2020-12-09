### EVENTOS:: concatenação,deslocação, cisão ("con", "des", "cis")
import random
import ModInd as i
import ModSopa as sp

def exprandom(m):
    x=random()
    return -m*log(x)

def con(ind1,sopa): 
    #ind 2 é um aleatorio dos "cincoprox (ind1,sopa)" 
    ind2=random.choice(sp.cincoprox(ind1,sopa))
    
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
    
        
