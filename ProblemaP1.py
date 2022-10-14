

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

"""

def solve(i, j, k):
    if i >= n:
        return 0
    if dp[i][j][k] != -1:# memo法
        return dp[i][j][k]
    o = solve(i+1, j, k) # (1) 当前位置 不修改 最大子序列数目
    c = s[i] != t[0]     # 当前位置是否需要用t[0]修改
    if k >= c:           # 还有修改的机会
        o = max(o, solve(i+1, j+1, k-c)) # (2) 使用t[0]修改之后最大子序列数目
    c = s[i] != t[1]     
    if k >= c:           
        o = max(o, solve(i+1, j+(t[0] == t[1]), k-c) + j) 
    dp[i][j][k] = o      
    return o
 
n, k = map(int, input().split())
s = input()
t = input()
 
dp = [[[-1] * (n+1) for _ in [0]*n] for _ in [0]*n]
 
print(solve(0, 0, k))

"""


def subSeqDif(ind,prim,kRes,X,Y):
    n = len(X)
    DP = [[[-1] * (n+1) for _ in [0]*n] for _ in [0]*n]
    if (ind >= n):
        return 0
    if (not (DP[ind][prim][kRes] == -1)):
        return DP[ind][prim][kRes]
    sol = subSeqDif(ind+1,prim,kRes,X,Y)
    cond = (not (X[ind] == Y[0]))
    if kRes >= cond:
        sol = max(sol, subSeqDif(ind+1, prim+1, kRes-cond,X,Y))
    cond = (not (X[ind] == Y[1]))
    cond2 = (not (X[ind] == Y[1]))
    if kRes >= cond:
        sol = max(sol, prim + subSeqDif(ind+1, prim+cond2, kRes-cond,X,Y))
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
        resultado = subSeqDif(0,0,m,X,Y)
    return resultado


print(consola(['ccqq','qc','2']))
