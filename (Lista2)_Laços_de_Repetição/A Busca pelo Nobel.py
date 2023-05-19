mensagem = 'nada'
encerrou = False 
pontuacao = 0

while encerrou == False:
    mensagem = input()

    if pontuacao == 0:
        if mensagem == 'Começou a Trabalhar na Caltech':
            mensagem = input()
            if mensagem != 'Bazinga':
                pontuacao = pontuacao + 1
            
        elif mensagem == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or mensagem == 'Leonard seu anão covarde' or mensagem == 'Tu é muito burro Raj':
            print ('Não xingue seus amigos Sheldon!')
            
        if mensagem == 'É o fim da Estrada pra Sheldon Cooper' or pontuacao == 6:
          encerrou = True    
        
        
    if pontuacao == 1:
        if mensagem == 'Trabalho sobre a String Theory':
            mensagem = input()
            if mensagem != 'Bazinga':
                pontuacao = pontuacao + 1
            
        elif mensagem == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or mensagem == 'Leonard seu anão covarde' or mensagem == 'Tu é muito burro Raj':
            print ('Não xingue seus amigos Sheldon!')
        
        if mensagem == 'É o fim da Estrada pra Sheldon Cooper' or pontuacao == 6:
          encerrou = True

    if pontuacao == 2:
        if mensagem == 'Ganhar o Chancellor de ciência':
            mensagem = input()
            if mensagem != 'Bazinga':
                pontuacao = pontuacao + 1
            
        elif mensagem == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or mensagem == 'Leonard seu anão covarde' or mensagem == 'Tu é muito burro Raj':
            print ('Não xingue seus amigos Sheldon!')        
        
        if mensagem == 'É o fim da Estrada pra Sheldon Cooper' or pontuacao == 6:
          encerrou = True

    if pontuacao == 3:
        if mensagem == 'Pensar na Teoria de Cooper-Hofstader':
            mensagem = input()
            if mensagem != 'Bazinga':
                pontuacao = pontuacao + 1
            
        elif mensagem == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or mensagem == 'Leonard seu anão covarde' or mensagem == 'Tu é muito burro Raj':
            print ('Não xingue seus amigos Sheldon!') 

        if mensagem == 'É o fim da Estrada pra Sheldon Cooper' or pontuacao == 6:
          encerrou = True
        
    if pontuacao == 4:
        if mensagem == 'Criou a Super Assimetria':
            mensagem = input()
            if mensagem != 'Bazinga':
                pontuacao = pontuacao + 1
            
        elif mensagem == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or mensagem == 'Leonard seu anão covarde' or mensagem == 'Tu é muito burro Raj':
            print ('Não xingue seus amigos Sheldon!') 
        
        if mensagem == 'É o fim da Estrada pra Sheldon Cooper' or pontuacao == 6:
          encerrou = True

    if pontuacao == 5:
        if mensagem == 'Ganhar o Nobel':
            pontuacao = pontuacao + 1
            
        elif mensagem == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or mensagem == 'Leonard seu anão covarde' or mensagem == 'Tu é muito burro Raj':
            print ('Não xingue seus amigos Sheldon!') 
        
        if mensagem == 'É o fim da Estrada pra Sheldon Cooper' or pontuacao == 6:
          encerrou = True

if encerrou == True:
    if pontuacao == 0:
        print ('Que potencial desperdiçado...')

    elif pontuacao == 1 or pontuacao == 2:
        print ('Tão perto, mas tão longe')

    elif pontuacao == 3 or pontuacao == 4:
        print ('Não desista Sheldon, você ainda têm muito para alcançar!')

    elif pontuacao == 5:
        print ('Nãoooooo, esse momento ia ser seu Sheldon')

    elif pontuacao == 6:
        print ('Você conseguiu Sheldon, o Nobel é seu!!!')


       
            



       
            

