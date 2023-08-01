    
def mcd(a, b):
    # Implementación del algoritmo de Euclides para calcular el mcd
    while b != 0:
        a, b = b, a % b
    return abs(a)

def primo(a, b):
    return mcd(a, b) == 1

def paresprimos(r): #funcion que cuenta los pares primos en la region
    count = 0
    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            if primo(x, y):
                count += 1
    return count

def densidad(r): #calculo de densidad
    return paresprimos(r) / ((2 * r + 1) ** 2)

#elegir r, entre mayor sea, mejor precisión del calculo
r = 49

# Contar los pares de números primos relativos en la región
numparesp = paresprimos(r)

# Calcular la densidad de pares primos relativos y comparar con 6/π^2
densidad1 = densidad(r)
densidad2 = 6 / (3.14159265358979323846 ** 2)

print('')
print('r elegido:', r)
print("Pares primos relativos en la región:", numparesp)
print("Densidad obtenida:", densidad1)
print("Densidad esperada (6/π^2):", densidad2)
print('')
