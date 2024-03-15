# Maneira Simples
a = float(input("Digite o valor a: "))
b = float(input("Digite o valor b: "))
c = float(input("Digite o valor c: "))

delta = (b**2 - 4*a*c)
x1 = (-b + delta**(1/2)) / (2*a)
x2 = (-b - delta**(1/2)) / (2*a)

print("Valor de x1: {}".format(x1))
print("Valor de x2: {}".format(x2))