nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
print('Media: ',media)

if media < 7:
    print("Reprovado")
elif media < 10:
    print("Aprovado")
else:
    print("Aprovado com Distinção")