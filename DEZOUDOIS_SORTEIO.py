

import random
#lista vazia para cadastrar via loop
jogadores = []
times = ['Time 1', 'Time 2', 'Time 3', 'Time 4', 'Time 5']

while True:
    jogador = str(input('CADASTRE O NOME DO JOGADOR(APERTE FINALIZAR AO FINAL): '))
                          
    if jogador.lower() == 'finalizar':
        break #Encerramento do loop.

    jogadores.append(jogador) #Adicionando cada jogador cadastrado ao final da lista.

#Sorteando os times

random.shuffle(jogadores)

num_jogadores = len(jogadores)
num_times = num_jogadores // 5

if num_times < len(times):
    times = times[:num_times]

times_sorteados = {}

for time in times:
    jogadores_time = random.sample(jogadores, 5)
    times_sorteados[time] = jogadores_time
    for jogador in jogadores_time:
        jogadores.remove(jogador)

jogadores_sobrantes = jogadores

for time, jogadores_time, in times_sorteados.items():
    print(time + ':')
    for jogador in jogadores_time:
        print(jogador)
    print()

print('Jogadores que sobraram: ')
for jogador in jogadores_sobrantes:
    print(jogador)