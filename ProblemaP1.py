
import sys
import time

#Caso - la cadena de la subsecuencia tiene las dos mismas letras
def conteoOcurrencias1(X,Y,m):
    conteo = 0
    #Longitud de la cadena X
    n = len(X)
    for i in range(0, n):
        if (X[i] == Y[0]): #Si el elemento de la cadena es igual al primer elemento de la subcadena
            conteo = conteo + 1
    #El número de reemplazos no puede exceder al de la cadena 
    conteo = min(n, conteo+m)
    #Definición Sumatoria
    return int(((conteo-1)*conteo)/2)

#Caso - la cadena de la subsecuencia tiene diferentes letras
def conteoOcurrencias2(ind,prim,mRes,X,Y,DP):
    #Longitud de la cadena X
    n = len(X)
    #El programa termina de ejecutarse
    if (ind >= n):
        return 0
    #Continuar el programa
    if (not (DP[ind][prim][mRes] == -1)):
        return DP[ind][prim][mRes]
    #Avance en el indice de la cadena
    sol = conteoOcurrencias2(ind+1,prim,mRes,X,Y,DP)
    #Booleano - el elemento del indice es diferente que el primer elemento de la subcadena
    cond = (not (X[ind] == Y[0]))
    if mRes >= cond: #Si aún quedan reemplazos por hacer 
        #Si se cumple la condición, se hace el reemplazo por el primer elemento de la subcadena
        sol = max(sol, conteoOcurrencias2(ind+1, prim+1, mRes-cond,X,Y,DP))
    #Condición, el elemento es diferente al segundo elemento de la subcadena
    cond = (not (X[ind] == Y[1]))
    #Condición, el primer elemento de la subcadena es igual al segundo elemento - problema de conteoOcurrencias()
    cond2 = (Y[0] == Y[1])
    if mRes >= cond: #Si aún quedan reemplazos por hacer
        #Si se cumple la condición, se hace el reemplazo por el segundo elemento de la subcadena
        sol = max(sol, prim + conteoOcurrencias2(ind+1, prim+cond2, mRes-cond,X,Y,DP)) 
    DP[ind][prim][mRes] = sol #Añadir a la matriz DP
    return sol


#Función para evaluar por casos
def conteoOcurrencias(l:list):
    X = l[0]
    Y = l[1]
    m = int(l[2])
    n = len(X)
    if (Y[0] == Y[1]):
        resultado = conteoOcurrencias1(X,Y,m)
    else:
        DP = [[[-1] * (n+1) for _ in [0]*n] for _ in [0]*n]
        #Empezar desde indice 0, conteo 0 y m reemplazos restantes
        resultado = conteoOcurrencias2(0,0,m,X,Y,DP)
    return resultado


#Función para compilar los datos
def main():
    linea = sys.stdin.readline() 
    casos = int(linea)
    linea = sys.stdin.readline()
    sumaT = 0
    for i in range(0,casos):
       numeros = [num for num in linea.split()]
       start = (time.time())
       respuesta = conteoOcurrencias(numeros)
       end = (time.time())
       sumaT = sumaT + (end - start) #Tiempo acumulado
       print((respuesta))
       linea = sys.stdin.readline()
    print("Time: "+ str(sumaT))

    
main()

