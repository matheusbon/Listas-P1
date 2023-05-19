lista_numeros = input().split(" ")
lista_letras = []
tamanho_lista = len(lista_numeros)
    
def decifrador():    
    invalido = False
    for i in range (tamanho_lista):
        if int(lista_numeros[i]) <= 25:
            numero = int(lista_numeros[i]) + 97
            lista_letras.append(chr(numero))
        elif  25 < int(lista_numeros[i]) < 50:
            numero = int(lista_numeros[i]) + 71
            lista_letras.append(chr(numero))
        elif 49 < int(lista_numeros[i]) <= 75:            
            numero = int(lista_numeros[i]) + 15
            lista_letras.append(chr(numero))
        elif 75 < int(lista_numeros[i]) < 100:
            numero = int(lista_numeros[i]) - 11 
            lista_letras.append(chr(numero))
        elif int(lista_numeros[i]) == 100:
            lista_letras.append(' ')
        else:
            invalido = True

    if invalido == False:
        mensagem = ''.join(lista_letras)
        print (mensagem)
    else :
        print ('Infelizmente os números nao dizem nada')    

decifrador()
