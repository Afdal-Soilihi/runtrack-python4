def valeurs_extremes():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    minimum = L[0]
    maximum = L[0]
    
    for nombre in L:
        if nombre < minimum:
            minimum = nombre
        elif nombre > maximum:
            maximum = nombre
    
    valeur = L[3]  # Vous n'avez pas précisé quelle valeur vous vouliez récupérer, donc j'ai pris L[3] comme exemple
    
    print(f"Valeur : {valeur}, Minimum : {minimum}, Maximum : {maximum}")

# Appel de la fonction
valeurs_extremes()