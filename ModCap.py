## CAP
def event(t,k,IDe):
    if k=="con" or k=="des" or k=="cis":
        return [t,k,IDe]
    else:
        return ("Erro do tipo de evento!")

def kind(e):
    if e[1]=="con" or e[1]=="des" or e[1]=="cis":
        return e[1]
    else:
        return ("Erro do tipo de evento!")

def time(e):
    return e[0]

def IDe(e):
    return e[2]

def addE(c,e):
    return [x for x in c if time(x)<time(e)] + [e] + [x for x in c if time(x)>time(e)]

def removeE(c,e):
    return [x for x in c if x!=e]

def nextE(c):       # current event no simulador
    if len(c)>0:
        return c[0]
    else:
        print("A cap está vazia")
        
def delE(cap):     # elimina da cap o current event no fim do ciclo
    if len(cap)>0:
        return cap[1:]
    else:
        print("Erro de delE! A cap está vazia")
