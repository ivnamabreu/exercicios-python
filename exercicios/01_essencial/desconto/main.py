def resposta(preço, percentual):
    desconto = preço * (percentual / 100)
    preço_final = preço - desconto
    return(desconto, preço_final)