def resposta(n):
    sequencia = []
    if n <= 0:
        pass
    else:
        sequencia += [1, 1]
        for i in range(2,n):
            sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia[-1]
