nome = str(input("Digite seu nome (minúsculo ou maiusculo): "))

nome = nome.upper()
nome = nome[::-1]

print(f"Nome com letras em maiúsculo: {nome}")