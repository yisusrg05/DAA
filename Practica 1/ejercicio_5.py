

def inicializarTablero():
    matriz = [[0 for _ in range(8)] for _ in range(8)]
    return matriz


def inicializarJugador1(matriz):
    for i in range(3):
        for j in range(8):
            if (i + j) % 2 == 0:
                matriz[i][j] = 1
    return matriz


def inicializarJugador2(matriz):
    for i in range(5, 8):
        for j in range(8):
            if (i + j) % 2 == 0:
                matriz[i][j] = 2
    return matriz


def printTablero(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j + 1 == len(matriz[1]):
                print(matriz[i][j])
            else:
                print(matriz[i][j], end=" ")


tablero = inicializarTablero()
tablero = inicializarJugador1(tablero)
tablero = inicializarJugador2(tablero)
printTablero(tablero)
