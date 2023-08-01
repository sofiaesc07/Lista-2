def algoritmo(a, b):
    if a == 0:
        raise ValueError("El divisor 'a' no puede ser igual a cero.") #evitamos errores como que a sea cero

    if b == 0:
        return 0, 0  # Si el dividendo es cero, el cociente y el residuo son cero.

    #valores absolutos basados en la demostración
    b = abs(b)
    a  = abs(a)
    
    q = 0
    r = a


    #realizamos el calculo del residuo
    if a > b:
        if r > b:
            r = r - b
            q = q + 1

    # Si el residuo es negativo, ajustamos el cociente y el residuo
    if a < b:
        if r < 0:
            r = r + b
            q = q - 1

    return q, r

def imprimir():
    try:
        print('')
        a = int(input("Ingrese el valor de 'a': "))
        b = int(input("Ingrese el valor de 'b': "))
        q, r = algoritmo(a, b)
        print('')
        print(f"Cociente: {q}, Residuo: {r}")
        print('')
        print('b = qa + r')
        print(b, '=', (q*a) + r) #procuramos que se cumpla la igualdad
        print('')
    except ValueError as e:
        print("Error:", e)

imprimir()