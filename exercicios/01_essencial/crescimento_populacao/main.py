def resposta():
    pop_A = 80000
    pop_B = 200000
    anos = 0

    while pop_A < pop_B:
        pop_A += pop_A * 0.03
        pop_B += pop_B * 0.015
        anos += 1
    return(anos)

