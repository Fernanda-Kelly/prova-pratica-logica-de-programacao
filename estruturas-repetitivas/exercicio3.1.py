senhaUsu = int(input("Digite a senha: "))

senha = 2002

while (senhaUsu != senha):
    print("Senha Inválida")
    senhaUsu = int(input("Digite a senha: "))
else:
    print("Acesso Permitido")

