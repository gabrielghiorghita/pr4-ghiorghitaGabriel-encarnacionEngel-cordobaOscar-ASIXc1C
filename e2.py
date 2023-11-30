"""
Gabriel Ghiorghita / Engel Encarnación / Oscar Cordoba
10/10/2023
ASIX1c M03 UF1
Descripción: Piràmide
"""
def imprimir_piramide(numero):
    if numero >= 9:
     for i in range(1, numero + 1):
        if i == numero:
            print(str(i) * (i))
        else:
            spaces = " " * (i - 1)
            if i == 1:
                print(str(i))
            else:
                print(str(i) + spaces + str(i))


numero_str = input("Introduce un número para la altura de tu pirámide: ")
numero = int(numero_str)

if numero <=9:
    imprimir_piramide(numero)
else:
 print("El número debe estar en el rango de 2 a 9.")

print("Programa finalizado, cerrando...")
