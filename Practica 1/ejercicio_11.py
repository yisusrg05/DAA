

def inicializarMatriz():
    while True:
        n = int(input("Introduce el tamaño del triangulo de Floyd: "))
        if 0 < n < 16:
            break
    matriz = [[0 for _ in range(5)] for _ in range(5)]
    return n, matriz


def rellenarFloydInverso(matriz, n):
    num = n
    fila, columna = 0, 0

    while num >= 1:
        if num > 10:
            fila = 0
            columna = posicionesColumnas[num]
            matriz[fila][columna] = num
        elif num > 6:
            fila = 1
            columna = posicionesColumnas[num]
            matriz[fila][columna] = num
        elif num > 3:
            fila = 2
            columna = posicionesColumnas[num]
            matriz[fila][columna] = num
        elif num > 1:
            fila = 3
            columna = posicionesColumnas[num]
            matriz[fila][columna] = num
        elif num == 1:
            fila = 4
            columna = posicionesColumnas[num]
            matriz[fila][columna] = num
        num -= 1


posicionesColumnas = {
    1: 0,
    2: 0,
    3: 1,
    4: 0,
    5: 1,
    6: 2,
    7: 0,
    8: 1,
    9: 2,
    10: 3,
    11: 0,
    12: 1,
    13: 2,
    14: 3,
    15: 4
}


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
rellenarFloydInverso(matriz, n)
printMatriz(matriz)
