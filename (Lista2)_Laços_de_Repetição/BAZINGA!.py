piada = ''
gostou = 0
nao_gostou = 0
while piada != 'Fim do Show!':
  piada = input()
  if piada != 'Fim do Show!':
    reacao = input()
    if reacao == 'BAZINGA!':
      gostou = gostou + 1
    else:
      nao_gostou = nao_gostou + 1
    
if gostou > (nao_gostou * 1.5):
    print ('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')
elif nao_gostou > (gostou * 1.5): 
    print ('Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!')
else:
    print ('Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!')
 