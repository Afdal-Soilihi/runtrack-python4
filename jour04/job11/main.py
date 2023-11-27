def augmenter_liste(L):
    for i in range(len(L)):
        L[i] += 1

# Création de la liste
ma_liste = [7, 11, 42, 39, 2]

# Appel de la fonction
augmenter_liste(ma_liste)
print("Liste après augmentation :", ma_liste)