def notas(*n, sit=False):
    r={}
    r['total']=len(n)
    r['média']=sum(n)/len(n)
    r['maior']=max(n)
    r['menor']=min(n)
    if sit:
        if r['média'] >= 7:
            r['situação']='BOA'
        elif r['média'] >= 5:
            r['situação']='RAZOÁVEL'
        else:
            r['situação']='RUIM'
    return r




resp = notas(5.5,7,10,3.6,sit=True)
print(resp)