N = int(input())

pontuacao_sheldon = 0
pontuacao_raj = 0

while N > 0:
    escolha_sheldon = input() 
    escolha_raj = input() 
    N = N - 1
    if (escolha_sheldon == 'lagarto' and escolha_raj == 'spock') or (escolha_sheldon == 'spock' and escolha_raj == 'tesoura') or (escolha_sheldon == 'tesoura' and escolha_raj == 'lagarto'):
        pontuacao_sheldon = pontuacao_sheldon + 1
    elif (escolha_raj == 'lagarto' and escolha_sheldon == 'spock') or (escolha_raj == 'spock' and escolha_sheldon == 'tesoura') or (escolha_raj == 'tesoura' and escolha_sheldon == 'lagarto'):
        pontuacao_raj = pontuacao_raj + 1

if pontuacao_sheldon == pontuacao_raj:
    print("Oh não, precisamos de outra rodada.")
elif pontuacao_sheldon > pontuacao_raj:
    print ("BAZINGA! EU SOU O SENHOR DA SALA!")
elif pontuacao_sheldon < pontuacao_raj:
    print ("ENGOLE ESSA, SHELDON!")