#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
#de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

brasileirao = ('Palmeiras', 'Bragantino', 'Atlético-MG', 'Fortaleza',
                'Athletico-PR', 'Bahia', 'Fluminense', 'Flamengo',
                'Santos', 'Atlético-GO', 'Ceará', 'Corinthians',
                'Juventude', 'São Paulo', 'Internacional', 'América-MG',
                'Sport', 'Cuiabá', 'Chapecoense', 'Grêmio')

print(f'Lista de times do Brasileirão: {brasileirao}')
print('-='*20)
print(f'Os 5 primeiros times são: {brasileirao[0:5]}')
print('-='*20)
#Fatiamento na ordem reversa:
print(f'Os quatro últimos são {brasileirao[-4:]}')

#Lista criada para ordenar os times, pois as tuplas são imutáveis:
listaOrdenada = list()

for b in range(0, 20):
    #Primeiro coloca os elementos da tupla em listaOrdenada
    listaOrdenada.append(brasileirao[b])
    #Verifica em que posição está o Chapecoense:
    if brasileirao[b] == 'Chapecoense':
        chapecoense = b

#Ordena alfabeticamente os times:
listaOrdenada.sort()

print('-='*20)
print(f'Times em ordem alfabética: {listaOrdenada}')
#poderia usar o método sorted, que retorna uma lista ordenada:
#sorted(times)
print('-='*20)
print(f'O Chapecoense está na {chapecoense+1}ª posição')
#Poderia usar também times.index('Chapecoense')+1
