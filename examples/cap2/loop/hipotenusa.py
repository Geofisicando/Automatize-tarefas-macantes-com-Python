from math import sqrt as raiz_quadrada

a = float(input("Cateto a: "))
b = float(input("Cateto b: "))

c = raiz_quadrada(a*a+b*b)

print("Hipotenusa="+str(c))
