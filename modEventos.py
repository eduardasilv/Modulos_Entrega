def con(ind1,sopa): 
    #ind 2 é um aleatorio dos "cincoprox (ind1,sopa)" 
    ind2=random.choice(cincoprox(ind1,sopa))
    ind3=novoind()
    ind3[0]=caminho(ind1)[:-1]+caminho(ind2)
    ind3[1]=[(posicao(ind1)[0]+posicao(ind2)[0])/2 , (posicao(ind1)[1]+posicao(ind2)[1])/2 , (posicao(ind1)[2]+posicao(ind2)[2])/2 ]
    ind3[2]=nID(sopa) 
    
    sopa.remove(ind1)
    sopa.remove(ind2)
    sopa.append(ind3)
    
    
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
