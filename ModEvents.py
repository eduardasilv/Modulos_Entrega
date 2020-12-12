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
