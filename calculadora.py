print("-- Calculadora --")
print( )

n1 = float(input("Digite o primeiro número: "))
operaçao = input("Digite a operação (+, -, *, /): ")
n2 = float(input("Digite o segundo número: "))

if operaçao == "+":
    resultado = n1 + n2
    print("O resultado da soma é:", resultado)

elif operaçao == "-":
    resultado = n1 - n2
    print("O resultado da subtração é:", resultado)

elif operaçao == "*":
    resultado = n1 * n2
    print("O resultado da multiplicação é:", resultado)

elif operaçao == "/":
    if n2 != 0:
        resultado = n1 / n2
        print("O resultado da divisão é:", resultado)
    else:
        print("Não é possível dividir por zero.")

else:
    print("Não é possível realizar essa operacão.")