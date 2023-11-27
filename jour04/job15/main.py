def arrondir_et_trier(L):
    for i in range(len(L)):
        L[i] = int(round(L[i]))

    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

# Exemple de liste de nombres décimaux
ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Appel de la fonction
arrondir_et_trier(ma_liste)
print("Liste arrondie et triée dans l'ordre croissant :", ma_liste)