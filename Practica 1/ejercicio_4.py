

def introducePalabra():
    print("¡¡¡ATENCIÓN!!! Jugador A, no mires la pantalla.")
    palabra = input("JUGADOR B:  Introduce una palabra: ")
    fallos = int(input("JUGADOR B:  Introduce el número de fallos: "))
    adivina = "*" * len(palabra)
    return palabra, fallos, adivina


def ahorcado(palabra,fallos,adivina):
    print(f"JUGAODR A: Tienes {fallos} fallos para adivinar la palabra.")
    while fallos > 0:
        letra = input("JUGADOR A: Introduce una letra: ")
        if letra in palabra:
            for i in range(len(palabra)):
                if letra == palabra[i]:
                    adivina = adivina[:i] + letra + adivina[i+1:]
            print(adivina)
            if adivina == palabra:
                print("¡¡¡ENHORABUENA!!! Has acertado la palabra.")
                break
        else:
            fallos -= 1
            print(f"Has fallado, te quedan {fallos} fallos.")
            if fallos == 0:
                print("JUGADOR A: ¡¡¡HAS PERDIDO!!!")
                break


palabra, fallos, advina = introducePalabra()
ahorcado(palabra, fallos, advina)



