cod1 = int(input("Digite o c�digo da 1� pe�a: "))
qtd1 = int(input("Digite a quantidade da 1� pe�a: "))
val1 = float(input("Digite o valor da 1� pe�a: "))

cod2 = int(input("Digite o c�digo da 2� pe�a: "))
qtd2 = int(input("Digite a quantidade da 2� pe�as: "))
val2 = float(input("Digite o valor da 2� pe�a: "))

soma1 = qtd1 * val1
soma2 = qtd2 * val2

result = soma1 + soma2

print("VALOR A PAGAR: R$ {:.2f}".format(result))
