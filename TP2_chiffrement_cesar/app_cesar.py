import tkinter as tk
from tkinter import messagebox
import os

# Importation des fonctions depuis l'autre fichier de l'étape 1 et 2 
from fonctions_cesar import Chiffre_Texte, Dechiffre_Texte, Decoder_Cle_V1, Decoder_Cle_V2

# Permet d'aller chercher le texte que l'utilisateur veut chiffrer ou déchiffrer
def _extraireSource(choixSource, saisie, fichier, choixCle, v1Txt, v2Txt):
    # Si on utilise un décodeur, on prend directement le texte associé
    if choixCle == 2:
        return v1Txt.get()
    elif choixCle == 3:
        return v2Txt.get()

    # Sinon comportement normal
    if choixSource == 1:
        contenu = saisie.get().strip()
        if not contenu:
            raise ValueError("Le champ de saisie est vide.")
        return contenu
    else:
        chemin = fichier.get().strip()
        if not os.path.exists(chemin):
            raise FileNotFoundError(f"Fichier introuvable :\n{chemin}")
        with open(chemin, "r", encoding="utf-8") as f:
            return f.read()

# Suivant le choix on fait appel aux  fonctions présentes dans le fichier métier
def _determinerCle(choix, manuelle, v1Car, v1Txt, v2Txt):
    if choix == 1:
        val = manuelle.get().strip()
        if not val:
            raise ValueError("Aucune clé saisie.")
        return int(val)
    elif choix == 2:
        return Decoder_Cle_V1(v1Txt.get(), v1Car.get())
    elif choix == 3:
        return Decoder_Cle_V2(v2Txt.get())


# Déclanchée lorsque que le bouton de validation est déclanché
def executerOperation():
    try:
        # Gestion de la source du texte suivant le choix
        src = _extraireSource(choixSource.get(),champSaisieUtilisateur,champSourceFichier,choixCle.get(),champV1Txt,champV2Txt)
        # Gestion de la clé et vérification de la validité de la clé
        cle = _determinerCle(choixCle.get(), champCleManuelle, champV1Car, champV1Txt, champV2Txt)
        # Chiffrement / déchiffrement / décodage
        if choixCle.get() in [2, 3]:
            # on affiche explicitement la clé décodée
            texte_dechiffre = Dechiffre_Texte(cle, src)
            res = f"Clé décodée : {cle}\n\nTexte déchiffré :\n{texte_dechiffre}"
            champCleManuelle.delete(0, tk.END)
            champCleManuelle.insert(0, str(cle))
        else:
            if choixMode.get() == 1:
                res = Chiffre_Texte(cle, src)
            else:
                res = Dechiffre_Texte(cle, src)

        # Affichage ou sérialisation suivant le choix radio 
        if choixAffichage.get() == 1:
            zoneAffichage.delete("1.0", tk.END) # On vide l'écran
            zoneAffichage.insert(tk.END, res) # On écrit le résultat
        else:
            chemin = champAffichageFichier.get().strip()
            if not chemin:
                raise ValueError("Veuillez indiquer un chemin pour sauvegarder le fichier.") # Erreur si chemin vide
            with open(chemin, "w", encoding="utf-8") as f:
                f.write(res)
            messagebox.showinfo("Succès", f"Résultat sauvegardé dans :\n{chemin}")

    # Gestion d'erreurs saisie, fichier
    except ValueError as e:
        messagebox.showerror("Erreur de saisie", str(e))
    except FileNotFoundError as e:
        messagebox.showerror("Erreur fichier", str(e))
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

# Mets à jour les champs lorsque les décodages V1 et V2 sont sélectionnés
def updateUI_cle():
    if choixCle.get() in [2, 3]:  # V1 ou V2
        champSaisieUtilisateur.config(state="disabled")
        champSourceFichier.config(state="disabled")
        rbSourceSaisie.config(state="disabled")
        rbSourceFichier.config(state="disabled")
        rbModeChiffrer.config(state="disabled")
        rbModeDechiffrer.config(state="disabled")
        # On définit le mode de traitement sur le déchiffrement
        choixMode.set(2)
    else:
        champSaisieUtilisateur.config(state="normal")
        champSourceFichier.config(state="normal")
        rbSourceSaisie.config(state="normal")
        rbSourceFichier.config(state="normal")
        rbModeChiffrer.config(state="normal")
        rbModeDechiffrer.config(state="normal")

# Création fenêtre principale
fen= tk.Tk()
fen.title("Appli_Chiffrement_César")
fen.geometry("800x500")
fen.configure(padx=20, pady=20)

# Variables globale pour contrôler
choixCle= tk.IntVar(value=1)
choixSource = tk.IntVar(value=1)
choixAffichage= tk.IntVar(value=1)
choixMode= tk.IntVar(value=1)

# Colonne gauche

# Bloc : Type de clé 
tk.Label(fen, text="Type de clé").grid(row=0, column=0, sticky="w")
frameCle = tk.Frame(fen, bg="yellow", bd=2, relief="groove", padx=10, pady=10)
frameCle.grid(row=1, column=0, sticky="ew", pady=(0, 20))

tk.Radiobutton(frameCle, text="Saisie utilisateur", variable=choixCle, value=1, bg="yellow", command=updateUI_cle).grid(row=0, column=0, sticky="w") # Bouton radio 
champCleManuelle = tk.Entry(frameCle, width=5)
champCleManuelle.grid(row=0, column=1, sticky="w", padx=5)

tk.Radiobutton(frameCle, text="Decoder_Cle_V1", variable=choixCle, value=2, bg="yellow", command=updateUI_cle).grid(row=1, column=0, sticky="w")
champV1Car = tk.Entry(frameCle, width=5)
champV1Car.grid(row=1, column=1, padx=5)
champV1Txt = tk.Entry(frameCle, width=20)
champV1Txt.grid(row=1, column=2, padx=5)

tk.Radiobutton(frameCle, text="Decoder_Cle_V2", variable=choixCle, value=3, bg="yellow", command=updateUI_cle).grid(row=2, column=0, sticky="w")
champV2Txt = tk.Entry(frameCle, width=27)
champV2Txt.grid(row=2, column=1, columnspan=2, padx=5, sticky="w")

# Bloc : Source du texte
tk.Label(fen, text="Source du texte").grid(row=2, column=0, sticky="w")
frameSource = tk.Frame(fen, bg="green", bd=2, relief="groove", padx=10, pady=10)
frameSource.grid(row=3, column=0, sticky="ew", pady=(0, 20))

tk.Radiobutton(frameSource, text="Saisie utilisateur", variable=choixSource, value=1, bg="green").grid(row=0, column=0, sticky="w")
rbSourceSaisie = tk.Radiobutton(frameSource, text="Saisie utilisateur", variable=choixSource, value=1, bg="green")
rbSourceSaisie.grid(row=0, column=0, sticky="w")
champSaisieUtilisateur = tk.Entry(frameSource, width=40)
champSaisieUtilisateur.grid(row=0, column=1, padx=5)

rbSourceFichier = tk.Radiobutton(frameSource, text="Fichier texte", variable=choixSource, value=2, bg="green")
rbSourceFichier.grid(row=1, column=0, sticky="w")
champSourceFichier = tk.Entry(frameSource, width=40)
champSourceFichier.grid(row=1, column=1, padx=5)

# Bloc : Affichage du résultat
tk.Label(fen, text="Affichage du résultat").grid(row=4, column=0, sticky="w")
frameAffichage = tk.Frame(fen, bg="#C6E0B4", bd=2, relief="groove", padx=10, pady=10)
frameAffichage.grid(row=5, column=0, sticky="ew")

tk.Radiobutton(frameAffichage, text="Ecran", variable=choixAffichage, value=1, bg="#C6E0B4").grid(row=0, column=0, sticky="w")
tk.Radiobutton(frameAffichage, text="Fichier texte", variable=choixAffichage, value=2, bg="#C6E0B4").grid(row=1, column=0, sticky="w")
champAffichageFichier = tk.Entry(frameAffichage, width=40)
champAffichageFichier.grid(row=1, column=1, padx=5)

# Colonne droite

# Bloc : Mode de traitement
tk.Label(fen, text="Mode de traitement").grid(row=0, column=1, sticky="w", padx=40)
frameMode = tk.Frame(fen, bg="pink", bd=2, relief="groove", padx=10, pady=10)
frameMode.grid(row=1, column=1, sticky="w", padx=40, pady=(0, 20))

rbModeChiffrer = tk.Radiobutton(frameMode, text="Chiffrement",  variable=choixMode, value=1, bg="pink")
rbModeChiffrer.pack(anchor="w")
rbModeDechiffrer = tk.Radiobutton(frameMode, text="Déchiffrement", variable=choixMode, value=2, bg="pink")
rbModeDechiffrer.pack(anchor="w")

# Bouton valider
boutonValider = tk.Button(fen, text="Valider", bg="red", fg="black", font=("Arial", 10, "bold"), width=15, command=executerOperation)
boutonValider.grid(row=1, column=2, sticky="w")

# Bloc : Ecran d'affichage
tk.Label(fen, text="Ecran d'affichage").grid(row=2, column=1, sticky="w", padx=40)
zoneAffichage = tk.Text(fen, bg="pink", width=45, height=12)
zoneAffichage.grid(row=3, column=1, columnspan=2, rowspan=3, sticky="nw", padx=40)

# Lancement de la boucle Tkinter et update des champs de clé si besoin
updateUI_cle()
fen.mainloop()