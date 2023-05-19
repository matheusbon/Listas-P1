quantidade_mochilas = int (input())
amigos = input().split(' ')
lista_mochilas = [0] * quantidade_mochilas
encerrou = False 

for i in range (quantidade_mochilas):
    tamanho_mochila = int (input())
    lista_mochilas[i] = [0] * tamanho_mochila
    lista_mochilas[i][0] = "Lanterna"
    lista_mochilas[i][1] = "Omega 3 da top therm"

quantidade_itens = int (input())
if quantidade_itens > 0:    
    for i in range (quantidade_itens):
        nome_item = input()
        mochila_escolhida = int (input())
        if 0 in lista_mochilas[mochila_escolhida]:
            index_0 = lista_mochilas[mochila_escolhida].index(0)
            lista_mochilas[mochila_escolhida][index_0] = nome_item
        else:
            print ("Mochila cheia. Não vai dar para levar.")

while encerrou == False:
    acao = input()
    if acao == "CHEGAMOS NO CIN!":
        encerrou = True
        break
    if acao != "Tirar da mochila" and acao != "Guardar na mochila" and acao != "CHEGAMOS NO CIN!":
        acao = input()
        print ("Ação inválida.")
        if acao == "CHEGAMOS NO CIN!":
            encerrou = True
            break
    item_acao = input()
    mochila_item_acao = int (input())
    
    
    if acao == "Tirar da mochila":
        if (item_acao) in lista_mochilas[mochila_item_acao]:
            index_item_acao = lista_mochilas[mochila_item_acao].index(item_acao)
            lista_mochilas[mochila_item_acao][index_item_acao] = 0
            print (f"{item_acao} usado com sucesso da mochila {mochila_item_acao}.")
        else:
            print (f"Você não tem {item_acao} na mochila {mochila_item_acao}.")
    
    elif acao == "Guardar na mochila":
        if 0 in lista_mochilas[mochila_item_acao]:
            index_0 = lista_mochilas[mochila_item_acao].index(0)
            lista_mochilas[mochila_item_acao][index_0] = item_acao
            print (f"{item_acao} adicionado na mochila {mochila_item_acao}.")
        else:
            print (f"Mochila {mochila_item_acao} cheia!")

quantidade_amigos = len(amigos)

for i in range (quantidade_amigos):
    quantidade_itens_i = len(lista_mochilas[i])
    print (f"Mochila de {amigos[i]} chegou assim:")
    for j in range (quantidade_itens_i):
        if (lista_mochilas[i][j]) != 0:
            print (lista_mochilas[i][j])

    