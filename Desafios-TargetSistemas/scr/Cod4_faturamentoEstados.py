faturamentos = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamentos.values())

percentuais = {}
for estados, valor in faturamentos.items():
    percentual = (valor / total_faturamento) * 100
    percentuais[estados] = percentual

print("Percentual de representação por estado:")
for estados, percentual in percentuais.items():
    print(f"{estados}: {percentual:.2f}%")
