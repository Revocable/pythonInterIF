def tempo_para_segundos(tempo):
    minutos, resto = tempo.split(':')
    segundos, milissegundos = resto.split('.')
    return int(minutos) * 60 + int(segundos) + int(milissegundos) / 1000

# Leitura da entrada
ent = input()

abc = ent.split(" ")
qtde_pilotos = int(abc[0])
qtde_voltas = int(abc[1])
qtde_voltas_inv = int(abc[2])

# Leitura dos pilotos e criação do dicionário de siglas para nomes completos
pilotos = []
siglas_para_nomes = {}

for i in range(qtde_pilotos):
    nome_completo = input()
    pilotos.append(nome_completo)
    sigla = nome_completo[:3].upper()  # Gera a sigla a partir das 3 primeiras letras do nome
    siglas_para_nomes[sigla] = nome_completo

# Leitura das voltas
voltas = []

for i in range(qtde_voltas):
    voltas.append(input())

# Remoção das voltas inválidas
for i in range(qtde_voltas_inv):
    voltas.remove(input())

# Separação das voltas e pilotos
voltasFinal = []
for i in voltas:
    voltasFinal.append(i.split(" "))

# Ordena as voltas pelo tempo
voltasOrdenadas = sorted(voltasFinal, key=lambda x: tempo_para_segundos(x[1]))

# Dicionário para armazenar a melhor volta de cada piloto
melhoresVoltas = {}

for volta in voltasOrdenadas:
    piloto_sigla, tempo = volta
    if piloto_sigla not in melhoresVoltas:
        melhoresVoltas[piloto_sigla] = tempo

# Ordena os pilotos pelas suas melhores voltas
classificacao = sorted(melhoresVoltas.items(), key=lambda x: tempo_para_segundos(x[1]))

# Exibe a classificação final com o nome completo
for i, (piloto_sigla, melhor_tempo) in enumerate(classificacao, start=1):
    nome_completo = siglas_para_nomes[piloto_sigla]  # Recupera o nome completo pela sigla
    print(f"{i} {nome_completo} {melhor_tempo}")
