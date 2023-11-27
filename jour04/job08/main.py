def somme_valeurs_paires():
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    somme = sum(nombre for nombre in L if nombre % 2 == 0)
    print("Somme des valeurs paires :", somme)

# Appel de la fonction
somme_valeurs_paires()