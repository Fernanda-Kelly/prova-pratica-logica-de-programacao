import math

a = float(input("Digite o valor de 'a': "))
b = float(input("Digite o valor de 'b': "))
c = float(input("Digite o valor de 'c': "))

x1 = 0
x2 = 0

delta = b * b - 4 * a * c

if (a != 0 and delta > 0):
    x1 = round((-b + math.sqrt(delta)) / (2 * a),5)
    x2 = round((-b - math.sqrt(delta)) / (2 * a),5)

    print("X1 = {}".format(x1))
    print("X2 = {}".format(x2))
else:
    print("Impossível calcular")
