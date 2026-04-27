---
Tags: Variáveis, Conversão de Tipos, Operações Aritméticas, Funções
Nível: Iniciante
---

## Objetivo

Praticar conversão de tipos e cálculos simples com números. Neste exercício, você irá transformar um valor recebido como texto em número e utilizá-lo para calcular a idade.

## Especificação

### Cálculo de Idade

Abra o arquivo main.py. Dentro dele, localize a função resposta.

A função deverá receber um valor (string) representando o ano de nascimento e retornar a idade calculada considerando o ano atual como 2026.

Caso o exercício original peça entrada de dados com `input()`, considere que esse valor será passado como parâmetro para a função resposta.

Regras:

- Converter o valor recebido para inteiro
- Calcular a idade:
  - idade = 2026 - ano de nascimento
- Retornar o valor da idade

Exemplos:

- `resposta("2000")` → `26`  
- `resposta("1990")` → `36`  

**Atenção:** utilize return, não print