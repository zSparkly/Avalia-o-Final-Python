salario = float(input("Digite o seu salário: "))

acrescimo1 = salario * 0.20
total1 = salario * 1.20
acrescimo2 = salario * 0.15
total2 = salario * 1.15
acrescimo3 = salario * 0.10
total3 = salario * 1.10
acrescimo4 = salario * 0.05
total4 = salario * 1.05

print("Antes Reajuste:", salario)

if salario <= 280:
    print("Aumento: 20%")
    print("Valor: ", acrescimo1)
    print("Final: ", total1)
elif salario > 280 and salario <= 700:
    print("Aumento: 15%")
    print("Valor: ", acrescimo2)
    print("Final: ", total2)
elif salario > 700 and salario <= 1500:
    print("Aumento: 10%")
    print("Valor: ", acrescimo3)
    print("Final: ", total3)
else:
    print("Aumento: 5%")
    print("Valor: ", acrescimo4)
    print("Final: ", total4)