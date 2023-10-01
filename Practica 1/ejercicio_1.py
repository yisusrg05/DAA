

def introduce_cantidad():
    cantidad = int(input("Introduce cantidad en €:"))
    return cantidad


def desglose(cantidad):
    while cantidad != 0:
        if cantidad % 500 == 0:
            billetes["500"] += 1
            cantidad -= 500
            continue
        elif cantidad % 200 == 0:
            billetes["200"] += 1
            cantidad -= 200
            continue
        elif cantidad % 100 == 0:
            billetes["100"] += 1
            cantidad -= 100
            continue
        elif cantidad % 50 == 0:
            billetes["50"] += 1
            cantidad -= 50
            continue
        elif cantidad % 20 == 0:
            billetes["20"] += 1
            cantidad -= 20
            continue
        elif cantidad % 10 == 0:
            billetes["10"] += 1
            cantidad -= 10
            continue
        elif cantidad % 5 == 0:
            billetes["5"] += 1
            cantidad -= 5
            continue
        elif cantidad % 2 == 0:
            billetes["2"] += 1
            cantidad -= 2
            continue
        elif cantidad % 1 == 0:
            billetes["1"] += 1
            cantidad -= 1
            continue


def mostrar():
    for b in billetes.keys():
        if billetes[b] == 1:
            if b == 2 or b == 1:
                print(f"1 moneda de {b} euros.")
            else:
                print(f"1 billete de {b} euros.")
        elif billetes[b] >= 1:
            if b == 2 or b == 1:
                print(f"1 moneda de {b} euros.")
            else:
                print(f"{billetes[b]} monedas de {b} euros.")


billetes = {
    "500": 0,
    "200": 0,
    "100": 0,
    "50": 0,
    "20": 0,
    "10": 0,
    "5": 0,
    "2": 0,
    "1": 0
}

cantidad = introduce_cantidad()
desglose(cantidad)
mostrar()