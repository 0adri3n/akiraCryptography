import math
import hashlib


class akiraCryptography:

    def __init__(self, key):
        self.__k = key


    def get_key(self): #Accesseur à la clé
        return self.__k


    def crypt(self, seq):

        key = self.get_key()

        key_value = int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % 10 ** 8  # Encrypting of the key in SHA256

        logkey = math.log(key_value)  # On récupère le logarithme néperien de ce précédent hash

        lst = []
        for n in str(logkey):
            lst.append(n)

        dec = lst[len(lst) - 2] + lst[len(lst) - 1]  # On récupère les deux derniers chiffres de la suite après la virgule

        dec_finale = int(dec) // math.log(int(dec))  # On divise la somme de ces deux derniers chiffres par son propre logarithme néperien

        pas = int(dec_finale)  # On garde le dernier résultat en tant que pas

        # On déchiffre la phrase qui sera entré par l'utilisateur avec le pas en chiffrement de César

        liste_lettre = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        phrase_codee = []

        phrase = seq.split()

        for mot in phrase:
            liste_mot = []
            for lettre in mot:
                i = liste_lettre.index(lettre)
                if i + pas > 25:
                    i -= 26
                liste_mot.append(liste_lettre[i + pas])
            phrase_codee.append("".join(liste_mot))
        print(" ".join(phrase_codee))


    def decrypt(self, seq):

        key = self.get_key()

        key_value = int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % 10 ** 8  # Encodage de la clé en hash SHA256

        logkey = math.log(key_value)  # On récupère le logarithme néperien de ce précédent hash

        lst = []
        for n in str(logkey):
            lst.append(n)

        dec = lst[len(lst) - 2] + lst[len(lst) - 1]  # On récupère les deux derniers chiffres de la suite après la virgule

        dec_finale = int(dec) // math.log(int(dec))  # On divise la somme de ces deux derniers chiffres par son propre logarithme néperien

        pas = int(dec_finale)  # On garde le dernier résultat en tant que pas

        # On déchiffre la phrase qui sera entré par l'utilisateur avec le pas en chiffrement de César

        liste_lettre = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        phrase_codee = []

        phrase = seq.split()

        for mot in phrase:
            liste_mot = []
            for lettre in mot:
                i = liste_lettre.index(lettre)
                if i - pas > 25:
                    i += 26
                liste_mot.append(liste_lettre[i - pas])
            phrase_codee.append("".join(liste_mot))

        print(" ".join(phrase_codee))

