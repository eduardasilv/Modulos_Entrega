import random
import ModInd as i
import ModSopa as sp
import ModEvents as ev
import ModGrafos as gr
import ModSelecao as sel
import ModCap as cap
import ModOperacoes as op


def sim(g,o,d,k,limite,tbc,tbd,tbz):
 
    sopa = op.cond_iniciais(g,k)
 
    c=[]
    for x in sp.conjIDS(sopa):
        c = cap.addE(c,ev.event(op.exprandom(tbc),"con",x))
        c = cap.addE(c,ev.event(op.exprandom(tbd),"des",x))
    c = cap.addE(c,ev.event(op.exprandom(tbz),"cis",0))

    ce = cap.nextE(c)    #current event
    ct = ev.time(ce)  #current time = agora
    ck = ev.kind(ce)  #current kind
    cid = ev.IDe(ce)  #current IDe

    while ct <= limite:

        if ck == "con":
            for individuo in sopa:
                if i.ID(individuo)==cid:
                    ind1=individuo
            ind2=random.choice(op.cincoprox(ind1,sopa))
    
            "Modulo concatenacao"
            ind3 = op.con(ind1,ind2,sopa)
            sopa = sp.removeS(ind1,sopa)
            sopa = sp.removeS(ind2,sopa)
            sopa = sp.addS(ind3,sopa)
            c = cap.addE(c,ev.event(ct+op.exprandom(tbc),"con",i.ID(ind3)))
            c = cap.addE(c,ev.event(ct+op.exprandom(tbd),"des",i.ID(ind3)))
            # eliminar da cap os eventos previstos 
            for evt in c:
                if ev.IDe(evt)==i.ID(ind1) or ev.IDe(evt)==i.ID(ind2):
                    c = cap.removeE(c,evt)
            
        elif ck == "des":
            "Modulo deslocamento"
            c= cap.addE(c,ev.event(ct+op.exprandom(tbc),"des",cid))
        else:
            "Modulo cisão"
            c= cap.addE(c,ev.event(ct+op.exprandom(tbz),"cis",0))

        ce = cap.nextE(c)
        ct = ev.time(ce)
        ck = ev.kind(ce)
        cid = ev.IDe(ce)
        c = cap.delE(c)
