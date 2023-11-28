
"""
Gabriel Razvan Ghiorghita
23/11/2023
ASIXc1C M03 UF1
Activitat: Piramid

"""
def imprimir_piramide(numero):
    for i in range(1, numero + 1):
        print("#" * i)

numero_str = input("Introdueix un número per a l'altura de la teva piràmide: ")

numero = int(numero_str)

print(imprimir_piramide(numero))
print("Programa finalitzat, tancant...")


#VERSIÓ CLASSE:

#TOTXO = "#"
#alçada = int(input())
#for nivell in range (1,alçada+1):
    #print(TOTXO * nivell)