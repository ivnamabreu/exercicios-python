def resposta(texto):
    texto_novo = texto.lower().split()
    dicionario = {}
    for palavra in texto_novo:
        dicionario[palavra] = dicionario.get(palavra, 0) + 1
    return(dicionario)

#outra forma:
def resposta(texto):
    texto_novo = texto.lower().split()
    dicionario = {}
    for palavra in texto_novo:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return(dicionario)

#outra forma:
def resposta(texto):
    texto_novo = texto.lower().split()
    dicionario = {}
    for palavra in texto_novo:
        if palavra not in dicionario:
            dicionario[palavra] = texto_novo.count(palavra)
    return (dicionario)

#Qual é a diferença entre as abordagens?
#Usando count(): mais simples de entender, mas menos eficiente. Para cada palavra, o Python percorre a lista inteira para contar as ocorrências. Se o texto tiver muitas palavras, isso pode ficar lento.
#Usando o dicionário com if ou .get(): percorre a lista apenas uma vez, atualizando as contagens conforme encontra cada palavra. É a solução mais eficiente e a que normalmente se espera em exercícios desse tipo.