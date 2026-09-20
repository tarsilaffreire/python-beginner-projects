print("-- Calculadora: Converter real para dólar --")
print( )

real = float(input("Digite o valor em reais: "))
cotaçao = float(input("Digite a cotação do dólar hoje: "))

dolar = real / cotaçao
print(f"Valor em dólar: US$ {dolar:.2f}")