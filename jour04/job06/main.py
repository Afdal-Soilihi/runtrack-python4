def echanger_premier_et_dernier():
    ma_liste = [1, 2, 3, 4, 5]
    ma_liste[0], ma_liste[-1] = ma_liste[-1], ma_liste[0]
    print("Liste après échange :", ma_liste)

# Appel de la fonction
echanger_premier_et_dernier()