frase = input("Digite a frase: ")
vogais = 0
espacos = 0
letras = 0
for letra in frase:
    if letra == " ":
        espacos += 1
    elif letra in "aeiou":
        vogais += 1
    else:
        letras += 1
        letras = vogais + letras

print(f"A frase tem: {letras} letras, {vogais} vogais e {espacos} espaços ")