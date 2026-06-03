def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b


def calcular():
    print("\n=== CALCULADORA PYTHON ===")

    try:
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        op = input("Operação (+ - * /): ")

        if op == '+':
            resultado = somar(num1, num2)
        elif op == '-':
            resultado = subtrair(num1, num2)
        elif op == '*':
            resultado = multiplicar(num1, num2)
        elif op == '/':
            resultado = dividir(num1, num2)

            if resultado is None:
                print("Erro: divisão por zero")
                return
        else:
            print("Operação inválida")
            return

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Erro: digite apenas números")


while True:
    calcular()

    continuar = input("\nDeseja continuar? (s/n): ").lower()
    if continuar != "s":
        print("Encerrando calculadora...")
        break
