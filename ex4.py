padrao = input().split(" ")
padrao = [int(x) for x in padrao]
qtde = int(input())

padroes = []
for i in range(qtde):
    padroes.append([int(x) for x in input().split(" ")])

nAnalises = int(input())
percentuais = []
for i in range(nAnalises):
    percentuais.append(int(input()))

counter = 0
qtdeIguais = 0
percentuaisPadroes = []

for i in padroes:
    for j in range(8):
        if i[j]==padrao[j]:
            qtdeIguais+=1
    percentuaisPadroes.append((qtdeIguais/8)*100)
    qtdeIguais = 0


for i in percentuais:
    counter = 0
    for j in percentuaisPadroes:
        if j >= i:  # Verifica se a similaridade é maior ou igual ao percentual mínimo
            counter += 1
    # Calcula e imprime a porcentagem de tubos que atendem à análise
    porcentagem = (counter / len(padroes)) * 100
    print(f"{porcentagem:.2f}")

    
