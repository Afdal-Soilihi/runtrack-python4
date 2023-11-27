def manipuler_liste():
    L = [1, 2, 3, 4, 5]

    # Afficher la deuxième valeur de la liste
    print("Deuxième valeur de la liste :", L[1])

    # Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
    def remplacer_par_somme():
        L[3] = L[2] + L[4]

    # Appel de la fonction pour effectuer le remplacement
    remplacer_par_somme()

    # Afficher à nouveau le tableau
    print("Liste après remplacement :", L)

    # Afficher la dernière valeur de la liste
    print("Dernière valeur de la liste :", L[-1])

# Appel de la fonction
manipuler_liste()