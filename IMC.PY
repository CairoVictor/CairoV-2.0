import os

print("VAMOS CALCULAR SEU IMC")

peso = float(input("Qual o seu peso?: "))
altura = float(input("Qual a sua altura?: "))

imc = round(peso/altura**2)
classificacao = ""

os.system('cls')

print("<--------RESULTADO-------->")

if imc < 18.5:
    classificacao = "Magreza"
elif 18.5 <= imc < 25:
    classificacao = "Normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 40:
    classificacao = "Obesidade"
else :
    classificacao = "Obesidade Grave"
print("IMC: ", imc)
print("Sua classificação é:", classificacao)
print("<------------------------->")