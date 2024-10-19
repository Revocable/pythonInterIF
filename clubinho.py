codigo = []

for i in range(4):
    codigo.append(int(input()))

somaValida = False
soma = 0

soma=codigo[0]+codigo[1]+codigo[2]

if soma == codigo[3]:
    somaValida = True


codigoOriginal = codigo
codigo.sort()


verificar = False

if somaValida:
    for i in range(4):
        if codigoOriginal[i]==codigo[i]:
            verificar = True
        else:
            verificar = False

if verificar:
    print('LIBERADO')
else:
    print("NEGADO")