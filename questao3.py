#dia e valor

import json

with open('dados.json') as f:
    dados = json.load(f)

# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;

menor_valor = float('inf')
maior_valor = float('-inf')

for d in dados:
    if d['valor'] < menor_valor:
        menor_valor = d['valor']
    if d['valor'] > maior_valor:
        maior_valor = d['valor']

# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#Excluindo dias com valores iguais a 0
valores = [d['valor'] for d in dados if d['valor'] > 0]

#Calculando a média 
media = sum(valores) / len(valores)

#Calculando número de dias
dias_acima_da_media = sum(1 for v in valores if v > media)

print('Menor valor de faturamento: R$ {:.2f}'.format(menor_valor))
print('Maior valor de faturamento: R$ {:.2f}'.format(maior_valor))
print('{} dias com faturamento acima da média mensal de R$ {:.2f}'.format(dias_acima_da_media, media))