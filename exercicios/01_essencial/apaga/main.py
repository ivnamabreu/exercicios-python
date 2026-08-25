def resposta(palavra = 'palavra', index = 0):
    if index >= len(palavra):
        return(palavra)
    return(palavra[:index]+ palavra[index + 1:])
