def verifica_parentese(elemento, caracter):
    if elemento == '':
        return 0
    else:
        if elemento[0] == caracter:
            return 1 + verifica_parentese(elemento[1:],caracter)
        else:
            return 0 + verifica_parentese(elemento[1:],caracter)

quantidade_operacoes = int(input())
equacoes = []

for i in range(quantidade_operacoes):
    equacoes.append(input())

for eq in equacoes:
    right = verifica_parentese(eq, '(')                
    left = verifica_parentese(eq, ')')

    if right == left:
        print ('Essa sentença está com os parênteses balanceados, HOORAY!')
    elif right > left:
        print ('A quantidade de parênteses \'(\' está maior que a de \')\', vamos descartá-la')
    else:
        print ('A quantidade de parênteses \')\' está maior que a de \'(\', vamos descartá-la')      