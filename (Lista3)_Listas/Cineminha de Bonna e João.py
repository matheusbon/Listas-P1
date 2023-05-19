dono_lista = input()
print(f'Os filmes sugeridos por {dono_lista} são:')
quantidade_entradas = int(input())
n = 0

nomes_filmes = []
notas_filmes = []

while n != quantidade_entradas:
  entrada = input().split(" - ")
  nomes_filmes.append(entrada[0])
  notas_filmes.append(entrada[1])
  
  n = n + 1

size = len(notas_filmes)
for i in range(size -1):
  for j in range (size -i -1):
      if notas_filmes[j] < notas_filmes[j + 1]:
          nota_aux = notas_filmes[j]
          notas_filmes[j] = notas_filmes[j + 1]
          notas_filmes[j + 1] = nota_aux
          nome_aux = nomes_filmes[j]
          nomes_filmes[j] = nomes_filmes[j + 1]
          nomes_filmes[j + 1] = nome_aux

n = 0
while n != quantidade_entradas:
  print(f'{nomes_filmes[n]} - {notas_filmes[n]}')
  n = n + 1




            