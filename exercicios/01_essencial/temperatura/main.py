def resposta(temperatura, tipo_conversao):
    if tipo_conversao == "C":
        return (9 * temperatura / 5) + 32
    
    if tipo_conversao == "F":
        return (temperatura - 32) * 5 / 9

