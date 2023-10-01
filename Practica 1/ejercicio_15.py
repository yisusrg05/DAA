

def inicializarMatriz():
    matriz = [['-' for _ in range(8)] for _ in range(7)]
    return matriz


def introduceFicha(jugador, matriz):
    while True:
        columna = int(input(f"JUGADOR {jugador}: Introduce la columna en la que quieres introducir la ficha (1-8): "))
        if 0 < columna < 9:
            break
    for i in range(6, 0, -1):
        if matriz[i][columna-1] == '-':
            matriz[i][columna-1] = turno[jugador]
            break


def cuatroEnRaya(jugador, matriz):
    for i in range(7):
        for j in range(8):
            if matriz[i][j] == turno[jugador]:
                # Comprobar horizontalmente hacia la derecha
                if j + 3 < 8 and all(matriz[i][j+k] == turno[jugador] for k in range(4)):
                    return True

                # Comprobar verticalmente hacia arriba
                if i + 3 < 7 and all(matriz[i+k][j] == turno[jugador] for k in range(4)):
                    return True

                # Comprobar diagonal hacia abajo y a la derecha
                if i + 3 < 7 and j + 3 < 8 and all(matriz[i+k][j+k] == turno[jugador] for k in range(4)):
                    return True

                # Comprobar diagonal hacia arriba y a la derecha
                if i - 3 >= 0 and j + 3 < 8 and all(matriz[i-k][j+k] == turno[jugador] for k in range(4)):
                    return True

                # No es necesario realizar ninguna comprobacion mas hacia la izquierda, ya que comprueba todas las
                # casillas una a una, por lo que si una ficha tiene 4 en raya hacia su izquierda, la ficha más a la
                # izquierda de las 4 en raya, ya habrá comprobado que tiene 4 en raya hacia la derecha. Lo mismo es
                # aplicable a las comprobaciones hacia arriba y hacia abajo.

    return False


def printTablero(matriz):
    for i in range(1, 9):
        if i == 8:
            print(f"|{i}|")
        else:
            print(f"|{i}|", end="")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j + 1 == len(matriz[1]):
                print(f"|{matriz[i][j]}|")
            else:
                print(f"|{matriz[i][j]}|", end="")


def juego(matriz):
    jugador = 'A'
    while True:
        introduceFicha(jugador, matriz)
        if cuatroEnRaya(jugador, matriz):
            print(f"CUATRO EN RAYA DEL JUGADOR {jugador}")
            printTablero(matriz)
            print(f"JUGADOR {jugador} GANA")
            break
        if jugador == 'A':
            jugador = 'B'
        else:
            jugador = 'A'
        printTablero(matriz)


turno = {
    'A': 'X',
    'B': '#'
}

matriz = inicializarMatriz()
juego(matriz)
