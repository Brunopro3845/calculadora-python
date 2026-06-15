import math

historico = []


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero")
    return a / b


def potencia(a, b):
    return a ** b


def raiz(a):
    if a < 0:
        raise ValueError("Não existe raiz quadrada real de número negativo")
    return math.sqrt(a)


while True:
    print("\n" + "=" * 35)
    print("      CALCULADORA PYTHON")
    print("=" * 35)
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("7 - Histórico")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    try:
        if opcao == "0":
            print("Encerrando...")
            break

        elif opcao == "7":
            print("\n=== HISTÓRICO ===")

            if not historico:
                print("Nenhum cálculo realizado.")
            else:
                for item in historico:
                    print(item)

        elif opcao == "6":
            numero = float(input("Digite um número: "))

            resultado = raiz(numero)

            operacao = f"√{numero} = {resultado}"
            historico.append(operacao)

            print(f"Resultado: {resultado}")

        elif opcao in ["1", "2", "3", "4", "5"]:

            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))

            if opcao == "1":
                resultado = somar(num1, num2)
                operacao = f"{num1} + {num2} = {resultado}"

            elif opcao == "2":
                resultado = subtrair(num1, num2)
                operacao = f"{num1} - {num2} = {resultado}"

            elif opcao == "3":
                resultado = multiplicar(num1, num2)
                operacao = f"{num1} * {num2} = {resultado}"

            elif opcao == "4":
                resultado = dividir(num1, num2)
                operacao = f"{num1} / {num2} = {resultado}"

            elif opcao == "5":
                resultado = potencia(num1, num2)
                operacao = f"{num1}^{num2} = {resultado}"

            historico.append(operacao)

            print(f"Resultado: {resultado}")

        else:
            print("Opção inválida.")

    except ValueError as erro:
        print(f"Erro: {erro}")
