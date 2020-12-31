## CAP
import ModEvents as ev

def addE(c,e):
    return [x for x in c if ev.time(x)<ev.time(e)] + [e] + [x for x in c if ev.time(x)>ev.time(e)]

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
def conjIDcap(cap):
    res=[]
    for evt in cap:
        if ev.IDe(evt) not in res:
            res=res+[ev.IDe(evt)]
    return res
