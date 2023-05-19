tamanho_matriz = int(input())
lista_matriz = []
lista_linha = []
max_linha_valor = -999
lista_coluna = []
max_coluna_valor = -998
lista_diagonal = []
max_diagonal_valor = -997

for valores_coluna_horizontal in range(0, tamanho_matriz):
  valores_coluna_horizontal = input().split(' ')
  lista_matriz.append(valores_coluna_horizontal)
  
for linha_index in range(0, tamanho_matriz):
  for colun_index in range(0, tamanho_matriz - 1):
    valor1 = lista_matriz[linha_index][colun_index]
    valor2 = lista_matriz[linha_index][colun_index + 1]
    soma_elementos_linha = int(valor1) + int(valor2)
    if soma_elementos_linha > max_linha_valor:
      max_linha_valor = soma_elementos_linha
      caracter_parte_1 = valor1 + valor2

for linha_index in range(0, tamanho_matriz):
  for colun_index in range(0, tamanho_matriz - 1):
    valor3 = lista_matriz[colun_index][linha_index]
    valor4 = lista_matriz[colun_index + 1][linha_index]
    soma_elementos_colun = int(valor3) + int(valor4)
    if soma_elementos_colun > max_coluna_valor:
      max_coluna_valor = soma_elementos_colun
      caracter_parte_2 = valor3 + valor4
      
for linha_colun_index in range(0, tamanho_matriz - 1):
  valor5 = lista_matriz[linha_colun_index][linha_colun_index]
  valor6 = lista_matriz[linha_colun_index + 1][linha_colun_index + 1]
  soma_elementos_diagonal = int(valor5) + int(valor6)
  if soma_elementos_diagonal > max_diagonal_valor:
    max_diagonal_valor = soma_elementos_diagonal
    caracter_parte_3 = valor5 + valor6
    
senha = caracter_parte_1 + caracter_parte_2 + caracter_parte_3

print('Falei que era fácil Dustinzinho...')
print('Pegando todos os números que foram as combinações dos pares de cada sentido temos...')
print(f'Password: {senha}')