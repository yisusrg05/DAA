

def inicializarMatriz():
    while True:
        n = int(input("Introduce el tamaño de la matriz: "))
        if 0 < n < 11:
            break
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    return n, matriz


def distanciaBordes(matriz, n):
    maxDistancia = int(n / 2)
    k = 1
    while k <= maxDistancia:
        for i in range(k, n - k):
            for j in range(k, n - k):
                if i - k == 0 or j - k == 0 or i + k == n - 1 or j + k == n - 1:
                    matriz[i][j] = k
        k += 1


def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j + 1 == len(matriz[1]):
                print(matriz[i][j])
            else:
                print(matriz[i][j], end=" ")


n, matriz = inicializarMatriz()
distanciaBordes(matriz, n)
printMatriz(matriz)

