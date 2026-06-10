---
Tags: Métodos de Lista, Listas
Nível: Iniciante
---

## Objetivo

Praticar a ordenação de listas com o método `sort`. Ordenar dados é essencial para gerar relatórios legíveis, encontrar mínimos e máximos e organizar resultados.

## Especificação

### Ordenar uma lista

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe uma lista (`lista`) e deve retorná-la com os elementos em **ordem crescente**. Para listas de texto, a ordem crescente é a ordem alfabética.

Regras:

- Utilize o método `sort` (ou a função `sorted`).
- A lista retornada deve estar em ordem crescente.

Exemplos:

- `resposta([3, 1, 2])` deve retornar `[1, 2, 3]`
- `resposta(['banana', 'abacaxi', 'manga'])` deve retornar `['abacaxi', 'banana', 'manga']`

**Atenção:** utilize `return`, não `print`.
