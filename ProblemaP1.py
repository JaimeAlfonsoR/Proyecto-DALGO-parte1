

#Caso - la cadena de la subsecuencia tiene las dos mismas letras


def conteoOcurrencias(X,Y,m):
    conteo = 0
    n = len(X)
    for i in range(0, n):
        if (X[i] == Y[0]):
            conteo = conteo + 1
    #El número de reemplazos no puede exceder al de la cadena 
    conteo = min(n, conteo+m)
    #Definición Sumatoria
    return ((conteo-1)*conteo)/2


def subSeqDif(ind,prim,kRes,X,Y,DP):
    n = len(X)
    if (ind >= n):
        return 0
    if (not (DP[ind][prim][kRes] == -1)):
        return DP[ind][prim][kRes]
    sol = subSeqDif(ind+1,prim,kRes,X,Y,DP)
    cond = (not (X[ind] == Y[0]))
    if kRes >= cond:
        sol = max(sol, subSeqDif(ind+1, prim+1, kRes-cond,X,Y,DP))
    cond = (not (X[ind] == Y[1]))
    cond2 = (Y[0] == Y[1])
    if kRes >= cond:
        sol = max(sol, prim + subSeqDif(ind+1, prim+cond2, kRes-cond,X,Y,DP))
    DP[ind][prim][kRes] = sol
    return sol



def consola(l:list):
    X = l[0]
    Y = l[1]
    m = int(l[2])
    n = len(X)
    if (Y[0] == Y[1]):
        resultado = conteoOcurrencias(X,Y,m)
    else:
        DP = [[[-1] * (n+1) for _ in [0]*n] for _ in [0]*n]
        resultado = subSeqDif(0,0,m,X,Y,DP)
    return resultado


print(consola(['qwertyhgfdsazxc','qa','6']))
