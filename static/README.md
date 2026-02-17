# Module Static

## Description
Ce répertoire héberge tous les fichiers statiques publics de l'application. Ces fichiers sont servis directement au navigateur client sans modification par le serveur Flask.

## Contenu
* **`style.css`** : La feuille de style en cascade qui gère l'apparence de la calculatrice (couleurs, disposition Grid, Flexbox, etc.).

## Utilisation
Dans les templates HTML Flask, les fichiers de ce dossier doivent être référencés via la fonction `url_for`