n = int(input())

numerosPrimos = []

def ehPrimo(n):
    if n <= 1:
        return False  
    for i in range(2, n): 
        if n % i == 0: 
            return False
    return True  


for i in range(n+1):
    if ehPrimo(i):
        numerosPrimos.append(str(i))

print(" ".join(numerosPrimos))

