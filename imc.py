peso_texto = input("Digite seu peso em kg (ex.: 70 ou 70,5): ").replace(",", ".")
altura_texto = input("Digite sua altura em metros (ex.: 1.75 ou 1,75): ").replace(",", ".")

peso = float(peso_texto)
altura = float(altura_texto)

if peso <= 0 or altura <= 0:
    print("Erro: peso e altura precisam ser maiores que zero.")
else:
    imc = peso / (altura * altura)
    print("Seu IMC é:", round(imc, 2))

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 25:
        print("Classificação: Peso normal")
    elif imc < 30:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obesidade")
