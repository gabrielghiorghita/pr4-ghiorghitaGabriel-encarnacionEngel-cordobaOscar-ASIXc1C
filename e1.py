"""
Gabriel Ghiorghita / Engel Encarnación / Oscar Cordoba
10/10/2023
ASIX1c M03 UF1
Descripción: Numeros positivos y negativos
"""

#Ponemos los contadores a 0
positivos = 0
negativos = 0
ceros = 0

#Pedimos al usuario que ingrese 10 números
for var in range(10):
    numero = float(input("Ingrese un número aleatorio: "))

#Verificamos si el número es +,-,0
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

#Mostramos los resultados, utilizando los contadores del principio.
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números iguales a cero: {ceros}")

