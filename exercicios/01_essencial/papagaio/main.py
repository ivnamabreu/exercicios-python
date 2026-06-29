def resposta(falando, hora):
    if falando and (hora < 7 or hora > 20):
        return True
    else:
        return False