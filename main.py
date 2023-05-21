def imprimir_quadrados_perfeitos(numero):
    i = 1
    while i * i <= numero:
        print(i * i)
        i += 1
3

numero = int(input("Digite um número: "))
imprimir_quadrados_perfeitos(numero)
