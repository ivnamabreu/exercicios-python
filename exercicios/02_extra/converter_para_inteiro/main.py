def resposta(texto):
    try:
        inteiro = int(texto)
        return(inteiro)
    
    except ValueError:
        return("Valor inválido")
