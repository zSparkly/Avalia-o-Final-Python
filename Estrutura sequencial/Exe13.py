sexo = int(input('Escolha: 1- Sexo Masculino / 2- Sexo Feminino: '))
h = float(input('Altura:'))
peso = float(input('Peso:'))

pesoIdeal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7


print('Peso: %.2f / Peso ideal: %.2f' %(peso, pesoIdeal))