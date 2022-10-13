

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

#No sirve nada aún
"""
#Caso - la cadena tiene letras diferentes
def sol(ind,mRes,prim,X,Y):
    n = len(X)
    #Inicializar matriz DP con -1
    matPrim = [-1]*1000
    matResK = [matPrim]*1000
    matInd = [matResK]*1000


    terminado = False
    resultado = 0
    r = 0
    r1 = 0
    r2 = 0
    r3 = 0

    while (not terminado):
        if (ind == n): #Ultima comparacion
            terminado = True
        if (mRes == 0):
            if (X[ind] == Y[1]):
                r = prim + sol(ind+1,0,prim,X,Y)
            else:
                if (X[ind]==Y[0]):
                    r = sol(ind+1,0,prim+1,X,Y)
                else:
                    r = sol(ind+1,0,prim,X,Y)
        else:
            if (X[ind] == Y[0]):
                r1 = sol(ind+1,mRes,prim+1,X,Y)
                r2 = prim + sol(ind+1,mRes-1,prim,X,Y)
                r = max(r1,r2)
            elif (X[ind] == Y[1]):
                #Decisión - dejar el string como está o cambiarlo por el primer elemento
                r1 = sol(ind+1,mRes-1,prim+1,X,Y)
                r2 = prim + sol(ind+1,mRes,prim,X,Y)
                r = max(r1,r2)
            else:
                #Decidir para cambio entre el primer elemento o el segundo elemento
                r1 = sol(ind+1,mRes,prim,X,Y)
                r2 = prim+sol(ind+1,mRes-1,prim,X,Y)
                r3 = sol(ind+1,mRes-1,prim+1,X,Y)
                r = max(r1,max(r2,r3))

        matInd[ind][mRes][prim] = r

    return matInd[n-1][n-1][n-1]

def consola(X, Y, m):
    if (Y[0] == Y[1]):
        conteoOcurrencias(X,Y,m)
    else:
        sol(0,m,0,X,Y)


X = 'qcqc'
Y = 'qc'
m = 2
print(consola(X,Y,m))

"""