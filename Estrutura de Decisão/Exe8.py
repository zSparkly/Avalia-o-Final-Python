P1 = float(input("Preço primeiro produto: "))
P2 = float(input("Preço segundo produto: "))
P3 = float(input("Preço terceiro produto: "))

print('\n' * 2)

if P1 < P2 and P3:
    print("O primeiro Produto é o mais barato: ", P1)
elif P2 < P1 and P3:
    print("O segundo Produto é o mais barato: ", P2)
elif P3 < P1 and P2:
    print("O terceiro Produto é o mais barato: ", P3)