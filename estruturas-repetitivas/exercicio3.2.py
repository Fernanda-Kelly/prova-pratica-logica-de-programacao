valN = int(input("Digite um valor N: "))

lista1 = []
lista2 = []
cont = 1

while (cont <= valN):
    valX = int(input("Digite um valor X: "))
    if (valX >= 10 and valX<= 20):
        lista1.append(valX)
    else:
        lista2.append(valX)
    cont += 1
else:
    print(len(lista1), "in")
    print(len(lista2), "out")
