import string # Import pour une liste alphabet

# Acquisition du texte par input utilisateur
def Acquerir_Texte():       
    texte = input("Saisissez un texte finissant par un point.")
    # Vérification des conditions (>80 + fini par un point)
    if texte.endswith("."):
        if len(texte) > 80:
            print("Veuillez saisir au maximum 80 caractères")
        else:
            print("Acquisition finie, voici votre texte : ")
            return texte


def Afficher_Texte(texte): # Simple print
    print(texte)


def Acquerir_Cle():         # Acquisition de la clé par input utilisateur
    cle = int(input("Saisissez une clé entre 0 et 25 : "))
    if (cle >= 0) & (cle <= 25):
        print("Clé acceptable") 
        return cle
    else:
        print("Veuillez saisir une clé entre 0 et 25 : ")

# Chiffrage en se référant à l'alphabet, prenant une clé et un texte finissant par un point en paramètre 
def Chiffre_Texte(cle, texte):          
    alphabet_min = list(string.ascii_lowercase)
    alphabet_maj = list(string.ascii_uppercase)
    
    texteConverti = list(texte)

    for i in range(len(texteConverti)): # Vérification si la lettre est minuscule 
        if texteConverti[i] in alphabet_min:
            if texteConverti[i] == ".":
                print("Texte fini")
            else:
                pos = alphabet_min.index(texteConverti[i])
                nouvelle_pos = (pos + cle) % 26 # modulo 26 pour reboucler sur l'alphabet
                texteConverti[i] = alphabet_min[nouvelle_pos]

        elif texteConverti[i] == " ":
            print("passe")

        elif texteConverti[i] in alphabet_maj: # Vérification si la lettre est majuscule
            if texteConverti[i] == ".":
                print("Texte fini")
            else:
                pos = alphabet_maj.index(texteConverti[i])
                nouvelle_pos = (pos + cle) % 26 # modulo 26 pour reboucler sur l'alphabet
                texteConverti[i] = alphabet_maj[nouvelle_pos]
    return "".join(texteConverti)

# On prend simplement la clé négative pour déchiffrer
def Dechiffre_Texte(cle, texte):
    return Chiffre_Texte(-cle, texte) 

# Retrouver un texte à partir du texte chiffré et du premier caractère original
def Decoder_Cle_V1(txt_c, car_c): #
    alpha = string.ascii_lowercase
    
    txt_c = txt_c.lower() # Texte chiffré
    car_c = car_c.lower() # Premier caractère

    for caractere in txt_c:
        if caractere in alpha:
            pc = alpha.index(caractere)
            break

    pp = alpha.index(car_c)

    cle = (pc - pp) % 26 # modulo 26 pour reboucler sur l'alphabet
    return cle

# Retrouver la clé de chiffrement à partir d'un texte chiffré passé en paramètre
def Decoder_Cle_V2(txt_c): 
    alpha = string.ascii_lowercase
    txt_c = txt_c.lower() # Passage en minuscules pour un comptage global
    
    max_occurrences = 0
    lettre_frequente = ''
    
    # Recherche de la lettre la plus présente
    for lettre in alpha:
        occurrences = txt_c.count(lettre)
        if occurrences > max_occurrences:
            max_occurrences = occurrences
            lettre_frequente = lettre

    # Si aucune lettre n'est trouvée, on renvoie 0    
    if lettre_frequente == '':
        return 0 
        
    # Calcul du décalage par rapport à l'index de la lettre e
    index_e = alpha.index('e')
    index_max = alpha.index(lettre_frequente)
    
    cle = (index_max - index_e) % 26 # modulo 26 pour reboucler sur l'alphabet
    
    return cle

# Programme principal
def main():
    texte = Acquerir_Texte()
    Afficher_Texte(texte)

    cle = Acquerir_Cle()

    textechiffre = Chiffre_Texte(cle, texte)
    Afficher_Texte(textechiffre)

    texteDechiffre = Dechiffre_Texte(cle, textechiffre)
    Afficher_Texte(texteDechiffre)

    cle = Decoder_Cle_V1("Fsrnsyv.", "B")
    Afficher_Texte(cle)

    # Test Décodage V2 pour montrer que le e est omniprésent via une phrase longue
    # Avec ce type d'analyse de lettres, on ne peut pas avoir de résultats un minimum précis avec "Bonjour."
    textechiffre = "qj rjxxflj xjhwjy vzj stzx jyzintsx rtsywj vzj qf qjyywj j jxy wjjqqjrjsy qf uqzx uwjxjsyj." 
    cle2 = Decoder_Cle_V2(textechiffre)
    Afficher_Texte(cle2)

if __name__ == "__main__":
    main()