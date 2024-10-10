# https://drive.google.com/file/d/1AsUib2XougnXeATj4JeHxRFKQnLUe4vj/view -> link da prova

vogais = "aeiou"

n_vogais = 0

nome = input()

for i in nome:
    if i.lower() in vogais:
        n_vogais+=1

print("frasco", n_vogais%3)