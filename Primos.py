"""
David Bueno Cleybergh

>>> esPrimo(1)
True

>>> esPrimo(2)
True

>>> esPrimo(74211)
False

>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcmN(42, 60, 70, 63)
1260

>>> mcdN(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    """
    Devuelve true si el numero es primo y false si no lo es

    >>> for numero in range (2, 10): 
    ...     print(esPrimo(numero))
    True
    True
    False
    True
    False
    True
    False
    False
    """
    for prueba in range(2, numero):
        if numero % prueba == 0: return False
    return True

def primos(numero):
    """
    Devuelve todos los numeros primos menores que el numero seleccionado

    >>> print(primos(50))
    ...
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    """
    primos = []
    for n in range(2, numero):
        if esPrimo(n):  # Usa la función esPrimo para verificar si el número es primo
            primos.append(n)
    return tuple(primos)  # Devuelve los números primos como una tupla

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos del número.
    
    >>> descompon(36 * 175 * 143)
    ...
    (2, 2, 3, 3, 5, 5, 7, 11, 13)

    """
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factores)

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de dos números.
    
    >>> print(mcm(90, 14))
    ...
    630

    """
    from math import prod
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_unicos = set(factores1) | set(factores2)
    maximos = {factor: max(factores1.count(factor), factores2.count(factor)) for factor in factores_unicos}
    return prod(factor ** maximos[factor] for factor in maximos)

def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de dos números.
    
    >>> print(mcd(924, 780))
    ...
    12
    
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    comunes = set(factores1) & set(factores2)
    minimos = {factor: min(factores1.count(factor), factores2.count(factor)) for factor in comunes}
    from math import prod
    return prod(factor ** minimos[factor] for factor in minimos) if minimos else 1

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de un número arbitrario de argumentos.
    
    >>> print(mcmN(42, 60, 70, 63))
    ...
    1260
    """
    from functools import reduce
    return reduce(mcm, numeros)

def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de un número arbitrario de argumentos.

    >>> print(mcdN(840, 630, 1050, 1470))
    ...
    210
    """
    from functools import reduce
    return reduce(mcd, numeros)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

