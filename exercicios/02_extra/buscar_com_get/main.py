def resposta(dicionario, chave):
    if chave in dicionario:
        return dicionario.get(chave)
    else:
        return None
