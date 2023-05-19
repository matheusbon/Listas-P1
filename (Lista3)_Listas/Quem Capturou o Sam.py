suspeitos = input().split(",")

while len(suspeitos) != 1:
  entrada = input()

  if entrada == "Não encontrei nada no primeiro suspeito":
    suspeitos.pop(0)
  
  elif entrada == "O último da lista está limpo":
    suspeitos.pop(-1)
  
  elif entrada == "Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita":
    tamanho_lista = int(len(suspeitos))
    if tamanho_lista % 2 == 0:
        tamanho_lista_par = int(tamanho_lista_par / 2)
        suspeitos.pop(tamanho_lista_par)
    elif tamanho_lista % 2 != 0:
        tamanho_lista_impar = int((tamanho_lista - 1) / 2) 
        suspeitos.pop(tamanho_lista_impar)
  
  elif entrada == "Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:":
    posicao = int(input())
    suspeitos.pop(posicao)   
  
  elif entrada == "Acho que temos mais uma opção a ser analisada…":
    novo_suspeito = input()
    suspeitos.append(novo_suspeito)
  
  else:
      print ("Isso não estava no combinado, a lista vai permanecer do mesmo jeito")

else:
    nome_suspeito = ("".join(suspeitos))
    print (f"Acho que encontramos o suspeito. O seu nome é {nome_suspeito}, vamos salvar o Sam!")  