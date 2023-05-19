Pokedex = {}
encerrou = False

while encerrou == False:
    
    try:  
        entrada_poke = input().split()
        
        if entrada_poke[0] == 'ADD' :            
            if entrada_poke[1] in Pokedex.keys():            
                print ('Pokémon já adicionado na Pokédex')
            else:
                entrada_desc = input()
                Pokedex.update({entrada_poke[1] : entrada_desc})
                print ('Pokémon adicionado com sucesso')

        elif entrada_poke[0] == 'DESC' :
            if entrada_poke[1] in Pokedex.keys():
                print (Pokedex[entrada_poke[1]])
            else:
                print ('Ainda não há registro desse Pokémon')

    except:
        encerrou = True
        break 
        