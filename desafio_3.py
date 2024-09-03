import json

def calcular_faturamento(dados_arquivo):
    with open(dados_arquivo, 'r') as arquivo:
        dia= json.load(arquivo)

# Filtrar os valores maior que zero.
    faturamentos = [item['valor'] for item in dia if item['valor'] > 0]

# Verificar se há faturamentos válidos.
    if not faturamentos:
        return None, None, 0

# Calcular menor, maior e média de faturamentos.
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_mensal = sum(faturamentos) / len(faturamentos)

    dias_acima_media = sum(1 for valor in faturamentos if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_media

# Executar a função com o arquivo JSON e armazenar resultados.
menor, maior, dias_acima_media = calcular_faturamento('dados.json')

# Exibir resultados.
print(f"Menor valor: R${menor:.2f}")
print(f"Maior valor: R${maior:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")