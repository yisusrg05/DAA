

def contar_palabras(frase):
    # Inicializar un diccionario para almacenar el recuento de palabras
    contador_palabras = {}
    palabra = ''
    # Recorrer cada caracter en la frase
    for caracter in frase:
        # Sino es espacio en blanco, concatenar el caracter a la palabra
        if caracter != ' ':
            caracter = caracter.lower()
            palabra += caracter
        elif caracter == ' ':
            if palabra in contador_palabras:
                contador_palabras[palabra] += 1
            else:
                contador_palabras[palabra] = 1
            palabra = ''

    return contador_palabras


# Solicitar al usuario una frase
frase = input("Ingrese una frase: ")
frase += ' '

# Obtener el diccionario de recuento de palabras
recuento = contar_palabras(frase)

# Imprimir el recuento de palabras
for palabra, cantidad in recuento.items():
    if cantidad == 1:
        print(f"'{palabra}': {cantidad} vez")
    else:
        print(f"'{palabra}': {cantidad} veces")