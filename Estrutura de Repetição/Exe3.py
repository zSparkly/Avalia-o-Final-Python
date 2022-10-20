nome = input("Digite o nome: ")
while (len(nome) <= 3):
    print("ERRO: O nome deve conter + de 3 caracteres")
    nome = input("informe um nome:")

idade = int(input("Digite a idade: "))
while (idade > 150 or idade < 0):
    print("ERRO: idade inválida")
    idade = int(input("Digite a idade: "))

sal = float(input("Digite um salário: "))
while (sal < 0):
    print("ERRO: o salário precisa ser > 0")
    sal = float(input("Digite um salário: "))

sexo = str(input("Digite a inicial do seu sexo: "))
while sexo != "f" and sexo != "F" and sexo != "m" and sexo != "M":
    sexo = str(input("Digite a inicial do seu sexo: "))

ec = str(input("informe a inicial do seu estado civil: "))
while (ec != "s" and ec != "S"
       and ec != "c" and ec != "C"
       and ec != "v" and ec != "V"
       and ec != "d" and ec != "D"):

    print("Erro: estado civil inválido\nAs opções são: Casado/a,Solteiro/a,Viúvo/a ou Divorciado/a")
    ec = str(input("informe a inicial do seu estado civil: "))