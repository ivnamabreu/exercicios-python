def resposta(cigarros, anos):
    total_cigarros = cigarros * 365 * anos
    total_minutos = total_cigarros * 10
    dias_perdidos = total_minutos // 1440
    return dias_perdidos
