def sim(g,o,d,k,limite,tbc,tbd,tbz):
 
    sopa = posInicial(g,k)
 
    c=[]
    for x in conjIDS(sopa):
        c = addE(c,[event(exprandom(tbc),"con",x)])
        c = addE(c,[event(exprandom(tbd),"des",x)])
    c = addE(c,[event(exprandom(tbz),"cis",0)])

    ce = nextE(c)    #current event
    ct = time(ce)  #current time = agora
    ck = kind(ce)  #current kind
    cid = IDe(ce)  #current IDe

    while ct <= limite:

        if ck == "con":
            "Modulo concatenacao"
            c=addE(c,event(ct+random(tbc),"con",cid))

        elif ck == "des":
            "Modulo deslocamento"
            c=addE(c,event(ct+random(tbc),"des",cid))
        else:
            "Modulo cisão"
            c=addE(c,event(ct+random(tbz),"cis",0))

        ce = nextE(c)
        ct = time(ce)
        ck = kind(ce)
        cid = IDe(ce)
        c=delE(c)
