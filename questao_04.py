# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_por_estado.values())

percentual_por_estado = {}
for estado, faturamento in faturamento_por_estado.items():
    percentual = (faturamento / faturamento_total) * 100
    percentual_por_estado[estado] = percentual

print('Percentual de representação de cada estado no faturamento total mensal da distribuidora: ')
for estado, percentual in percentual_por_estado.items():
    print(f'{estado}: {percentual:.2f}%')