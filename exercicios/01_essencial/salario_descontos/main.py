def resposta(valor, horas):
    sal_brut = valor * horas
    ir = 0.11 * sal_brut
    inss = 0.08 * sal_brut
    sind = 0.05 * sal_brut
    descontos = ir + inss + sind
    sal_liq = sal_brut - descontos
    return(sal_brut, ir, inss, sind, sal_liq)
    







