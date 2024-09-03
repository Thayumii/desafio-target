# Desafio Target Sistemas.
Este repositório contém soluções para uma série de problemas técnicos que foram propostos como parte de um processo seletivo da Gupy.

## Desafios

### 1. Cálculo de Soma
No primeiro desafio, foi solicitado que eu analisasse o seguinte trecho de código:
```c
int INDICE = 13, SOMA = 0, K = 0;
while (K < INDICE) {
    K = K + 1;
    SOMA = SOMA + K;
}
print(SOMA);
```
A tarefa era determinar o valor final da variável SOMA após a execução do código.

### 2. Sequência de Fibonacci
No segundo desafio, foi solicitado que eu desenvolvesse um programa que:

- Recebesse um número como entrada.
- Calculasse a sequência de Fibonacci até o número informado.
- Verificasse se o número informado pertence à sequência e retornasse uma mensagem apropriada.

O programa foi escrito na linguagem de minha preferência(python) e considerou a entrada fornecida pelo usuário.

### 3. Análise de Faturamento Diário
Para o terceiro desafio, foi necessário criar um programa que, dado um vetor com o valor de faturamento diário de uma distribuidora, calculasse e retornasse:

- O menor valor de faturamento ocorrido em um dia do mês.
- O maior valor de faturamento ocorrido em um dia do mês.
- O número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

Eu utilizei um arquivo JSON que foi disponibilizado como fonte dos dados do faturamento mensal.

### 4. Percentual de Representação dos Estados
No quarto desafio, foi solicitado que eu escrevesse um programa que, dado o valor de faturamento mensal de uma distribuidora detalhado por estado calcularia o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora:

- SP – R$67.836,43
- RJ – R$36.678,66
- MG – R$29.229,88
- ES – R$27.165,48
- Outros – R$19.849,53

### 5. Inversão de String
Para o quinto desafio, foi solicitado que eu escrevesse um programa que invertesse os caracteres de uma string.

- A string poderia ser informada através de qualquer entrada de minha preferência ou ser previamente definida no código.
- Evitei usar funções prontas como reverse para realizar a inversão.
