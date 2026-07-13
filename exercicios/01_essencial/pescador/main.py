def resposta(peso):
    if peso >= 50:
        excesso = peso - 50
        multa = 4 * excesso
    else:
        excesso = 0
        multa = 0
    return(excesso, multa)
