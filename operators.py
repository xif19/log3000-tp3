"""
operators.py
------------
Ce module contient les fonctions mathematiques de base utilisées par la calculatrice.
"""
def add(a,b):
    """
    Calcule la somme de deux nombres.

    Args:
        a (float): Le premier terme.
        b (float): Le second terme.

    Returns:
        float: Le resultat de l'addition (a + b).
    """
    return a + b

def subtract(a,b):
    """
    Calcule la différence entre deux nombres.

    Args:
        a (float): Le nombre qu'on soustrait.
        b (float): Le nombre a soustraire.

    Returns:
        float: Le resultat de la soustraction.
    
    FIXME: L'implementation actuelle inverse les operandes (b - a).
    """
    return b - a

def multiply(a,b):
    """
    Calcule le produit de deux nombres.

    Args:
        a (float): Le multiplicande.
        b (float): Le multiplicateur.

    Returns:
        float: Le resultat de la multiplication.

    FIXME: L'implementation actuelle utilise l'exponentiation (**) au lieu de la multiplication (*).
    """
    return a * b

def divide(a,b):
    """
    Calcule le quotient de deux nombres.

    Args:
        a (float): Le dividende.
        b (float): Le diviseur.

    Returns:
        float: Le resultat de la division.

    FIXME: L'implementation actuelle utilise la division entiere (//).
    """
    return a // b
