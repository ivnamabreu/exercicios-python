def resposta(mensagem, chave):

    nova_mensagem = []

    for c in mensagem:
        if c.isalpha():
            char = c
            posicao = ord(char) - ord("A")
            posicao = (posicao - chave) % 26
            nova_letra = chr(posicao + ord("A"))
            nova_mensagem.append(nova_letra)
        else:
            nova_mensagem.append(c)
    
    return "".join(nova_mensagem)

mensagem = "ZKBKLOXC, UFXK WKCMKBOXRKC O KLBOE! FYMO MYXMVESE Y MEBCY DBSVRK NOF ZIDRYX"
chave = 10
mensagem_decodificada = resposta(mensagem, chave)
print(mensagem_decodificada)




