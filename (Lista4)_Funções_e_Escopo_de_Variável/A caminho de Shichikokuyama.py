def separador__silabas(string):
    vogais = set('aeiou')
    inicio = 0
    resposta = []
    for index in range(len(string)):
        if string[index] in vogais:
            resposta.append(string[inicio:index + 1])
            inicio = index + 1
    return resposta


def comparador(a, b):
    return a == b


def ordem(_silabas):
    ordem = False
    ultimo_index = 0
    atual_index = 0
    cont = 0
    while cont < len(_silabas):
        if cont == 0:
            ultimo_index = nome_hospital.index(_silabas[cont])
        else:
            atual_index = nome_hospital.index(_silabas[cont])

            ordem = comparador(ultimo_index, atual_index - 1)

            ultimo_index = atual_index
        cont += 1
    return ordem


nome_hospital = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']

silaba_encontrada = []
condicao_parada = True
while condicao_parada:
    _string = input()
    silabas = separador__silabas(_string)
    pertence_hospital = []
    for silaba in silabas:
        if silaba in nome_hospital:
            index_nome = nome_hospital.index(silaba)
            if index_nome not in silaba_encontrada:
                silaba_encontrada.append(index_nome)
                pertence_hospital.append(silaba)

    if len(pertence_hospital) == 1:
        print(f'Lembrei! A sílaba {pertence_hospital[0]} está no nome do hospital. Obrigada, Totoro!')
    elif len(pertence_hospital) > 1:
        na_ordem = ordem(pertence_hospital)
        s = ''
        if na_ordem and s.join(pertence_hospital) == _string:
            print(f'A palavra {s.join(pertence_hospital)} está toda no nome do hospital. Acertou em cheio, Totoro!')
        else:
            separador = ', '
            print(
                f'Lembrei! As sílabas: {separador.join(pertence_hospital)} estão no nome do hospital. Obrigada, Totoro!')
    else:
        print('Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')

    silaba_encontrada.sort()
    if silaba_encontrada == [0, 1, 2, 3, 4, 5]:
        condicao_parada = False
        print('Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')



       



    




    
