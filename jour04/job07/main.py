def compter_multiples_de_trois():
    L = [8, 24, 48, 2, 16]
    nombre_multiples_trois = sum(1 for nombre in L if nombre % 3 == 0)
    print("Nombre de multiples de 3 dans la liste :", nombre_multiples_trois)

# Appel de la fonction
compter_multiples_de_trois()