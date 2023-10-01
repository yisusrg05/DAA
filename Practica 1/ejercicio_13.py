

# Definir diccionario de numeros
numeros = {
    'uno': '1',
    'dos': '2',
    'tres': '3',
    'cuatro': '4',
    'cinco': '5',
    'seis': '6',
    'siete': '7',
    'ocho': '8',
    'nueve': '9',
    'diez': '10',
    'once': '11',
    'doce': '12',
    'trece': '13',
    'catorce': '14',
    'quince': '15',
    'dieciseis': '16',
    'diecisiete': '17',
    'dieciocho': '18',
    'diecinueve': '19',
    'veinte': '20',
    'veintiuno': '21',
    'veintidos': '22',
    'veintitres': '23',
    'veinticuatro': '24',
    'veinticinco': '25',
    'veintiseis': '26',
    'veintisiete': '27',
    'veintiocho': '28',
    'veintinueve': '29',
    'treinta': '30',
    'treinta y uno': '31',
    'treinta y dos': '32',
    'treinta y tres': '33',
    'treinta y cuatro': '34',
    'treinta y cinco': '35',
    'treinta y seis': '36',
    'treinta y siete': '37',
    'treinta y ocho': '38',
    'treinta y nueve': '39',
    'cuarenta': '40',
    'cuarenta y uno': '41',
    'cuarenta y dos': '42',
    'cuarenta y tres': '43',
    'cuarenta y cuatro': '44',
    'cuarenta y cinco': '45',
    'cuarenta y seis': '46',
    'cuarenta y siete': '47',
    'cuarenta y ocho': '48',
    'cuarenta y nueve': '49',
    'cincuenta': '50'
}


def cambiar_numeros(frase):
    # Recorrer cada caracter en la frase
    palabra = ''
    frase_numeros = ''
    encontrado = False
    for caracter in frase:
        # Sino es espacio en blanco, concatenar el caracter a la palabra
        if caracter != ' ':
            palabra += caracter
        elif caracter == ' ':
            for numero in numeros.keys():
                if palabra == numero:
                    frase_numeros += numeros[numero] + ' '
                    encontrado = True
            if not encontrado:
                frase_numeros += palabra + ' '
            palabra = ''
            encontrado = False

    return frase_numeros


# Solicitar al usuario una frase
print("Los números deben estar en minúsculas y sin acentos.")
frase = input("Ingrese una frase: ")
frase += ' '

# Obtener el diccionario de recuento de palabras
frase_digitos = cambiar_numeros(frase)

print(frase_digitos)
