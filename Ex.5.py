BLANC = "⬜"
NEGRE = "⬛"

def imprimir_tauler():
    for fila in range(8):
        for columna in range(8):
            if (fila + columna) % 2 == 0:
                print(BLANC, end=" ")
            else:
                print(NEGRE, end=" ")
        print() #Salt a la següent linia al final de cada fila

#Imprimir tauler
imprimir_tauler()