Temperatura = 30
Fome = True
Internet = 0

acao =''

while acao != 'parar':
    acao = input()
    if acao != 'ir para o grad' and acao != 'sair para a rua' and acao != 'comer uma quentinha' and acao != 'conectar no wifi' and acao != 'parar':
        print ('Entrada inválida')
    elif acao == 'ir para o grad':
        Temperatura = Temperatura - 5
        Internet = Internet + 300
    elif acao == 'sair para a rua':
        Temperatura = Temperatura + 5
    elif acao == 'comer uma quentinha':
        Fome = False 
    elif acao == 'conectar no wifi':
        Internet = Internet + 100

if Temperatura >= 30:
    print ('A temperatura aqui não está agradável')
elif Temperatura <= 25:
    print ('Agora sim, está aconchegante')

if Fome == True:
    print ('Meu corpo precisa de comida')

if Internet < 100:
    print ('Essa conexão está horrível')

if Fome == False and Temperatura <= 25 and Internet >= 300:
    print('Finalmente um lugar preciso para mim!')