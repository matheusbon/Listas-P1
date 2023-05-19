doce1 = input()
quantidade_pe = int(input())
doce2 = input()
quantidade_cocada = int(input())
doce3 = input()
quantidade_maca = int(input())
valor_pe = 2
valor_cocada = 5
valor_maca = 3

fat_pe = valor_pe * quantidade_pe
fat_cocada = valor_cocada * quantidade_cocada
fat_maca = valor_maca * quantidade_maca

if fat_cocada < fat_pe > fat_maca:
    print (f'Oxe! Você ganhou {fat_pe} reais vendendo pe de moleque. O povo gostou, visse?!')
elif fat_pe < fat_cocada > fat_maca:
    print (f'Oxe! Você ganhou {fat_cocada} reais vendendo cocada. O povo gostou, visse?!')
elif fat_pe < fat_maca > fat_cocada:
    print (f'Oxe! Você ganhou {fat_maca} reais vendendo maca do amor. O povo gostou, visse?!')

if fat_pe == fat_cocada == fat_maca and fat_pe != 0:
    print (f'Oxe! Você ganhou {fat_pe} reais vendendo pe de moleque. O povo gostou, visse?!')
elif fat_pe == fat_cocada > fat_maca and fat_pe != 0:
    print (f'Oxe! Você ganhou {fat_pe} reais vendendo pe de moleque. O povo gostou, visse?!')
elif fat_pe == fat_maca > fat_cocada and fat_pe != 0:
    print (f'Oxe! Você ganhou {fat_pe} reais vendendo pe de moleque. O povo gostou, visse?!')
elif fat_maca == fat_cocada > fat_pe and fat_pe != 0:
    print (f'Oxe! Você ganhou {fat_maca} reais vendendo maca do amor. O povo gostou, visse?!')    

if fat_pe == 0 and fat_cocada == 0 and fat_maca == 0:
    print('A ideia foi peba! Acho melhor encontrar um novo jeito de ganhar dinheiro...')    