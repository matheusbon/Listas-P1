nome_fogos = input()
decibeis_fogos = int(input())
decibeis_caruaru = int(input())
decibeis_campina = int(input())
if decibeis_caruaru >= decibeis_fogos <= decibeis_campina:
  print  (f'Boa Felipe, o {nome_fogos} será um sucesso em Campina Grande e Caruaru!')
elif decibeis_caruaru >= decibeis_fogos > decibeis_campina:
    print (f'Infelizmente em Campina Grande não vai rolar, mas em Caruaru o {nome_fogos} vai ser extouro!')
elif decibeis_caruaru < decibeis_fogos <= decibeis_campina:
    print (f'Infelizmente em Caruaru não vai rolar, mas em Campina Grande o {nome_fogos} vai ser extouro!')
elif decibeis_caruaru < decibeis_fogos > decibeis_campina:
    print (f'Poxa Felipe, não vai ser dessa vez que {nome_fogos} fará um sucesso pelas festas juninas do Brasil')

        