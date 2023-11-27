def my_long_word(longueur, texte):
    mots = texte.split()
    result = " ".join(mot for mot in mots if len(mot) > longueur)
    return result

# Exemple d'appel de la fonction
resultat_job_14 = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output :", resultat_job_14)