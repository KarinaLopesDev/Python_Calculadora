print("\n******************* Calculadora em Python *******************")

print("\nSelecione o numero da operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicacao")
print("4- Divisao")

#Funcao soma
def soma(number1, number2):
    return number1 + number2

#Funcao subtrair
def subtrair(numero1, numero2):
    return numero1-numero2

#Funcao dividir
def dividir(numero1, numero2):
    return numero1/numero2

#Funcao Multiplicar
def multiplica(numero1, numero2):
    return numero1*numero2

escolha = input("\n Digite sua operacao (1/2/3/4)?")

if escolha == "1" or escolha == "2" or escolha == "3" or escolha == "4":
    numero1 = float(input("Digite o numero 01:"))
    numero2 = float(input("Digite o numero 02:"))
    if escolha == "1":
        resultado = soma(numero1, numero2)
        print("A soma dos valores é: ", resultado)
    elif escolha == "2":
        resultado = subtrair(numero1, numero2)
        print("A subtracao dos valores é: ", resultado)
    elif escolha == "3":
        resultado = multiplica(numero1, numero2)
        print("A multiplicacao dos valores é: ", resultado)
    else:
        resultado = dividir(numero1, numero2)
        print("A divisao dos valores é: ", resultado)
else:
    print("Valor escolhido invalido!")





