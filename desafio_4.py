# Dicionário com o valor de faturamento por estado.
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

def calcular_percentual(faturamento_por_estado):
    total_faturamento = sum(faturamento_por_estado.values()) # Calcula o valor total de faturamento.

# Calcula o percentual de cada estado.
    percentual_por_estado = {}
    for estado, faturamento in faturamento_por_estado.items():
        percentual = (faturamento / total_faturamento) * 100
        percentual_por_estado[estado] = percentual

    return percentual_por_estado

# Executar a função e calcular os percentuais.
percentuais = calcular_percentual(faturamento_por_estado)

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")