Cidade1 = input()
Nota1 = float(input())
Distância1 = int(input())
Cidade2 = input()
Nota2 = float(input())
Distância2 = int(input())
Cidade3 = input()
Nota3 = float(input())
Distância3 = int(input())
if 4 <= Nota1 > Nota2 and Nota3:
  print (Cidade1)
elif 4 <= Nota2 > Nota1 and Nota3:
  print (Cidade2)  
elif 4 <= Nota3 > Nota1 and Nota2:
  print (Cidade3)    
elif 4 <= Nota1 == Nota2 > Nota3 and Distância1 < Distância2:
    print (Cidade1)
elif 4 <= Nota1 == Nota3 > Nota2 and Distância1 < Distância3:
    print (Cidade1)
elif 4 <= Nota2 == Nota1 > Nota3 and Distância2 < Distância1:
    print (Cidade2)
elif 4 <= Nota2 == Nota3 > Nota1 and Distância2 < Distância3:
    print (Cidade3)
elif 4 <= Nota3 == Nota2 > Nota1 and Distância3 < Distância2:
    print (Cidade3)
elif 4 <= Nota1 == Nota2 == Nota3 and Distância2 > Distância1 < Distância3:
    print (Cidade1)
elif 4 <= Nota1 == Nota2 == Nota3 and Distância1 > Distância2 < Distância3:
    print (Cidade2)
elif 4 <= Nota1 == Nota2 == Nota3 and Distância1 > Distância3 < Distância2:
    print (Cidade3)
else:
  print ('Nota mínima não atingida')