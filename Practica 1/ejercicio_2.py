import random

def generar_numero():
    random_number = random.randint(1, 20)
    return random_number


hot_potato = generar_numero()
a = 0

while True:
    a = int(input("Introduce un número:"))
    if a == hot_potato:
        print(f"{a} es el número correcto, ¡ganaste!")
        break
    else:
        print("Número incorrecto, sigue intentandolo")
