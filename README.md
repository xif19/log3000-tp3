# CALCULATRICE WEB FLASK - **Équipe 32**

## Description du Projet
Bienvenue dans le dépôt de la Calculatrice Web. Il s'agit d'une application web simple permettant d'effectuer des opérations arithmétiques de base (addition, soustraction, multiplication, division). 

Le projet est conçu avec une architecture MVC légère :
* **Backend** : Python avec le framework Flask pour le routage et la logique métier.
* **Frontend** : HTML5 et CSS3 pour l'interface utilisateur.

L'application est construite avec un backend Python avec Flask et une interface frontend en HTML/CSS.

## Prérequis d’installation
Avant de commencer, il faut avoir:

* **Python 3.8+**
* **pip**
* **Git**

## Instructions d’installation

### 1. Cloner le dépot
```bash
git clone https://github.com/xif19/log3000-tp3.git
```

### 2. Créer un environnement virtuel dans le terminal
Windows: 
```bash
python -m venv venv
venv\Scripts\activate
```

Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install flask
```

## Utilisation

### 1. Démarrer l'application
A la racine du projet on éxecute:
```bash
python app.py
```

### 2. Accéder a l'application
L'application va être accessible à l'addresse : http://127.0.0.1:5000/

### 3. Utiliser l'application

Faire un calcul
* Cliquez sur les boutons pour entrer une opération (ex: `1 + 2`).
    * Cliquez sur `=` pour voir le résultat.
    * Cliquez sur `C` pour effacer.

## Tests
*Section en construction.*
Actuellement, les tests sont effectues manuellement via l'interface web. Un framework de tests unitaires (comme `pytest`) sera intégre prochainement pour tester automatiquement les fonctions dans `operators.py`.

Pour tester manuellement :
1. Lancez l'app.
2. Essayez une addition simple (`2+2`).
3. Vérifiez si le résultat affiché est `4.0`.

## Flux de Contribution

Nous suivons un flux de travail basé sur les branches.

1.  **Issues** : Consultez l'onglet "Issues" de GitHub pour voir les bugs à corriger.
2.  **Branche** : Créez une branche pour votre tâche :
    ```bash
    git checkout -b fix/nom-du-bug

    git checkout -b feat/nouvelle-fonctionnalite
    ```
3.  **Commit** : Faites vos modifications et committez avec des messages clairs.
4.  **Pull Request** : Poussez votre branche et ouvrez une Pull Request (PR) vers la branche `main`. Demandez une revue de code avant de fusionner.

---
**Structure du Projet**
* `app.py` : Contrôleur principal et point d'entrée.
* `operators.py` : Logique fonctionnelle.
* `templates/` : Vues HTML.
* `static/` : Styles CSS et assets.