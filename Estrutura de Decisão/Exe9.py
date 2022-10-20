num = []
qtd = 3
for i in range(qtd):
    elemento = int(input('Digite um numero: '))
    num.append(elemento)

num.sort(reverse = True)
print(num)
