# Tests module

Ce dossier contient les tests automatisés du projet avec `unittest`.

## Prérequis

- Python 3.8+
- Les dépendances du projet installées dans l'environnement virtuel (`flask`)

## Exécution des tests

Depuis la racine du projet:

```bash
venv\Scripts\python -m unittest discover -s tests -v
```

## Couverture actuelle

- `tests/test_operators.py`
  - Vérifie les 4 opérations de base dans `operators.py`.
  - Met en evidence les écarts entre le comportement attendu et le comportement réel.
- `tests/test_app.py`
  - Vérifie `calculate()` (parsing + routage vers les operateurs).
  - Vérifie le endpoint Flask `GET /` et `POST /` avec un client de test.

## Pourquoi certains tests échouent

Les tests sont écrits selon le comportement mathematique correct attendu.
Si un test échoue, cela signale un bogue fonctionnel à corriger, puis à relancer.