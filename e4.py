BLANC = "⬜"
NEGRE = "⬛"

def imprimir_tauler():
    for fila in range(8):
        for columna in range(8):
            if (fila + columna) % 2 == 0:
                print(NEGRE, end=" ")
            else:
                print(BLANC, end=" ")
        print() #Salt a la següent linia al final de cada fila

#Imprimim el tayker tauler
imprimir_tauler()