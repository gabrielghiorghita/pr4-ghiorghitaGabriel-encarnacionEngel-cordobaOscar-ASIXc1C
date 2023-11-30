"""
Gabriel Ghiorghita / Engel Encarnación / Oscar Cordoba
10/10/2023
ASIX1c M03 UF1
Descripción: Multiplicació de dos nombres sencers mitjançant sumes.

"""
def suma(a, b):
    # Funció que suma dos nombres
    return a + b

def multiplicacio(a, b):
    # Funció que realitza la multiplicació mitjançant sumes successives
    resultat = 0
    for _ in range(b):
        resultat = suma(resultat, a)
    return resultat

# Programa principal
if __name__ == "__main__":
    # Demanem a l'usuari dos nombres per multiplicar
    num1 = int(input("Introdueix el primer nombre: "))
    num2 = int(input("Introdueix el segon nombre: "))

    # Calculem la multiplicació utilitzant la funció
    resultat = multiplicacio(num1, num2)

    # Mostrem el resultat
    print("El resultat de la multiplicació és:", resultat)


