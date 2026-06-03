# Calculadora Spark 2030 - Bruno Miguel

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


print("=== CALCULADORA SPARK 2030 ===")

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
op = input("Operação (+ - * /): ")

if op == '+':
    print(f"Resultado: {somar(num1, num2)}")
elif op == '-':
    print(f"Resultado: {subtrair(num1, num2)}")
elif op == '*':
    print(f"Resultado: {multiplicar(num1, num2)}")
elif op == '/':
    print(f"Resultado: {dividir(num1, num2)}")
else:
    print("Operação inválida")
