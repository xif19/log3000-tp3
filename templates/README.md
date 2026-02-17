# Module Templates

## Description
Ce répertoire contient les fichiers HTML utilisés par Flask pour le rendu de l'interface utilisateur. Le projet utilise le moteur de template **Jinja2** (intégré à Flask), ce qui permet d'insérer dynamiquement des données depuis le backend (Python) vers le frontend (HTML).

## Fichiers
* **`index.html`** : Le fichier principal de l'application. Il contient :
    * La structure de la calculatrice.
    * Le formulaire HTML `<form>` qui envoie les données à `app.py`.
    * Le code JavaScript minimal pour gérer les clics sur les boutons (cote client).

## Dépendances
* Ce dossier est requis par `flask.render_template`.
* Il dépend du dossier `../static` pour les fichiers CSS.