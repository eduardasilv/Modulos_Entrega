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
def final(sopa,g,o,d):
    r=[]
    for individuo in sopa:
        if hamilton(individuo,g,o,d):
            r+=[[caminho(individuo)]]
    return r
