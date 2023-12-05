print("VAMOS CALCULAR SEU IMC")

peso = float(input("Qual o seu peso?: "))
altura = float(input("Qual a sua altura?: "))

imc = round(peso/altura**2,2)

print("RESULTADO->")

if imc < 18.5:
    print("IMC: ", imc)
    print("Classificação: Magreza")

elif 18.5 < imc < 24.9:
    print("IMC: ", imc)
    print("Classificação: Normal")

elif 25 < imc < 29.9:
    print("IMC: ", imc)
    print("Classificação: Sobrepeso")

elif 30 < imc < 39.9:
    print("IMC: ", imc)
    print("Classificação: Obesidade")

else : 
    print("IMC: ", imc)
    print("Classificação: Obesidade Grave")