pontuacao = 0
n = 0
n1 = 0
numero_arremessos = int(input())
lista1 = input().split()
lista2 = input().split()
dicionario_pontuacao = {}

try:
    while n != (numero_arremessos**2) and n1 != (numero_arremessos):
        if lista1[n] in lista2[n1]:
            pontuacao = pontuacao + 1
            n = n + 1
            lista2.pop(n1)    
            n1 = 0
        else:
            n1 = n1 + 1

except:
    if pontuacao == numero_arremessos:
        dicionario_pontuacao = {'resultado' : 'empate'}
    else:
        dicionario_pontuacao = {'resultado' : 'derrota'}

    if dicionario_pontuacao['resultado'] == 'empate':
        print ('Dale Gohan!')    
    else:
        print ('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')           



