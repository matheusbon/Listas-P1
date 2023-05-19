def soma_matrizes(m1, m2):
    resultado = []
    for i in range(len(m1)):
        resultado.append([])
        for j in range(len(m1[0])):
            resultado[i].append(m1[i][j] + m2[i][j])
    return resultado


def substracao_matrizes(m1, m2):
    resultado = []
    for i in range(len(m1)):
        resultado.append([])
        for j in range(len(m1[0])):
            resultado[i].append(m1[i][j] - m2[i][j])
    return resultado


def multiplicacao_matrizes(m1, m2):
    def getLinha(matriz, n):
        return [i for i in matriz[n]]  

    def getColuna(matriz, n):
        return [i[n] for i in matriz]

    mat1lin = len(m1)
    mat2col = len(m2[0])

    matRes = []
    for i in range(mat1lin):
        matRes.append([])
        for j in range(mat2col):
            listMult = [x * y for x, y in zip(getLinha(m1, i), getColuna(m2, j))]
            matRes[i].append(sum(listMult))

    return matRes


def multiplicacao_escalar(matrix, k):
    resultado = []
    for line in matrix:
        resultado.append([elem * k for elem in line])
    return resultado


N = int(input())

M1 = []
for index in range(N):
    line = input().split(' ')
    M1.append([int(i) for i in line])

M2 = []
for index in range(N):
    line = input().split(' ')
    M2.append([int(i) for i in line])

qtd_op = int(input())

operations = []
for index in range(qtd_op):
    line = input().split(' ')
    operations.append(line)

resultado = []
for operation in operations:
    if operation[0] == 'm1' and '*' not in operation:
        Ma = None
        if operation[2] == 'm1':
            Ma = M1
        else:
            Ma = M2
        Mb = None
        if operation[4] == 'm1':
            Mb = M1
        else:
            Mb = M2
        if operation[3] == '+':
            resultado = soma_matrizes(Ma, Mb)
            M1 = resultado
        elif operation[3] == '-':
            resultado = substracao_matrizes(Ma, Mb)
            M1 = resultado
        elif operation[3] == '.':
            resultado = multiplicacao_matrizes(Ma, Mb)
            M1 = resultado
    elif operation[0] == 'm1' and '*' in operation:
        A = None
        B = None
        if operation[2] == 'm1' or operation[2] == 'm2':
            if operation[2] == 'm1':
                A = M1
            else:
                A = M2
            B = int(operation[4])
        else:
            B = int(operation[2])
            if operation[4] == 'm1':
                A = M1
            else:
                A = M2
        resultado = multiplicacao_escalar(A, B)
        M1 = resultado
    elif operation[0] == 'm2' and '*' not in operation:
        Ma = None
        if operation[2] == 'm1':
            Ma = M1
        else:
            Ma = M2
        Mb = None
        if operation[4] == 'm1':
            Mb = M1
        else:
            Mb = M2
        if operation[3] == '+':
            resultado = soma_matrizes(Ma, Mb)
            M2 = resultado
        elif operation[3] == '-':
            resultado = substracao_matrizes(Ma, Mb)
            M2 = resultado
        elif operation[3] == '.':
            resultado = multiplicacao_matrizes(Ma, Mb)
            M2 = resultado
    elif operation[0] == 'm2' and '*' in operation:
        A = None
        B = None
        if operation[2] == 'm1' or operation[2] == 'm2':
            if operation[2] == 'm1':
                A = M1
            else:
                A = M2
            B = int(operation[4])
        else:
            B = int(operation[2])
            if operation[4] == 'm1':
                A = M1
            else:
                A = M2
        resultado = multiplicacao_escalar(A, B)
        M2 = resultado

for line in resultado:
    s = ' '
    cLine = [str(i) for i in line]
    print(s.join(cLine))