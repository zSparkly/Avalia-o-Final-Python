lista1 = ['Janeiro','Fevereiro','Março','Abril',
          'Maio','Junho','Julho','Agosto',
          'Setembro','Outubro','Novembro','Dezembro']


dia = int(input('Digite o dia do nascimento: '))
mes = int(input('Digite o mês do nascimento: '))
ano = int(input('Digite o ano do nascimento: '))

if mes == 1:
    mes = (lista1[0])
elif mes == 2:
    mes = (lista1[1])
elif mes == 3:
    mes = (lista1[2])
elif mes == 4:
    mes = (lista1[3])
elif mes == 5:
    mes = (lista1[4])
elif mes == 6:
    mes = (lista1[5])
elif mes == 7:
    mes = (lista1[6])
elif mes == 8:
    mes = (lista1[7])
elif mes == 9:
    mes = (lista1[8])
elif mes == 10:
    mes = (lista1[9])
elif mes == 11:
    mes = (lista1[10])
elif mes == 12:
    mes = (lista1[11])

print(f'Você nasceu em {dia} de {mes} de {ano}.')