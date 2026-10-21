try:
    valor = int(input("Digite um número: "))
    res = 10 / valor
    print(res)
except (ValueError, ZeroDivisionError):
    print("Ocorreu um erro")
