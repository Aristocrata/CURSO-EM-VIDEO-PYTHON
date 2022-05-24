import math

a = float(input('Digite a medida do lado a:'))
b = float(input('Digite a medida do lado b:'))
c = float(input('Digite a medida do lado c:'))

if abs(b - c) < a < (b + c): # CONDIÇÃO DE EXISTÊNCIA
    print('O triângulo existe.')
else:
    print('O triângulo não existe.')
