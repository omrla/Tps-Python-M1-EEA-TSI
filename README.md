# 🐍 Travaux Pratiques Python — M1 EEA/TSI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow)
![OpenCV](https://img.shields.io/badge/Vision-OpenCV-green)
![Pandas](https://img.shields.io/badge/Data-Pandas-purple)
![NumPy](https://img.shields.io/badge/Math-NumPy-013243?logo=numpy)

</div>

---

**Auteurs :** Omar Lamari & Alexis Paris  
**Établissement :** Université de Bourgogne Europe  
**Filière :** M1 EEA/TSI — 2025/2026  
**Encadrants :** Mahdi Madani & Abdellah El-Zaar  

---

## 📋 Contenu du projet

| TP | Thème | Compétences clés |
|----|-------|-----------------|
| **TP 1** | Récursivité, tri et recherche dichotomique | Factorielle, Fibonacci, PGCD, Tri bulle/sélection/fusion, Dichotomie |
| **TP 2** | Chiffrement de César + Interface graphique | Cryptographie, Tkinter, Architecture MVC |
| **TP 3** | Programmation orientée objet | Classes, Héritage simple & multiple, Encapsulation |
| **TP 4** | Traitement d'images numériques | OpenCV, Convolution, Filtres Gauss & Sobel, Binarisation |
| **TP 5** | Analyse de données tabulaires | Pandas, Nettoyage, IMC, Normalisation min-max, Export CSV |

---

## 🔍 Détail des TPs

### TP 1 — Récursivité, tri et recherche dichotomique
Implémentation d'algorithmes fondamentaux en Python :
- Calcul récursif de la **factorielle**, de la suite de **Fibonacci** et du **PGCD**
- **Recherche dichotomique** dans une liste triée
- Trois algorithmes de tri : **tri à bulle**, **tri par sélection**, **tri par fusion**

---

### TP 2 — Application de chiffrement César

Application de chiffrement par décalage alphabétique avec interface graphique Tkinter.

**Architecture en deux couches :**
- `fonctions_cesar.py` — couche métier (chiffrement, déchiffrement, décodage de clé)
- `app_cesar.py` — couche IHM (interface Tkinter)

**Fonctionnalités :**
- Chiffrement / déchiffrement avec clé manuelle
- **Decoder_Cle_V1** : retrouve la clé à partir d'un caractère clair connu
- **Decoder_Cle_V2** : retrouve la clé par analyse de fréquence des lettres (lettre `e`)
- Source texte depuis saisie ou fichier — résultat vers écran ou fichier

---

### TP 3 — Programmation orientée objet

Modélisation d'une hiérarchie de personnages via un diagramme UML :

```
Personne
├── Etudiant      (compte : 100€, dépenses : 50€/achat)
│   └── Cadre     (compte : 2000€, salaire : 3000€/mois)
└── Fonctionnaire (compte : 1000€, salaire : 1800€/mois)
    └── Retraité  (héritage multiple Cadre + Fonctionnaire, pension : 80% ancien salaire)
```

---

### TP 4 — Traitement d'image numérique

Pipeline de traitement appliqué à l'image de référence **Barbara** (512×512 px, niveaux de gris) :

| Étape | Fonction | Description |
|-------|----------|-------------|
| Lecture | `Lire_Image` | Chargement via `cv2.imread` |
| Histogramme | `Calcul_Histo` / `Affiche_Histo` | Distribution des 256 niveaux de gris |
| Pixels | `Get_Pixel` / `Set_Pixel` | Accès et modification individuels |
| Binarisation | `Binarise_Image` | Seuillage avec `np.where` |
| Zoom | `Zoom_Zone` | Agrandissement par `np.repeat` |
| Convolution | `Filtre_Image` | Gauss (lissage) & Sobel (contours) |
| Sauvegarde | `Sauvegarde_Image` | Export PNG via `cv2.imwrite` |

---

### TP 5 — Analyse de données (fichier `individus.xlsx`)

Pipeline complet d'analyse avec Pandas :

```
Lecture Excel → Nettoyage (NaN, '?') → Calcul IMC → Filtrage → 
Fusion DataFrames → Statistiques descriptives → Normalisation min-max → Export CSV
```

**Résultats :** 5 fichiers CSV générés (`df2_nettoye`, `df3_avec_IMC`, `df4_masculin`, `df6_fusionne`, `df8_normalise`)

---

## 📁 Structure du dépôt

```
python-tps-m1-eeatsi/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── TPs_Python_LAMARI_PARIS.ipynb      ← Notebook complet (TP1 à TP5)
│
├── TP2_chiffrement_cesar/
│   ├── fonctions_cesar.py             ← Couche métier
│   └── app_cesar.py                   ← Interface Tkinter
│
├── assets/
│   └── barbara_ng.png                 ← Image de test (TP4)
│
└── rapport/
    └── RenduTPs_LAMARI_PARIS_PARIS.pdf ← Rapport complet (44 pages)
```

---

## ⚙️ Installation

```bash
# Cloner le dépôt
git clone https://github.com/<votre-username>/python-tps-m1-eeatsi.git
cd python-tps-m1-eeatsi

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'interface César (TP2)
cd TP2_chiffrement_cesar
python app_cesar.py

# Ouvrir le notebook complet
jupyter notebook TPs_Python_LAMARI_PARIS.ipynb
```

---

## 📦 Dépendances

Voir [`requirements.txt`](requirements.txt)

```
numpy
opencv-python
matplotlib
pandas
openpyxl
jupyter
```
