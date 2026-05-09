# Travaux Pratiques Python - M1 EEA/TSI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow)
![OpenCV](https://img.shields.io/badge/Vision-OpenCV-green)
![Pandas](https://img.shields.io/badge/Data-Pandas-purple)
![NumPy](https://img.shields.io/badge/Math-NumPy-013243?logo=numpy)

</div>

---

**Auteurs :** Omar Lamari & Alexis Paris  
**Etablissement :** Universite de Bourgogne Europe  
**Filiere :** M1 EEA/TSI - 2025/2026  
**Encadrants :** Mahdi Madani & Abdellah El-Zaar  

---

## Rapport et enonce

- [Telecharger le rapport complet (PDF)](rapport/RenduTPs_LAMARI_PARIS_PARIS.pdf)
- [Telecharger l'enonce officiel (PDF)](rapport/TPs_Python_M1.pdf)

---

## Contenu du projet

| TP | Theme | Competences cles |
|----|-------|-----------------|
| **TP 1** | Recursivite, tri et recherche dichotomique | Factorielle, Fibonacci, PGCD, Tri bulle/selection/fusion, Dichotomie |
| **TP 2** | Chiffrement de Cesar + Interface graphique | Cryptographie, Tkinter, Architecture MVC |
| **TP 3** | Programmation orientee objet | Classes, Heritage simple & multiple, Encapsulation |
| **TP 4** | Traitement d'images numeriques | OpenCV, Convolution, Filtres Gauss & Sobel, Binarisation |
| **TP 5** | Analyse de donnees tabulaires | Pandas, Nettoyage, IMC, Normalisation min-max, Export CSV |

---

## Detail des TPs

### TP 1 - Recursivite, tri et recherche dichotomique
Implementation d'algorithmes fondamentaux en Python :
- Calcul recursif de la **factorielle**, de la suite de **Fibonacci** et du **PGCD**
- **Recherche dichotomique** dans une liste triee
- Trois algorithmes de tri : **tri a bulle**, **tri par selection**, **tri par fusion**

---

### TP 2 - Application de chiffrement Cesar

Application de chiffrement par decalage alphabetique avec interface graphique Tkinter.

**Architecture en deux couches :**
- `fonctions_cesar.py` - couche metier (chiffrement, dechiffrement, decodage de cle)
- `app_cesar.py` - couche IHM (interface Tkinter)

**Fonctionnalites :**
- Chiffrement / dechiffrement avec cle manuelle
- **Decoder_Cle_V1** : retrouve la cle a partir d'un caractere clair connu
- **Decoder_Cle_V2** : retrouve la cle par analyse de frequence des lettres (lettre `e`)
- Source texte depuis saisie ou fichier - resultat vers ecran ou fichier

---

### TP 3 - Programmation orientee objet

Modelisation d'une hierarchie de personnages via un diagramme UML :

```
Personne
├── Etudiant      (compte : 100€, depenses : 50€/achat)
│   └── Cadre     (compte : 2000€, salaire : 3000€/mois)
└── Fonctionnaire (compte : 1000€, salaire : 1800€/mois)
    └── Retraite  (heritage multiple Cadre + Fonctionnaire, pension : 80% ancien salaire)
```

---

### TP 4 - Traitement d'image numerique

Pipeline de traitement applique a l'image de reference **Barbara** (512x512 px, niveaux de gris) :

| Etape | Fonction | Description |
|-------|----------|-------------|
| Lecture | `Lire_Image` | Chargement via `cv2.imread` |
| Histogramme | `Calcul_Histo` / `Affiche_Histo` | Distribution des 256 niveaux de gris |
| Pixels | `Get_Pixel` / `Set_Pixel` | Acces et modification individuels |
| Binarisation | `Binarise_Image` | Seuillage avec `np.where` |
| Zoom | `Zoom_Zone` | Agrandissement par `np.repeat` |
| Convolution | `Filtre_Image` | Gauss (lissage) & Sobel (contours) |
| Sauvegarde | `Sauvegarde_Image` | Export PNG via `cv2.imwrite` |

---

### TP 5 - Analyse de donnees (fichier `individus.xlsx`)

Pipeline complet d'analyse avec Pandas :

```
Lecture Excel -> Nettoyage (NaN, '?') -> Calcul IMC -> Filtrage ->
Fusion DataFrames -> Statistiques descriptives -> Normalisation min-max -> Export CSV
```

**Resultats :** 5 fichiers CSV generes (`df2_nettoye`, `df3_avec_IMC`, `df4_masculin`, `df6_fusionne`, `df8_normalise`)

---

## Structure du depot

```
python-tps-m1-eeatsi/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── TPs_Python_LAMARI_PARIS.ipynb      <- Notebook complet (TP1 a TP5)
│
├── TP2_chiffrement_cesar/
│   ├── fonctions_cesar.py             <- Couche metier
│   └── app_cesar.py                   <- Interface Tkinter
│
├── assets/
│   └── barbara_ng.png                 <- Image de test (TP4)
│
└── rapport/
    ├── RenduTPs_LAMARI_PARIS_PARIS.pdf <- Rapport complet (44 pages)
    └── TPs_Python_M1.pdf               <- Enonce officiel
```

---

## Installation

```bash
git clone https://github.com/omrla/Tps-Python-M1-EEA-TSI.git
cd Tps-Python-M1-EEA-TSI

pip install -r requirements.txt

cd TP2_chiffrement_cesar
python app_cesar.py

jupyter notebook TPs_Python_LAMARI_PARIS.ipynb
```

---

## Dependances

Voir [`requirements.txt`](requirements.txt)

```
numpy
opencv-python
matplotlib
pandas
openpyxl
jupyter
```
