"""
Gabriel Ghiorghita / Engel Encarnación / Oscar Cordoba
10/10/2023
ASIX1c M03 UF1
Descripción: Multiplicació de dos nombres sencers mitjançant sumes.

"""
def multiplicacio(a, b):
    # Cas base: quan b és 0, el resultat és 0
    if b == 0:
        return 0
    # Cas general: suma "a" i crida recursiva amb "a" i "b-1"
    else:
        return a + multiplicacio(a, b-1)

# Programa principal
if __name__ == "__main__":
    # Demana a l'usuari dos nombres per multiplicar
    num1 = int(input("Introdueix el primer nombre: "))
    num2 = int(input("Introdueix el segon nombre: "))

    # Calcula la multiplicació utilitzant la funció
    resultat = multiplicacio(num1, num2)

    # Mostra el resultat
    print("El resultat de la multiplicació és:", resultat)


