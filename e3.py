def suma_parells_i_senars(limit):
    suma_parells = 0
    suma_senars = 0

    for num in range(limit):
        if num % 2 == 0:
            suma_parells += num
        else:
            suma_senars += num

    return suma_parells, suma_senars

# Demana a l'usuari el límit
limit = int(input("Introdueix un número límit: "))

# Calcula les sumes
suma_parells, suma_senars = suma_parells_i_senars(limit)

# Mostra els resultats
print(f"La suma dels nombres parells fins a {limit} és: {suma_parells}")
print(f"La suma dels nombres senars fins a {limit} és: {suma_senars}")
