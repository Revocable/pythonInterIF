N = int(input())

cedulas = []
for i in range(N):
    cedula = int(input())
    cedulas.append(cedula)

cedulas.sort(reverse=True)

valor_cheque = int(input())

total_cedulas = 0

for cedula in cedulas:
    # Calcula quantas vezes essa cédula cabe no valor restante
    quantidade = valor_cheque // cedula
    # Adiciona ao total de cedulas
    total_cedulas += quantidade
    # Subtrai do valor do cheque
    valor_cheque -= quantidade * cedula


print(total_cedulas)