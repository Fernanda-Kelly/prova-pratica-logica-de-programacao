cod = int(input("Digite o código do item: "))
qtd = int(input("Digite a quantidade do item: "))

result = 0.00

if (cod == 1):
    result = qtd * 4.00
    print("Total: R$ {:.2f}".format(result))
elif (cod == 2):
    result = qtd * 4.50
    print("Total: R$ {:.2f}".format(result))
elif (cod == 3):
    result = qtd * 5.00
    print("Total: R$ {:.2f}".format(result))
elif (cod == 4):
    result = qtd * 2.00
    print("Total: R$ {:.2f}".format(result))
elif (cod == 5):
    result = qtd * 1.50
    print("Total: R$ {:.2f}".format(result))
else:
    print("O produto não existe!")
