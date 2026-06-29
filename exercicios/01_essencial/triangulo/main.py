def resposta(lado1, lado2, lado3):
    if (lado1 + lado2  > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1) and (lado1 == lado2 == lado3):
        return 'equilátero'
    elif (lado1 + lado2  > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1) and (lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado3 == lado2 != lado1):
        return 'isósceles'
    elif (lado1 + lado2  > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1) and (lado1 != lado2 != lado3):
        return 'escaleno'
    else:
        return 'não forma triângulo'
