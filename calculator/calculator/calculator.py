def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def root(a, b):
    if b == 0:
        raise ValueError("Cannot take root with degree zero")
    return a ** (1 / b)

def percent(a, b):
    return (a * b) / 100

def main():
    print("=== Calculatrice Interactive ===")
    operations = {
        '1': ('Addition', add),
        '2': ('Soustraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide),
        '5': ('Puissance', power),
        '6': ('Racine', root),
        '7': ('Pourcentage', percent)
    }
    historique = []
    while True:
        print("\nChoisis une opération :")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("8. Afficher l'historique")
        print("9. Quitter")
        choix = input("Numéro : ").strip()
        if choix == '9':
            print("Au revoir !")
            break
        if choix == '8':
            print("\n--- Historique des calculs ---")
            if not historique:
                print("Aucun calcul effectué.")
            else:
                for h in historique:
                    print(h)
            continue
        if choix not in operations:
            print("Choix invalide.")
            continue
        try:
            # Libellés personnalisés selon l'opération
            if choix == '6':  # Racine
                a = input("Nombre : ")
                b = input("Degré de la racine : ")
            elif choix == '7':  # Pourcentage
                a = input("Valeur : ")
                b = input("Pourcentage (%) : ")
            elif choix == '5':  # Puissance
                a = input("Base : ")
                b = input("Exposant : ")
            else:
                a = input("Premier nombre : ")
                b = input("Deuxième nombre : ")
            # Gestion des complexes
            if 'j' in a or 'j' in b:
                a = complex(a)
                b = complex(b)
            else:
                a = float(a)
                b = float(b)
            resultat = operations[choix][1](a, b)
            print(f"Résultat : {resultat}")
            historique.append(f"{operations[choix][0]}({a}, {b}) = {resultat}")
        except ValueError as e:
            print(f"Erreur : {e}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    main()
