def supprimer_doublons(L):
    i = 0
    while i < len(L):
        j = i + 1
        while j < len(L):
            if L[i] == L[j]:
                L.pop(j)
            else:
                j += 1
        i += 1

# Exemple de liste avec des doublons
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Appel de la fonction
supprimer_doublons(ma_liste)
print("Liste sans doublons :", ma_liste)