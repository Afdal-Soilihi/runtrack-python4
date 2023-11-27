def tri_croissant_liste(L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

# Exemple de liste
ma_liste = [5, 2, 8, 1, 3]

# Appel de la fonction
tri_croissant_liste(ma_liste)
print("Liste triée dans l'ordre croissant :", ma_liste)