import math

numero = int(input("Digite um número: "))

print("Quadrados perfeitos menores ou iguais a", numero, ":")
for i in range(1,numero+1):
    print(i **2)
