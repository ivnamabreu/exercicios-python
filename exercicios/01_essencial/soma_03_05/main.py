def resposta(n = 54):
    soma = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            soma += i
    return(soma)



#soma de todos os números menores que `n` que sejam múltiplos de 3 ou 5.
#Regras:
#Considere apenas números menores que `n`
#Inclua múltiplos de 3, de 5 ou de ambos

