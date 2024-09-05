# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados (2) do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


import json

with open('dados.json') as f:
    dados = json.load(f)

faturamento_diario = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

dias_com_faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

dias_acima_da_media = sum(1 for dia in dados if dia['valor'] > media_mensal)

print(f'Menor faturamento: {menor_valor}')
print(f'Maior faturamento: {maior_valor}')
print(f'Número de dias com faturamento acima da média: {dias_acima_da_media}')