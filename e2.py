"""
Gabriel Ghiorghita / Engel Encarnación / Oscar Cordoba
10/10/2023
ASIX1c M03 UF1
Descripción: Numeros positivos y negativos
"""
def mostrar_triangle(alcada):
    for i in range(1, alcada + 1):
        # Imprimir espacios a la izquierda
        print(" " * (alcada - i), end="")

        # Imprimir números a la izquierda
        for j in range(1, i):
            print(j, end="")