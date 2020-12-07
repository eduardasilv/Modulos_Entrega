def event(t,k):
    if k=="con" or k=="des" or k=="cis":
        return [t,k]

def kind(e):
    return e[1]

def time(e):
    return e[0]

def addE(c,e):
    return [x for x in c if time(x)<time(e)] + [e] + [x for x in c if time(x)>time(e)]
