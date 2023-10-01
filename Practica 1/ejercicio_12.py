

def contar_letras(frase):
    # Inicializar un diccionario para almacenar el recuento de letras
    contador_letras = {}

    # Recorrer cada caracter en la frase
    for caracter in frase:
        # Ignorar espacios en blanco
        if caracter != ' ':
            # Convertir el caracter a minúsculas para no distinguir entre mayúsculas y minúsculas
            caracter = caracter.lower()
            # Actualizar el contador para el caracter actual
            if caracter in contador_letras:
                contador_letras[caracter] += 1
            else:
                contador_letras[caracter] = 1

    return contador_letras


# Solicitar al usuario una frase
frase = input("Ingrese una frase: ")

# Obtener el diccionario de recuento de letras
recuento = contar_letras(frase)

# Imprimir el recuento de letras
for letra, cantidad in recuento.items():
    if cantidad == 1:
        print(f"'{letra}': {cantidad} vez")
    else:
        print(f"'{letra}': {cantidad} veces")
