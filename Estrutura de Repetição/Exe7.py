numeros = []
for num in range(1, 6):
    numeros.append(int(input("Digite um Número: ")))

maiorNumero = numeros[0]

cont = 1
while cont < 5:
    if numeros[cont] > maiorNumero:
        maiorNumero = numeros[cont]
    cont = cont + 1

print(f"O maior numero é: {maiorNumero}")