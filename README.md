
# 🏆 Projet 4 - Développez un programme logiciel en Python

Ce programme a été développé en **Python** et permet de **créer et organiser des tournois d'échecs**.  
Il fonctionne **hors ligne** et se lance via un **invite de commande**.  

✅ **Compatibilité** : Windows, Mac, Linux  
🎨 **Astuce** : Pour un meilleur affichage sous Windows 10, utilisez **Windows Terminal**.  

## ✨ Fonctionnalités principales

- 🏅 **Gestion des utilisateurs** : création, modification et suppression  
- 📅 **Gestion des tournois** : création, modification et suppression  
- 🔄 **Organisation des tours et des matchs** :
  - Chaque tournoi contient une liste de **tours**  
  - Chaque tour contient une liste de **matchs**  
  - Chaque match permet de **mettre à jour les scores des joueurs**  

> **💡 Remarque** : Bien que conçu pour les tournois d'échecs, ce programme peut être adapté à d'autres compétitions **1 contre 1**, car il n’utilise pas de vocabulaire spécifique aux échecs.

## 💾 Persistance des données

Le programme sauvegarde automatiquement toutes les données en local dans le dossier `data` :  

📂 **Utilisateurs** : `data/users.json`  
📂 **Tournois** : `data/tournaments/tournaments.json`  


# 🚀 Prérequis pour le premier lancement

Exécutez les commandes suivantes pour récupérer le projet et installer les dépendances :  

```bash
cd "Chemin\complet\vers\le\dossier\du\projet"
git init
git pull https://github.com/Matthieu-Chambon/OC_Projet_4.git main
pip install -r requirements.txt
```

# ▶️ Lancement du programme

```bash
cd "Chemin\complet\vers\le\dossier\du\projet"
py .\main.py
```

# 📝 Respect de la norme PEP 8

Le code respecte les **directives PEP 8**, avec une longueur de ligne limitée à **79 caractères**.  
Pour générer un **rapport Flake8** en format HTML :

```bash
flake8 --format=html --htmldir=flake-report
```

# 📂 Architecture MVC

Le programme suit l’architecture **MVC** (**Modèle - Vue - Contrôleur**) afin d’assurer **flexibilité** et **maintenabilité**.

### 🏗️ **Modèles (`models/`)**
Stocke les entités principales du programme :  
🔹 `User`  
🔹 `Tournament`  
🔹 `Round`  
🔹 `Match`

### 🔧 **Contrôleurs (`controllers/`)**
Gère la logique du programme :  
🔹 `Application` (contient les 3 autres contrôleurs)  
🔹 `UserManager`  
🔹 `TournamentManager`  
🔹 `MenuManager`  

### 🎨 **Vues (`views/`)**
Gère l'affichage avec la librairie **Rich** :  
🔹 `UserView`  
🔹 `TournamentView`  
🔹 `MenuView`  