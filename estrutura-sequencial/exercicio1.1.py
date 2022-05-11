cod1 = int(input("Digite o código da 1° peça: "))
qtd1 = int(input("Digite a quantidade da 1° peça: "))
val1 = float(input("Digite o valor da 1° peça: "))

cod2 = int(input("Digite o código da 2° peça: "))
qtd2 = int(input("Digite a quantidade da 2° peças: "))
val2 = float(input("Digite o valor da 2° peça: "))

soma1 = qtd1 * val1
soma2 = qtd2 * val2

result = soma1 + soma2

print("VALOR A PAGAR: R$ {:.2f}".format(result))
