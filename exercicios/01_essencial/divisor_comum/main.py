def resposta(numero1, numero2):
    while numero2 != 0:
        numero1, numero2 = numero2, numero1 % numero2
    return (numero1)

