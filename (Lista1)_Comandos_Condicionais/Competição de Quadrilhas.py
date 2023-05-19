nome_da_quadrilha = input()
passo_1 = input()
passo_2 = input()
passo_3 = input()
passo_4 = input()
passo_5 = input()
pontuacao = 0.0
foi_casamento = False
zerou = False

if passo_1 == "Cumprimento":
  pontuacao = pontuacao + 100
elif passo_1 == "Balancê":
  pontuacao = pontuacao + 50
elif passo_1 == "Passeio":
  pontuacao = pontuacao + 70
elif passo_1 == "Túnel":
  pontuacao = pontuacao * 0.9
elif passo_1 == "Serrote":
  pontuacao = pontuacao + 100
elif passo_1 == "Casamento":
  foi_casamento = True
elif passo_1 == "Despedida":
  pontuacao = pontuacao  
else:
  zerou = True 

if passo_2 == "Cumprimento":
  pontuacao = pontuacao + 10
elif passo_2 == "Balancê":
  pontuacao = pontuacao + 50
elif passo_2 == "Passeio":
  pontuacao = pontuacao + 70
elif passo_2 == "Túnel":
  pontuacao = pontuacao * 0.9
elif passo_2 == "Serrote":
  pontuacao = pontuacao + 100
elif passo_2 == "Casamento":
  foi_casamento = True
elif passo_2 == "Despedida":
  pontuacao = pontuacao  
else:
  zerou = True

if passo_3 == "Cumprimento":
  pontuacao = pontuacao + 10
elif passo_3 == "Balancê":
  pontuacao = pontuacao + 50
elif passo_3 == "Passeio":
  pontuacao = pontuacao + 70
elif passo_3 == "Túnel":
  pontuacao = pontuacao * 0.9
elif passo_3 == "Serrote":
  pontuacao = pontuacao + 100
elif passo_3 == "Casamento":
  foi_casamento = True
elif passo_3 == "Despedida":
  pontuacao = pontuacao  
else:
  zerou = True
  
if passo_4 == "Cumprimento":
  pontuacao = pontuacao + 10
elif passo_4 == "Balancê":
  pontuacao = pontuacao + 50
elif passo_4 == "Passeio":
  pontuacao = pontuacao + 70
elif passo_4 == "Túnel":
  pontuacao = pontuacao * 0.9
elif passo_4 == "Serrote":
  pontuacao = pontuacao + 100
elif passo_4 == "Casamento":
  foi_casamento = True
elif passo_4 == "Despedida":
  pontuacao = pontuacao  
else:
  zerou = True  

if passo_5 == "Cumprimento":
  pontuacao = pontuacao + 10
elif passo_5 == "Balancê":
  pontuacao = pontuacao + 50
elif passo_5 == "Passeio":
  pontuacao = pontuacao + 70
elif passo_5 == "Túnel":
  pontuacao = pontuacao * 0.9
elif passo_5 == "Serrote":
  pontuacao = pontuacao + 100
elif passo_5 == "Casamento":
  foi_casamento = True
elif passo_5 == "Despedida":
  pontuacao = pontuacao + 35  
else:
  zerou = True
  
if foi_casamento == True:
  pontuacao = pontuacao * 2
  
if zerou == False:
  print (f"Parabéns, {nome_da_quadrilha}! Bela apresentação. A pontuação foi de {pontuacao}!")
if zerou == True:
  print (f"Poxa, {nome_da_quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.")
  