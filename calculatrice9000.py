def saisir_nombre():
    while True:
        try:
            nombre = float(input("Entrez un nombre : "))
            return nombre
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

def saisir_operateur():
    operateurs_valides = ['+', '-', '*', '/']
    while True:
        operateur = input("Entrez un opérateur (+, -, *, /) : ")
        if operateur in operateurs_valides:
            return operateur
        else:
            print("Erreur : Opérateur invalide. Veuillez choisir parmi '+', '-', '*', '/'.")

def calculer(nombre1, operateur, nombre2):
    if operateur == '+':
        return nombre1 + nombre2
    elif operateur == '-':
        return nombre1 - nombre2
    elif operateur == '*':
        return nombre1 * nombre2
    elif operateur == '/':
        if nombre2 == 0:
            raise ValueError("Erreur : Division par zéro.")
        return nombre1 / nombre2

def calculatrice():
    print("Calculatrice simple - Entrez 'exit' pour quitter.")
    
    while True:
        try:
            nombre1 = saisir_nombre()
            operateur = saisir_operateur()
            nombre2 = saisir_nombre()

            resultat = calculer(nombre1, operateur, nombre2)
            print(f"Résultat : {resultat}")

        except ValueError as e:
            print(f"Erreur : {str(e)}")
        except KeyboardInterrupt:
            print("\nAu revoir !")
            break

if __name__ == "__main__":
    calculatrice()

