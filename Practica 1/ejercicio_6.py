

def inicializarTablero():
    matriz = [[0 for _ in range(8)] for _ in range(8)]
    return matriz


def elegirFicha():
    ficha = input("Elige ficha (torre/alfil): ")
    while ficha != "torre" and ficha != "alfil":
        ficha = input("Elige ficha (torre/alfil): ")
    ficha_numero = 0
    if ficha == "torre":
        ficha_numero = 1
    elif ficha == "alfil":
        ficha_numero = 2
    return ficha_numero


def elegirPosicion(matriz, ficha):
    x = int(input("Elige posición x: "))
    while x < 1 or x > 8:
        x = int(input("Elige posición x: "))
    y = int(input("Elige posición y: "))
    while y < 1 or y > 8:
        y = int(input("Elige posición y: "))
    matriz[x-1][y-1] = ficha
    return x - 1, y - 1


def posiblesPosiciones(matriz, x, y, ficha):
    if ficha == 1:
        for i in range(8):
            for j in range(8):
                if i == x or j == y:
                    if matriz[i][j] != matriz[x][y]:
                        matriz[i][j] = 'X'
    if ficha == 2:
        for i in range(8):
            for j in range(8):
                if abs(i - x) == abs(j - y):
                    if i != x and j != y:
                        matriz[i][j] = 'X'


def printTablero(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j + 1 == len(matriz[1]):
                print(matriz[i][j])
            else:
                print(matriz[i][j], end=" ")


tablero = inicializarTablero()
pieza = elegirFicha()
x, y = elegirPosicion(tablero, pieza)
posiblesPosiciones(tablero, x, y, pieza)
printTablero(tablero)