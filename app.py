"""
app.py
------
Le point d'entrée principal de l'application Flask.
Ce fichier gere les routes web, le traitement des requetes HTTP et l'orchestration de la logique de calcul.
"""
from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Mapping des symboles d'operateurs vers les bonnes fonctions
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Analyse une expression sous forme de chaine et effectue le calcul et gere des expressions simples à deux operandes.

    Args:
        expr (str): L'expression mathematique brute reçue.

    Returns:
        float: Le résultat numerique de l'operation.

    Raises:
        ValueError: Si l'expression est vide, contient plusieurs operateurs, ou si les operandes ne sont pas numeriques.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Suppression des espaces pour simplifier le parsing
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche de l'operateur et de sa position
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                # Limitation actuelle : ne supporte qu'un seul opérateur par calcul
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Validation de la position de l'operateur (ne peut pas etre au debut ou à la fin)
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    # Separation des operandes gauche et droit
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Execution de la fonction correspondante via le dictionnaire OPS
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Gere la route racine ('/').
    
    GET: Affiche la calculatrice avec un ecran vide.
    POST: Recupere l'expression du formulaire, tente de la calculer 
          et renvoie la page avec le résultat ou une erreur.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)