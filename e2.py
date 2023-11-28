"""
Gabriel Ghiorghita / Engel Encarnación / Oscar Cordoba
10/10/2023
ASIX1c M03 UF1
Descripción: Numeros positivos y negativos
"""
def imprimir_piramide(numero):
    for i in range(1, numero + 1):
        if i == numero:
            print(str(i) * (2* i- 1))
        else:
            spaces = " " * (i - 1)
            if i == 1:
                print(str(i))
            else:
                print(str(i) + spaces + str(i))


numero_str = input("Introduce un número para la altura de tu pirámide: ")

numero = int(numero_str)

imprimir_piramide(numero)

print("Programa finalizado, cerrando...")
