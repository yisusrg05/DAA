

def inicializarMatriz():
    while True:
        n = int(input("Introduce el tamaño de la matriz: "))
        if 0 < n < 11:
            break
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    return n, matriz


def rellenarInverso(matriz, n):
    k = 0
    for i in range(n):
        for j in range(n):
            matriz[i][j] = n * n - k
            k += 1


def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j + 1 == len(matriz[1]):
                if matriz[i][j] < 10:
                    print(f"{matriz[i][j]} ")
                else:
                    print(matriz[i][j])
            else:
                if matriz[i][j] < 10:
                    print(f"{matriz[i][j]} ", end=" ")
                else:
                    print(matriz[i][j], end=" ")


n, matriz = inicializarMatriz()
rellenarInverso(matriz, n)
printMatriz(matriz)
