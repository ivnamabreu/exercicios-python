---
Tags: Laços de Repetição (while), Listas, Estruturas Condicionais (if)
Nível: Intermediário
---

## Objetivo

Praticar o `while` com uma **condição de parada por sentinela**: o laço continua repetindo até encontrar um valor especial que sinaliza o fim. Esse padrão é a base de menus e leituras que se repetem "até o usuário decidir parar".

## Especificação

### Soma até o valor de parada

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe uma lista de números inteiros chamada `numeros`. Percorra a lista com um laço `while`, somando os valores, e **pare assim que encontrar o número `0`**. O `0` funciona como sinal de parada e **não** deve ser incluído na soma. A função retorna a soma obtida.

> Em um programa interativo, você leria cada número com `input()` dentro do laço, repetindo até o usuário digitar `0`. Aqui, a função `resposta` já recebe todos esses valores prontos na lista `numeros`.

Regras:

- Utilize obrigatoriamente o laço `while`.
- Pare ao encontrar o **primeiro** `0` e não some esse `0`.
- Se a lista não contiver nenhum `0`, some todos os elementos.

Exemplos:

- `resposta([4, 7, 2, 0, 9])` deve retornar `13` (soma 4 + 7 + 2 e para no 0)
- `resposta([1, 2, 3])` deve retornar `6` (não há 0, soma tudo)
- `resposta([0, 5])` deve retornar `0` (para logo no início)

**Atenção:** utilize `return`, não `print`.
