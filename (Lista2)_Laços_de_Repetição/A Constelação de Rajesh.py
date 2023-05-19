quantidade_estrelas = int(input())

pontuacao = 0
t1 = 0    
t2 = 1
t3 = 0
cont = 3
primo = True    

if quantidade_estrelas > 2:    

    n1 = 1
    n2 = 2
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    distancia_2 = (x1 - x2)**2 + (y1 - y2)**2
    distanciaf = distancia_2**(1/2)        
    distancia = int(distanciaf - (distanciaf%1))
    
    print (f'Distância [star{n1} <-> star{n2}]: {distancia}')
            
    n1 = n1 + 1
    n2 = n2 + 1 

    while cont <= 50:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        cont = cont + 1
        
        if distancia == t3:
            pontuacao = pontuacao + 1

    soma_distancias = distancia

    while n2 <= (quantidade_estrelas):
        x3 = int(input())
        y3 = int(input())    
        
        distancia_2 = (x2 - x3)**2 + (y2 - y3)**2
        distanciaf = distancia_2**(1/2)        
        distancia = int(distanciaf - (distanciaf%1))
        
        print (f'Distância [star{n1} <-> star{n2}]: {distancia}')
            
        n1 = n1 + 1
        n2 = n2 + 1 

        x2 = x3
        y2 = y3

        t1 = 0    
        t2 = 1
        t3 = 0
        cont = 3
        
        while cont <= 50:
            t3 = t1 + t2
            t1 = t2
            t2 = t3
            cont = cont + 1
            if distancia == t3:
                pontuacao = pontuacao + 1

        soma_distancias = soma_distancias + distancia

    n = (soma_distancias-1)

    while n > 1:
        if soma_distancias % n == 0:
            primo = False
        n = n - 1
    
    if pontuacao == (quantidade_estrelas - 1) and primo == False:
        print('Yes! Eu consegui!')
    elif pontuacao == (quantidade_estrelas - 1) and primo == True:
        print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')            
    elif pontuacao == (quantidade_estrelas - 2):
        print('Oh, não! Eu quase consegui!')
    elif pontuacao < (quantidade_estrelas - 2) and primo == False:
        print('Eu vou acabar como o Stuart :/')    
    elif pontuacao < (quantidade_estrelas - 2) and primo == True:
        print('Pelo menos o programa está funcionando...')      

else:
    if quantidade_estrelas <= 0:
        print('Isso está quebrado, acho que Howard pode me ajudar.')
    elif quantidade_estrelas > 0 and quantidade_estrelas < 3:
        print('Acho que bebi demais, eu juro que tinha mais estrelas!')    



      

