

def trianguloFloyd(n):
    k = 0
    lista = [x for x in range(1, n + 1)]
    aux = ''
    for i in range(n):
        for j in lista[k:k+1+i]:
            if i > 3:
                aux += str(j) + ' '
            else:
                aux += str(j) + '  '
        k += i+1
        print(aux)
        aux = ''


number = int(input("Introduce un número:"))
trianguloFloyd(number)

