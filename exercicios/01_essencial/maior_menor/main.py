def resposta(n1, n2, n3):
    maior_valor = None
    menor_valor = None

    if n1 >= n2 and n1 >= n3:
        maior_valor = n1
    elif n2 >= n1 and n2 >= n3:
        maior_valor = n2
    else:
        maior_valor = n3

    if n1 <= n2 and n1 <= n3:
        menor_valor = n1
    elif n2 <= n1 and n2 <= n3:
        menor_valor = n2
    else:
        menor_valor = n3

    return(maior_valor, menor_valor)